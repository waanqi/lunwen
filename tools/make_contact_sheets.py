from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw


src = Path(sys.argv[1])
out = Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
files = sorted(src.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
cols, rows = 4, 4
thumb_w, thumb_h = 300, 424
margin = 20
for sheet_index in range(0, len(files), cols * rows):
    batch = files[sheet_index:sheet_index + cols * rows]
    sheet = Image.new("RGB", (cols * (thumb_w + margin) + margin, rows * (thumb_h + 36 + margin) + margin), "#d9d9d9")
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(batch):
        img = Image.open(path).convert("RGB")
        img.thumbnail((thumb_w, thumb_h))
        x = margin + (i % cols) * (thumb_w + margin)
        y = margin + (i // cols) * (thumb_h + 36 + margin)
        sheet.paste(img, (x + (thumb_w - img.width) // 2, y))
        draw.text((x, y + thumb_h + 6), path.stem, fill="black")
    sheet.save(out / f"contact-{sheet_index // (cols * rows) + 1}.png")
