"""Remove the 'Activate Windows' watermark from Owl screenshots by rebuilding
that corner: row backgrounds, table column lines, the green 'Écriture
équilibrée' badge, and the dark text (numbers, badge label) copied back.

Usage: python3 clean_screens.py in.png out.png
"""
import sys
import numpy as np
from PIL import Image, ImageDraw

BOX = (1540, 915, 1876, 1000)      # watermark area (x0, y0, x1, y1)
PILL = (234, 246, 238)              # badge background colour


def row_mode(a, y, x0=1100, x1=1540):
    keys, cnt = np.unique(a[y, x0:x1].reshape(-1, 3), axis=0, return_counts=True)
    return keys[cnt.argmax()]


def clean(src, dst):
    im = Image.open(src).convert("RGB")
    a = np.array(im).astype(int)
    orig = a.copy()
    x0, y0, x1, y1 = BOX
    y1 = min(y1, a.shape[0])
    v = orig.mean(axis=2)

    # 1. each row gets the background colour of the same row further left
    for y in range(y0, y1):
        a[y, x0:x1] = row_mode(orig, y)
    footer_y = next(y for y in range(y0, y1) if tuple(row_mode(orig, y)) != (255, 255, 255))

    # 2. table column lines, sampled from a clean row above
    for x in range(x0, x1):
        c = orig[880, x]
        if 150 < c.mean() < 240:
            a[y0:footer_y, x] = c

    # 3. dark text in the table row (e.g. "9608,33")
    keep = v[y0:footer_y, x0:x1] < 170
    a[y0:footer_y, x0:x1][keep] = orig[y0:footer_y, x0:x1][keep]

    # 4. the green badge, if present: redraw the pill, copy its icon and label
    pill = np.all(np.abs(orig[footer_y:y1, x0:x1] - PILL) <= 2, axis=2)
    if pill.sum() > 200:
        ys, xs = np.nonzero(pill)
        px0, px1 = x0 + xs.min() - 1, x0 + xs.max() + 1
        py0, py1 = footer_y + ys.min(), footer_y + ys.max()
        out = Image.fromarray(a.clip(0, 255).astype(np.uint8))
        ImageDraw.Draw(out).rounded_rectangle([px0, py0, px1, py1], (py1 - py0) // 2, fill=PILL)
        a = np.array(out).astype(int)
        region = (slice(py0, py1 + 1), slice(px0, px1 + 1))
        dark = v[region] < 170
        a[region][dark] = orig[region][dark]

    Image.fromarray(a.clip(0, 255).astype(np.uint8)).save(dst)


if __name__ == "__main__":
    clean(sys.argv[1], sys.argv[2])
