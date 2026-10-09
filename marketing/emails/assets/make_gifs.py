"""Generate the Owl email GIFs: a 3-step flow animation and a video thumbnail."""
import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
F = "/usr/share/fonts/truetype/dejavu/"
def font(size, bold=False):
    return ImageFont.truetype(F + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), size)

NAVY = (15, 31, 61)
NAVY2 = (27, 48, 89)
AMBER = (245, 166, 35)
WHITE = (255, 255, 255)
MUTED = (140, 158, 190)
GREEN = (46, 204, 113)
S = 2  # supersample for smooth edges


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def centered(d, cx, y, text, f, fill):
    w = d.textlength(text, font=f)
    d.text((cx - w / 2, y), text, font=f, fill=fill)


# ---------- 1. Flow GIF (600x300) ----------
STEPS = [
    ("1", "Activité &", "régime de TVA", "Lus pour chaque client"),
    ("2", "Écritures", "comptables", "Générées automatiquement"),
    ("3", "Déclaration", "de TVA", "Prête à contrôler"),
]


def flow_frame(active, progress, done):
    W, H = 600 * S, 300 * S
    im = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(im)
    centered(d, W / 2, 22 * S, "Comment Owl traite un dossier", font(20 * S, True), WHITE)
    cw, ch, gap, top = 160 * S, 170 * S, 30 * S, 80 * S
    x0 = (W - (3 * cw + 2 * gap)) / 2
    for i, (num, l1, l2, sub) in enumerate(STEPS):
        x = x0 + i * (cw + gap)
        on = i < active or (i == active and progress > 0)
        t = 1.0 if i < active else (progress if i == active else 0.0)
        border = mix(NAVY2, AMBER, t)
        d.rounded_rectangle([x, top, x + cw, top + ch], 14 * S, fill=NAVY2, outline=border, width=3 * S)
        cx = x + cw / 2
        r = 20 * S
        circ = GREEN if (i < active or (done and i == 2)) else mix(MUTED, AMBER, t)
        d.ellipse([cx - r, top + 16 * S, cx + r, top + 16 * S + 2 * r], fill=circ)
        mark = "✓" if (i < active or (done and i == 2)) else num
        centered(d, cx, top + 23 * S, mark, font(20 * S, True), NAVY)
        tc = WHITE if on or not active else MUTED
        centered(d, cx, top + 72 * S, l1, font(17 * S, True), tc)
        centered(d, cx, top + 94 * S, l2, font(17 * S, True), tc)
        centered(d, cx, top + 130 * S, sub, font(10 * S), MUTED)
        if i < 2:  # arrow
            ax, ay = x + cw + 6 * S, top + ch / 2
            ac = AMBER if i < active else MUTED
            d.line([ax, ay, ax + gap - 12 * S, ay], fill=ac, width=3 * S)
            d.polygon([(ax + gap - 12 * S, ay - 6 * S), (ax + gap - 4 * S, ay), (ax + gap - 12 * S, ay + 6 * S)], fill=ac)
    footer = "Votre collaborateur contrôle et valide." if done else "thinkactionn.com  ·  Owl"
    centered(d, W / 2, 268 * S, footer, font(13 * S, done), GREEN if done else MUTED)
    return im.resize((600, 300), Image.LANCZOS)


frames, durs = [], []
# First frame: all three steps visible (Outlook shows only this one)
frames.append(flow_frame(0, 0, False)); durs.append(1400)
for step in range(3):
    for k in range(1, 6):
        frames.append(flow_frame(step, k / 5, False)); durs.append(90)
    frames.append(flow_frame(step + 1 if step < 2 else 2, 1.0 if step == 2 else 0, False)); durs.append(700)
frames.append(flow_frame(3, 0, True)); durs.append(2600)
frames[0].save(OUT + "/owl-flow.gif", save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True)


