"""Turn a raw screen recording into a polished product demo.

Adds: a framed layout on a soft background (rounded corners, shadow), smooth
eased zooms on chosen areas, click highlights, sped-up waiting parts with a
visible "×N" badge, a title card and a closing card. Keeps the original audio.

Usage:
    python3 polish.py raw.mp4 edit.json out.mp4

edit.json (all times in seconds of the RAW video, x/y as 0–1 of the screen):
{
  "subtitle": "Un dossier traité de bout en bout",
  "outro": ["thinkactionn.com", "Réservez une démo de 20 minutes"],
  "zooms":  [{"start": 4, "end": 10, "x": 0.30, "y": 0.40, "scale": 1.8}],
  "clicks": [{"t": 5.2, "x": 0.31, "y": 0.42}],
  "speed":  [{"start": 20, "end": 50, "factor": 6}]
}
"""
import json, math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
FW, FH = 1680, 945            # framed screen size inside the canvas
FX, FY = (W - FW) // 2, (H - FH) // 2 + 6
RADIUS = 18
EASE = 0.8                    # seconds for zoom in / out
INTRO, OUTRO, XFADE = 2.6, 3.2, 0.5
NAVY, NAVY2, AMBER, WHITE, MUTED = (15, 31, 61), (27, 48, 89), (245, 166, 35), (255, 255, 255), (150, 165, 195)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans{}.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT.format("-Bold" if bold else ""), size)


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate:format=duration", "-of", "json", path],
                         capture_output=True, text=True, check=True).stdout
    d = json.loads(out)
    s = d["streams"][0]
    num, den = map(int, s["r_frame_rate"].split("/"))
    has_audio = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                                "stream=index", "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip() != ""
    return s["width"], s["height"], num / den, float(d["format"]["duration"]), has_audio


def smooth(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def background(with_shadow=True):
    """Soft navy gradient with a faint glow; the frame's drop shadow is optional."""
    y = np.linspace(0, 1, H)[:, None]
    x = np.linspace(0, 1, W)[None, :]
    base = np.array(NAVY, float)
    top = np.array(NAVY2, float)
    img = np.zeros((H, W, 3), float)
    for c in range(3):
        img[..., c] = base[c] + (top[c] - base[c]) * (0.6 * y + 0.4 * x)
    glow = np.exp(-(((x - 0.5) / 0.45) ** 2 + ((y - 0.5) / 0.4) ** 2))
    img += glow[..., None] * np.array([20, 25, 40], float)
    bg = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    if not with_shadow:
        return bg
    shadow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shadow).rounded_rectangle([FX, FY + 14, FX + FW, FY + FH + 14], RADIUS, fill=150)
    shadow = shadow.filter(ImageFilter.GaussianBlur(28))
    bg.paste((5, 10, 22), (0, 0), shadow)
    return bg


def frame_mask():
    m = Image.new("L", (FW * 2, FH * 2), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, FW * 2 - 1, FH * 2 - 1], RADIUS * 2, fill=255)
    return m.resize((FW, FH), Image.LANCZOS)


def centered(d, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)


def card(bg, lines):
    im = bg.copy()
    d = ImageDraw.Draw(im)
    y = H / 2 - 30 * len(lines) - 20
    for i, (text, size, bold, color) in enumerate(lines):
        centered(d, y, text, font(size, bold), color)
        y += size + 28
    return im


def build_timeline(dur, fps, speed):
    """List of raw-video times to sample, one per output frame."""
    segs = sorted(speed, key=lambda s: s["start"])
    times, t = [], 0.0
    step = 1.0 / fps
    while t < dur - 1e-6:
        f = next((s["factor"] for s in segs if s["start"] <= t < s["end"]), 1)
        times.append((t, f))
        t += step * f
    return times


def zoom_at(t, zooms):
    z, cx, cy = 1.0, 0.5, 0.5
    for k in zooms:
        w = smooth((t - k["start"]) / EASE) * smooth((k["end"] - t) / EASE)
        if w > 0:
            z += w * (k["scale"] - 1)
            cx += w * (k["x"] - 0.5)
            cy += w * (k["y"] - 0.5)
    return z, cx, cy


