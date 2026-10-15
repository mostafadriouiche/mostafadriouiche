"""Animate a few app screenshots into a short demo video (same look as polish.py).

Each shot: a screenshot, a camera path (eased zoom/pan), an animated cursor
gliding between points, click rings and a French caption. Shots crossfade,
with a short title card at the start and a closing card at the end.

Usage:
    python3 slides.py storyboard.json out.mp4 [out.gif]
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw
from polish import (W, H, FW, FH, FX, FY, NAVY, AMBER, WHITE, MUTED,
                    background, frame_mask, card, smooth, font)

FPS = 30
XF = 0.35  # crossfade seconds


def interp(keys, t):
    """keys: [[t, a, b, ...], ...] -> eased interpolation of the values at time t."""
    if t <= keys[0][0]:
        return keys[0][1:]
    for k0, k1 in zip(keys, keys[1:]):
        if t <= k1[0]:
            u = smooth((t - k0[0]) / (k1[0] - k0[0]))
            return [p + (q - p) * u for p, q in zip(k0[1:], k1[1:])]
    return keys[-1][1:]


def cursor_sprite(scale=1.0):
    s = 2
    pts = [(0, 0), (0, 26), (7, 20), (13, 32), (17, 30), (11, 18), (20, 18)]
    im = Image.new("RGBA", (40 * s, 44 * s))
    d = ImageDraw.Draw(im)
    d.polygon([(4 * s + x * s * 1.15, 4 * s + y * s * 1.15) for x, y in pts], fill=(0, 0, 0, 255), outline=(255, 255, 255, 255))
    d.line([(4 * s + x * s * 1.15, 4 * s + y * s * 1.15) for x, y in pts + pts[:1]], fill=(255, 255, 255, 255), width=3)
    return im.resize((int(40 * scale), int(44 * scale)), Image.LANCZOS)


def render_shot(shot, img, t, bg, mask, cur):
    sw, sh = img.size
    cx, cy, z = interp(shot["camera"], t)
    cw, ch = sw / z, sw / z * FH / FW
    if ch > sh:
        ch = sh; cw = ch * FW / FH
    x0 = min(max(cx - cw / 2, 0), sw - cw)
    y0 = min(max(cy - ch / 2, 0), sh - ch)
    view = img.resize((FW, FH), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
    to_frame = lambda px, py: ((px - x0) / cw * FW, (py - y0) / ch * FH)
    d = ImageDraw.Draw(view, "RGBA")
    for c in shot.get("clicks", []):
        age = t - c[0]
        if 0 <= age < 0.6:
            px, py = to_frame(c[1], c[2])
            r = 14 + 40 * smooth(age / 0.6)
            a = int(220 * (1 - age / 0.6))
            d.ellipse([px - r - 3, py - r - 3, px + r + 3, py + r + 3], outline=NAVY + (a,), width=4)
            d.ellipse([px - r, py - r, px + r, py + r], outline=AMBER + (a,), width=4)
    if shot.get("cursor"):
        px, py = to_frame(*interp(shot["cursor"], t))
        press = any(0 <= t - c[0] < 0.15 for c in shot.get("clicks", []))
        sp = cur if not press else cur.resize((int(cur.width * 0.88), int(cur.height * 0.88)))
        view.paste(sp, (int(px - 5), int(py - 5)), sp)
    im = bg.copy()
    im.paste(view, (FX, FY), mask)
    cap = shot.get("caption")
    if cap:
        a = smooth(t / 0.4) * smooth((shot["dur"] - t) / 0.3)
        layer = Image.new("RGBA", im.size)
        dc = ImageDraw.Draw(layer)
        fnt = font(38, True)
        tw = dc.textlength(cap, font=fnt)
        base_y = FY + 34 if shot.get("caption_pos") == "top" else FY + FH - 112
        x, y = (W - tw) / 2, base_y + 10 * (1 - smooth(t / 0.4))
        dc.rounded_rectangle([x - 30, y - 18, x + tw + 30, y + 62], 20, fill=NAVY + (int(232 * a),))
        dc.text((x, y), cap, font=fnt, fill=WHITE + (int(255 * a),))
        im = Image.alpha_composite(im.convert("RGBA"), layer).convert("RGB")
    return im


def main(story_path, out, gif=None):
    st = json.load(open(story_path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(story_path))
    bg, mask, plain = background(), frame_mask(), background(with_shadow=False)
    cur = cursor_sprite(1.25)
    imgs = []
    for s in st["shots"]:
        imgs.append(Image.open(os.path.join(base, s["image"])).convert("RGB"))
    intro = card(plain, [("Owl", 96, True, AMBER), (st["title"], 44, True, WHITE), ("ThinkAction", 28, False, MUTED)])
    outro = card(plain, [("Owl", 84, True, AMBER)] + [(l, 46 if i == 0 else 32, i == 0, WHITE if i == 0 else MUTED)
                                                    for i, l in enumerate(st["outro"])])
    seq = [("card", intro, st["intro_dur"])] + [("shot", i, s["dur"]) for i, s in enumerate(st["shots"])] + [("card", outro, st["outro_dur"])]
    starts, t = [], 0.0
    for kind, ref, dur in seq:
        starts.append(t); t += dur - XF
    total = t + XF
    frames = int(round(total * FPS))

    def at(i, tl):
        kind, ref, dur = seq[i]
        if kind == "card":
            return ref
        return render_shot(st["shots"][ref], imgs[ref], tl, bg, mask, cur)

    w = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                          "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for n in range(frames):
        tt = n / FPS
        live = [i for i in range(len(seq)) if starts[i] <= tt < starts[i] + seq[i][2]]
        i = live[-1]
        im = at(i, tt - starts[i])
        if len(live) > 1:
            j = live[0]
            a = smooth((tt - starts[i]) / XF)
            im = Image.blend(at(j, tt - starts[j]), im, a)
        w.stdin.write(im.tobytes())
    w.stdin.close(); w.wait()
    print(f"video: {out} ({total:.1f}s)")
    if gif:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-vf",
                        "fps=15,scale=800:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer:bayer_scale=4",
                        gif], check=True)
        print(f"gif: {gif}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