# ---------- 2. Video thumbnail GIF (600x338) ----------
ROWS = [
    ("401000", "Fournisseur Métro", "1 250,00"),
    ("445660", "TVA déductible 20 %", "250,00"),
    ("607000", "Achats marchandises", "1 000,00"),
    ("411000", "Client Dupont SARL", "3 600,00"),
    ("445710", "TVA collectée 20 %", "600,00"),
]


def thumb_frame(rows_shown, pulse):
    W, H = 600 * S, 338 * S
    im = Image.new("RGB", (W, H), (233, 237, 244))
    d = ImageDraw.Draw(im)
    # app window
    d.rounded_rectangle([20 * S, 18 * S, 580 * S, 320 * S], 10 * S, fill=WHITE, outline=(205, 212, 225), width=S)
    d.rounded_rectangle([20 * S, 18 * S, 580 * S, 50 * S], 10 * S, fill=NAVY)
    d.rectangle([20 * S, 40 * S, 580 * S, 50 * S], fill=NAVY)
    d.text((36 * S, 25 * S), "Owl", font=font(15 * S, True), fill=AMBER)
    d.text((80 * S, 27 * S), "Dossier : Boulangerie Martin  ·  Activité : commerce  ·  TVA mensuelle", font=font(11 * S), fill=WHITE)
    # table header
    y = 66 * S
    for x, h in ((40, "Compte"), (130, "Libellé"), (450, "Montant")):
        d.text((x * S, y), h, font=font(11 * S, True), fill=MUTED)
    d.line([36 * S, y + 20 * S, 564 * S, y + 20 * S], fill=(225, 230, 238), width=S)
    for i in range(rows_shown):
        ry = y + (30 + i * 30) * S
        acc, lab, amt = ROWS[i]
        d.text((40 * S, ry), acc, font=font(12 * S, True), fill=NAVY)
        d.text((130 * S, ry), lab, font=font(12 * S), fill=(60, 70, 90))
        d.text((450 * S, ry), amt + " €", font=font(12 * S), fill=(60, 70, 90))
        d.text((540 * S, ry), "✓", font=font(12 * S, True), fill=GREEN)
    # dim overlay + play button
    ov = Image.new("RGBA", (W, H), (15, 31, 61, 95))
    im = Image.alpha_composite(im.convert("RGBA"), ov)
    d = ImageDraw.Draw(im)
    cx, cy = W / 2, 165 * S
    r = (40 + 6 * pulse) * S
    d.ellipse([cx - r - 10 * S, cy - r - 10 * S, cx + r + 10 * S, cy + r + 10 * S], fill=(245, 166, 35, int(70 * (1 - pulse))))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AMBER + (255,))
    t = 16 * S
    d.polygon([(cx - t * 0.7, cy - t), (cx - t * 0.7, cy + t), (cx + t * 1.1, cy)], fill=WHITE)
    # caption pill
    cap = "Démo : un dossier traité en 2 minutes"
    f = font(14 * S, True)
    tw = d.textlength(cap, font=f)
    d.rounded_rectangle([cx - tw / 2 - 16 * S, 245 * S, cx + tw / 2 + 16 * S, 277 * S], 16 * S, fill=NAVY + (235,))
    d.text((cx - tw / 2, 252 * S), cap, font=f, fill=WHITE)
    return im.convert("RGB").resize((600, 338), Image.LANCZOS)


tf, td = [], []
tf.append(thumb_frame(5, 0)); td.append(1200)  # first frame: full table + play button
for n in range(0, 6):
    for p in (0.0, 0.5, 1.0, 0.5):
        tf.append(thumb_frame(n, p)); td.append(110)
for p in (0.0, 0.5, 1.0, 0.5, 0.0, 0.5, 1.0, 0.5):
    tf.append(thumb_frame(5, p)); td.append(140)
tf[0].save(OUT + "/owl-video-thumb.gif", save_all=True, append_images=tf[1:], duration=td, loop=0, optimize=True)
tf[0].save(OUT + "/owl-video-thumb.png")