def main(src, cfg_path, out):
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    sw, sh, fps, dur, has_audio = probe(src)
    fps = min(fps, 30)
    zooms, clicks, speed = cfg.get("zooms", []), cfg.get("clicks", []), cfg.get("speed", [])
    timeline = build_timeline(dur, fps, speed)
    bg, mask = background(), frame_mask()
    plain = background(with_shadow=False)
    intro = card(plain, [("Owl", 96, True, AMBER), (cfg.get("subtitle", ""), 44, True, WHITE),
                      ("ThinkAction", 28, False, MUTED)])
    outro_lines = cfg.get("outro", ["thinkactionn.com"])
    outro = card(plain, [("Owl", 80, True, AMBER)] + [(l, 44 if i == 0 else 32, i == 0, WHITE if i == 0 else MUTED)
                                                    for i, l in enumerate(outro_lines)])

    reader = subprocess.Popen(["ffmpeg", "-v", "error", "-i", src, "-vf", f"fps={fps}", "-f", "rawvideo",
                               "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    total_out = len(timeline)
    audio_filter, amap = [], []
    if has_audio:
        parts, t0 = [], 0.0
        for s in sorted(speed, key=lambda s: s["start"]):
            parts.append((t0, s["start"], 1)); parts.append((s["start"], s["end"], s["factor"])); t0 = s["end"]
        parts.append((t0, dur, 1))
        chains = []
        for i, (a, b, f) in enumerate(p for p in parts if p[1] > p[0]):
            tempo = ",".join(["atempo=2.0"] * int(math.log(f, 2)) + ([f"atempo={f / 2 ** int(math.log(f, 2)):.4f}"] if f > 1 else []))
            vol = ",volume=0" if f > 1 else ""
            chains.append(f"[1:a]atrim={a}:{b},asetpts=PTS-STARTPTS{(',' + tempo) if tempo else ''}{vol}[a{i}]")
        n = len(chains)
        audio_filter = chains + ["".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,adelay={int(INTRO * 1000)}|{int(INTRO * 1000)}[aout]"]
        amap = ["-filter_complex", ";".join(audio_filter), "-map", "0:v", "-map", "[aout]", "-c:a", "aac", "-b:a", "160k"]
    writer = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                               "-r", str(fps), "-i", "-"] + (["-i", src] if has_audio else []) + amap +
                              ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                               "-movflags", "+faststart", out], stdin=subprocess.PIPE)

    def emit(im):
        writer.stdin.write(im.tobytes())

    def render(raw, t, f):
        z, cx, cy = zoom_at(t, zooms)
        cw, ch = sw / z, sh / z
        x0 = min(max(cx * sw - cw / 2, 0), sw - cw)
        y0 = min(max(cy * sh - ch / 2, 0), sh - ch)
        shot = raw.resize((FW, FH), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))
        d = ImageDraw.Draw(shot, "RGBA")
        for c in clicks:
            age = t - c["t"]
            if 0 <= age < 0.6:
                px = (c["x"] * sw - x0) / cw * FW
                py = (c["y"] * sh - y0) / ch * FH
                r = 14 + 46 * smooth(age / 0.6)
                a = int(200 * (1 - age / 0.6))
                d.ellipse([px - r - 3, py - r - 3, px + r + 3, py + r + 3], outline=NAVY + (a,), width=4)
                d.ellipse([px - r, py - r, px + r, py + r], outline=WHITE + (a,), width=4)
                d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=NAVY + (int(a * 0.6),), outline=WHITE + (a,), width=2)
        im = bg.copy()
        im.paste(shot, (FX, FY), mask)
        if f > 1:
            d2 = ImageDraw.Draw(im)
            label = f"×{f}"
            fnt = font(30, True)
            tw = d2.textlength(label, font=fnt)
            d2.rounded_rectangle([FX + FW - tw - 52, FY + 20, FX + FW - 20, FY + 70], 14, fill=NAVY)
            d2.text((FX + FW - tw - 36, FY + 28), label, font=fnt, fill=AMBER)
        return im

    # intro
    n_intro = int(INTRO * fps)
    frames_needed = {round(t * fps): (t, f) for t, f in timeline}
    idx, out_i, last = 0, 0, None
    raw_size = sw * sh * 3
    rendered_first = None
    while True:
        chunk = reader.stdout.read(raw_size)
        if len(chunk) < raw_size:
            break
        if idx in frames_needed:
            t, f = frames_needed[idx]
            raw = Image.frombuffer("RGB", (sw, sh), chunk)
            im = render(raw, t, f)
            if rendered_first is None:
                rendered_first = im
                for i in range(n_intro):
                    a = smooth((i - (n_intro - XFADE * fps)) / (XFADE * fps))
                    emit(Image.blend(intro, im, a) if a > 0 else intro)
            emit(im)
            last = im
            out_i += 1
        idx += 1
    for i in range(int(OUTRO * fps)):
        a = smooth(i / (XFADE * fps))
        emit(Image.blend(last, outro, a) if a < 1 else outro)
    writer.stdin.close()
    writer.wait()
    reader.wait()
    print(f"done: {out}  ({out_i} video frames + intro/outro, {fps:.0f} fps)")


if __name__ == "__main__":
    main(*sys.argv[1:4])
