"""Generate a Stardew Valley style typing GIF (pixel font, parchment panel).

Output: assets/stardew-typing.gif  (+ a PNG preview frame for quick checks)
"""

import pathlib

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT_PATH = ASSETS / "PressStart2P-Regular.ttf"

W, H = 600, 200
SKY_TOP, SKY_BOT = (143, 214, 242), (211, 238, 249)
GRASS, GRASS_DARK = (111, 191, 62), (86, 166, 43)
PARCH_TOP, PARCH_BOT = (252, 242, 218), (238, 218, 192)
WOOD, WOOD_DARK, GOLD, INK = (74, 44, 23), (46, 27, 14), (242, 193, 78), (74, 44, 23)

title = "ZetvD"
subtitle = "FULLSTACK DEV // COZY FARMER"

f_title = ImageFont.truetype(str(FONT_PATH), 56)
f_sub = ImageFont.truetype(str(FONT_PATH), 11)


def gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size)
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(1, h - 1)
        d.line(
            [(0, y), (w, y)],
            fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bottom)),
        )
    return img


def panel_layer():
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle(
        [58, 38, 542, 162], radius=14, fill=PARCH_TOP, outline=WOOD, width=7
    )
    d.rounded_rectangle([70, 50, 530, 150], radius=9, outline=(139, 94, 52), width=3)
    for cx, cy in [(78, 58), (522, 58), (78, 142), (522, 142)]:
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(139, 94, 52))
    return layer


def base_frame():
    img = gradient((W, H), SKY_TOP, SKY_BOT)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 140, W, H], fill=GRASS)
    d.rectangle([0, 168, W, H], fill=GRASS_DARK)
    # grass tufts
    for x in (60, 150, 300, 420, 520):
        d.polygon([(x - 6, 170), (x - 3, 158), (x, 170)], fill=(62, 123, 39))
        d.polygon([(x, 170), (x + 3, 154), (x + 7, 170)], fill=(70, 160, 46))
    sun = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sun).ellipse([516, 22, 570, 76], fill=(247, 208, 70, 255))
    ImageDraw.Draw(sun).ellipse([526, 32, 560, 66], fill=(251, 227, 138, 255))
    img = Image.alpha_composite(img.convert("RGBA"), sun)
    img = Image.alpha_composite(img, panel_layer())
    return img


def render(prefix, cursor_on, show_sub):
    img = base_frame()
    d = ImageDraw.Draw(img)
    full_w = d.textlength(title, font=f_title)
    start_x = (W - full_w) / 2
    d.text((start_x, 96), prefix, font=f_title, fill=INK, anchor="lm")
    if cursor_on:
        cx = start_x + d.textlength(prefix, font=f_title) + 6
        d.rectangle([cx, 74, cx + 6, 120], fill=WOOD_DARK)
    if show_sub:
        d.text((W / 2, 136), subtitle, font=f_sub, fill=(139, 94, 52), anchor="mm")
    return img.convert("RGB")


def main() -> None:
    frames = []
    # typing
    for i in range(1, len(title) + 1):
        f = render(title[:i], cursor_on=True, show_sub=False)
        frames += [f, f, f]
    # blink + subtitle
    full = render(title, cursor_on=True, show_sub=True)
    blank = render(title, cursor_on=False, show_sub=True)
    frames += [full, blank, full, blank, full, blank]
    frames += [blank, full]

    gif = ASSETS / "stardew-typing.gif"
    frames[0].save(
        gif,
        save_all=True,
        append_images=frames[1:],
        duration=110,
        loop=0,
        optimize=True,
    )
    render("Zetv", cursor_on=True, show_sub=True).save(
        ASSETS / "stardew-typing-preview.png"
    )
    print(
        f"wrote {gif.relative_to(ROOT)} ({gif.stat().st_size / 1024:.1f} KB, {len(frames)} frames)"
    )


if __name__ == "__main__":
    main()
