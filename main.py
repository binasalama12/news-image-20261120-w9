#!/usr/bin/env python3
"""Warm Postcard - Friday 20 November 2026, one day of world news in one picture.

A front page drawn from scratch with PIL: warm paper, a double postcard frame,
three hero stories stacked on the left, the day's other 32 stories on the right,
a 4/5/4 pictured grid, a dot-matrix world map and a date-check box.
Run: python3 main.py  (writes entry.png, 1024x1024)
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1600
PAPER = (247, 238, 220)
PAPER2 = (250, 244, 231)
INK = (44, 33, 24)
MUT = (112, 96, 78)
TERRA = (176, 70, 38)
RED = (168, 32, 40)
GOLD = (178, 136, 52)
CREAM = (255, 250, 238)
OLIVE = (108, 108, 58)
NAVY = (38, 60, 96)
TEAL = (42, 110, 110)
SKY_DUSK = (52, 66, 96)

FD = "/usr/share/fonts/truetype/dejavu/"
FL = "/usr/share/fonts/truetype/liberation/"


def F(name, size):
    try:
        return ImageFont.truetype(FD + name, size)
    except Exception:
        return ImageFont.load_default()


def FLF(name, size):
    try:
        return ImageFont.truetype(FL + name, size)
    except Exception:
        return ImageFont.truetype(FD + "DejaVuSerif.ttf", size)


SANS = "DejaVuSans.ttf"
BOLD = "DejaVuSans-Bold.ttf"
SERIF = "LiberationSerif-Regular.ttf"
SERIFB = "LiberationSerif-Bold.ttf"
SERIFI = "LiberationSerif-Italic.ttf"


def wrap(d, text, font, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, text, font, w, lh, color, max_lines=None):
    lines = wrap(d, text, font, w)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and d.textlength(lines[-1] + "…", font=font) > w:
            lines[-1] = lines[-1][:-1]
        lines[-1] = lines[-1].rstrip() + "…"
    for ln in lines:
        d.text((x, y), ln, font=font, fill=color)
        y += lh
    return y


def fit1(d, x, y, text, name, size, w, color):
    while size > 9:
        f = F(name, size)
        if d.textlength(text, font=f) <= w:
            break
        size -= 1
    d.text((x, y), text, font=F(name, size), fill=color)
    return size


def paper(w, h, base, seed=7, amp=6):
    im = Image.new("RGB", (w, h), base)
    px = im.load()
    rnd = random.Random(seed)
    for yy in range(h):
        for xx in range(w):
            if rnd.random() < 0.28:
                n = rnd.randint(-amp, amp)
                r, g, b = px[xx, yy]
                px[xx, yy] = (max(0, min(255, r + n)), max(0, min(255, g + n)),
                              max(0, min(255, b + n)))
    return im


def sky(d, x, y, w, h, top, bot):
    for i in range(h):
        t = i / max(1, h - 1)
        c = tuple(int(top[k] + (bot[k] - top[k]) * t) for k in range(3))
        d.line([(x, y + i), (x + w, y + i)], fill=c)


def sun(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    for k in range(8):
        a = k * math.pi / 4
        d.line([(cx + int(math.cos(a) * (r + 4)), cy + int(math.sin(a) * (r + 4))),
                (cx + int(math.cos(a) * (r + 15)), cy + int(math.sin(a) * (r + 15)))],
               fill=color, width=3)


def stars(d, x, y, w, h, n, seed=3):
    rnd = random.Random(seed)
    for _ in range(n):
        px = x + rnd.randint(0, w - 1)
        py = y + rnd.randint(0, h - 1)
        r = rnd.choice([1, 1, 2])
        d.ellipse([px - r, py - r, px + r, py + r], fill=(255, 255, 240))


def flag(d, x, y, w, h, kind):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=1)
    if kind == "us":
        for i in range(7):
            d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7],
                        fill=(178, 34, 52) if i % 2 == 0 else CREAM)
        d.rectangle([x, y, x + w * 0.4, y + h * 0.55], fill=NAVY)
    elif kind == "cn":
        d.rectangle([x, y, x + w, y + h], fill=(206, 40, 40))
        sun(d, x + w * 0.22, y + h * 0.28, 3, (255, 220, 60))
    elif kind == "ru":
        d.rectangle([x, y, x + w, y + h / 3], fill=CREAM)
        d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(40, 80, 170))
        d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(200, 40, 40))


def scene(d, x, y, w, h, kind):
    x, y, w, h = int(x), int(y), int(w), int(h)
    if kind == "storm":
        sky(d, x, y, w, h, (28, 52, 66), (72, 112, 132))
        d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(16, 40, 56))
        cx, cy = x + w * 0.42, y + h * 0.36
        for k in range(5):
            r = 11 + k * 9
            d.arc([cx - r, cy - r * 0.8, cx + r, cy + r * 0.8],
                  20 + k * 40, 200 + k * 40, fill=(240, 244, 246), width=3)
        rnd = random.Random(11)
        for _ in range(24):
            rx = x + rnd.randint(0, w)
            ry = y + rnd.randint(0, int(h * 0.6))
            d.line([(rx, ry), (rx - 4, ry + 12)], fill=(200, 220, 230), width=2)
        d.polygon([(x, y + h), (x, y + h * 0.86), (x + w * 0.5, y + h * 0.8),
                   (x + w, y + h * 0.88), (x + w, y + h)], fill=(120, 100, 60))
    elif kind == "missile":
        sky(d, x, y, w, h, (18, 22, 44), (62, 52, 72))
        stars(d, x, y, w, int(h * 0.4), 18, seed=7)
        rnd = random.Random(5)
        bx = x
        while bx < x + w:
            bw = rnd.randint(18, 46)
            bh = rnd.randint(int(h * 0.3), int(h * 0.75))
            d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(30, 32, 52))
            bx += bw + 3
        d.line([(x + w * 0.08, y + h * 0.55), (x + w * 0.78, y + h * 0.34)],
               fill=(240, 180, 60), width=3)
        sun(d, x + w * 0.82, y + h * 0.42, 13, (255, 140, 40))
    elif kind == "summit":
        sky(d, x, y, w, h, (70, 80, 120), (220, 170, 120))
        rnd = random.Random(9)
        bx = x
        while bx < x + w:
            bw = rnd.randint(22, 50)
            bh = rnd.randint(int(h * 0.35), int(h * 0.7))
            d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(52, 52, 74))
            bx += bw + 4
        fy = y + h * 0.18
        flag(d, x + w * 0.14, fy, 34, 22, "us")
        flag(d, x + w * 0.44, fy, 34, 22, "cn")
        flag(d, x + w * 0.74, fy, 34, 22, "ru")
        sun(d, x + w * 0.88, y + h * 0.22, 10, (255, 210, 110))
    elif kind == "bridge":
        sky(d, x, y, w, h, (120, 160, 190), (240, 210, 160))
        sun(d, x + w * 0.8, y + h * 0.24, 12, (255, 190, 80))
        d.rectangle([x, y + h * 0.68, x + w, y + h], fill=(50, 90, 120))
        d.arc([x + w * 0.1, y + h * 0.2, x + w * 0.9, y + h * 1.1],
              180, 360, fill=(60, 60, 70), width=5)
        d.line([(x, y + h * 0.66), (x + w, y + h * 0.66)], fill=(60, 60, 70), width=4)
        for k in range(6):
            px = x + w * (0.15 + k * 0.13)
            d.line([(px, y + h * 0.66), (px, y + h * 0.5)], fill=(60, 60, 70), width=2)
    elif kind == "climate":
        sky(d, x, y, w, h, (30, 90, 110), (150, 200, 190))
        sun(d, x + w * 0.82, y + h * 0.22, 13, (255, 205, 90))
        d.ellipse([x + w * 0.28, y + h * 0.22, x + w * 0.72, y + h * 0.85],
                  fill=(70, 130, 180), outline=CREAM, width=3)
        d.ellipse([x + w * 0.36, y + h * 0.34, x + w * 0.52, y + h * 0.5], fill=(90, 170, 90))
        d.ellipse([x + w * 0.55, y + h * 0.55, x + w * 0.66, y + h * 0.68], fill=(90, 170, 90))
        d.rectangle([x, y + h * 0.85, x + w, y + h], fill=(90, 130, 70))
    elif kind in ("law", "court"):
        sky(d, x, y, w, h, (200, 180, 140), (240, 225, 190))
        d.rectangle([x + w * 0.1, y + h * 0.72, x + w * 0.9, y + h * 0.8], fill=(120, 100, 70))
        for k in range(4):
            cx = x + w * (0.18 + k * 0.21)
            d.rectangle([cx - 8, y + h * 0.3, cx + 8, y + h * 0.72], fill=(235, 228, 205))
            d.rectangle([cx - 13, y + h * 0.26, cx + 13, y + h * 0.3], fill=(200, 180, 130))
        d.polygon([(x + w * 0.08, y + h * 0.26), (x + w * 0.92, y + h * 0.26),
                   (x + w * 0.5, y + h * 0.06)], fill=(190, 160, 110))
    elif kind == "markets":
        d.rectangle([x, y, x + w, y + h], fill=(24, 26, 34))
        rnd = random.Random(21)
        cx = x + w * 0.08
        prev = y + h * 0.3
        while cx < x + w * 0.92:
            cw = rnd.randint(8, 16)
            top = min(prev + rnd.randint(4, 10), y + int(h * 0.55))
            bot = min(top + rnd.randint(10, 22), y + int(h * 0.88))
            col = (200, 60, 60) if rnd.random() < 0.7 else (70, 180, 90)
            d.rectangle([cx, top, cx + cw, bot], fill=col)
            d.line([(cx + cw / 2, top - 6), (cx + cw / 2, bot + 6)], fill=col, width=2)
            prev = top
            cx += cw + 6
        d.line([(x + w * 0.05, y + h * 0.3), (x + w * 0.95, y + h * 0.75)],
               fill=(255, 120, 90), width=3)
    elif kind == "games":
        sky(d, x, y, w, h, (240, 130, 80), (60, 40, 90))
        sun(d, x + w * 0.5, y + h * 0.42, 16, (255, 220, 120))
        rnd = random.Random(13)
        bx = x
        while bx < x + w:
            bw = rnd.randint(20, 44)
            bh = rnd.randint(int(h * 0.3), int(h * 0.6))
            d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(40, 30, 60))
            bx += bw + 3
        d.rectangle([x, y + h * 0.85, x + w, y + h], fill=(30, 90, 90))
    elif kind == "space":
        d.rectangle([x, y, x + w, y + h], fill=(8, 10, 26))
        stars(d, x, y, w, h, 40, seed=17)
        d.ellipse([x + w * 0.68, y + h * 0.12, x + w * 0.92, y + h * 0.38],
                  fill=(200, 210, 230))
        d.ellipse([x + w * 0.72, y + h * 0.16, x + w * 0.78, y + h * 0.24], fill=(170, 180, 200))
        d.ellipse([x + w * 0.82, y + h * 0.26, x + w * 0.88, y + h * 0.33], fill=(170, 180, 200))
        px, py = x + w * 0.3, y + h * 0.55
        d.rectangle([px - 26, py - 6, px - 8, py + 6], fill=(150, 160, 180))
        d.rectangle([px + 8, py - 6, px + 26, py + 6], fill=(150, 160, 180))
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=(220, 200, 120))
        d.line([(px, py - 9), (px + 16, py - 26)], fill=CREAM, width=2)
        d.ellipse([px + 13, py - 29, px + 19, py - 23], fill=(255, 255, 240))
    elif kind == "drought":
        sky(d, x, y, w, h, (240, 190, 120), (250, 230, 180))
        sun(d, x + w * 0.78, y + h * 0.26, 15, (255, 170, 60))
        d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(170, 120, 70))
        rnd = random.Random(31)
        for _ in range(10):
            cx = x + rnd.randint(0, w)
            cy = y + int(h * 0.68) + rnd.randint(0, int(h * 0.28))
            d.line([(cx, cy), (cx + rnd.randint(-18, 18), cy + rnd.randint(4, 14))],
                   fill=(110, 70, 35), width=2)
        d.polygon([(x, y + h * 0.62), (x + w * 0.3, y + h * 0.55),
                   (x + w * 0.6, y + h * 0.62), (x + w, y + h * 0.56),
                   (x + w, y + h * 0.62)], fill=(140, 100, 55))
    elif kind == "nuclear":
        sky(d, x, y, w, h, (140, 150, 170), (220, 210, 190))
        d.rectangle([x, y + h * 0.78, x + w, y + h], fill=(110, 110, 100))
        d.polygon([(x + w * 0.2, y + h * 0.78), (x + w * 0.3, y + h * 0.2),
                   (x + w * 0.5, y + h * 0.2), (x + w * 0.6, y + h * 0.78)],
                  fill=(200, 195, 180))
        d.polygon([(x + w * 0.62, y + h * 0.78), (x + w * 0.68, y + h * 0.35),
                   (x + w * 0.82, y + h * 0.35), (x + w * 0.88, y + h * 0.78)],
                  fill=(180, 175, 160))
        for k in range(3):
            d.ellipse([x + w * (0.32 + k * 0.06), y + h * (0.08 + k * 0.05),
                       x + w * (0.4 + k * 0.06), y + h * (0.16 + k * 0.05)],
                      fill=(235, 235, 230))
    elif kind == "diplomacy":
        sky(d, x, y, w, h, (90, 110, 150), (230, 200, 160))
        d.rectangle([x, y + h * 0.7, x + w, y + h], fill=(90, 80, 60))
        d.rectangle([x + w * 0.15, y + h * 0.62, x + w * 0.85, y + h * 0.7], fill=(70, 55, 40))
        flag(d, x + w * 0.18, y + h * 0.2, 36, 24, "us")
        flag(d, x + w * 0.46, y + h * 0.14, 36, 24, "cn")
        flag(d, x + w * 0.72, y + h * 0.2, 36, 24, "ru")
        d.line([(x + w * 0.18, y + h * 0.2), (x + w * 0.18, y + h * 0.62)], fill=INK, width=2)
        d.line([(x + w * 0.46, y + h * 0.14), (x + w * 0.46, y + h * 0.62)], fill=INK, width=2)
        d.line([(x + w * 0.72, y + h * 0.2), (x + w * 0.72, y + h * 0.62)], fill=INK, width=2)
    elif kind == "tanker":
        sky(d, x, y, w, h, (150, 180, 200), (240, 220, 180))
        sun(d, x + w * 0.85, y + h * 0.2, 11, (255, 200, 90))
        d.rectangle([x, y + h * 0.66, x + w, y + h], fill=(40, 80, 110))
        for k in range(4):
            d.line([(x, y + h * (0.72 + k * 0.07)), (x + w, y + h * (0.72 + k * 0.07))],
                   fill=(120, 170, 200), width=2)
        d.polygon([(x + w * 0.12, y + h * 0.62), (x + w * 0.88, y + h * 0.62),
                   (x + w * 0.8, y + h * 0.78), (x + w * 0.2, y + h * 0.78)],
                  fill=(60, 50, 45))
        for k, col in enumerate([(200, 60, 50), (50, 120, 80), (220, 170, 60)]):
            d.rectangle([x + w * (0.2 + k * 0.2), y + h * 0.44,
                         x + w * (0.36 + k * 0.2), y + h * 0.6], fill=col)
        d.rectangle([x + w * 0.78, y + h * 0.4, x + w * 0.86, y + h * 0.6], fill=CREAM)
    elif kind == "cricket":
        sky(d, x, y, w, h, (140, 180, 210), (230, 235, 200))
        d.rectangle([x, y + h * 0.6, x + w, y + h], fill=(90, 150, 80))
        d.rectangle([x + w * 0.38, y + h * 0.6, x + w * 0.62, y + h], fill=(210, 190, 140))
        for k in range(3):
            d.line([(x + w * (0.44 + k * 0.05), y + h * 0.22),
                    (x + w * (0.44 + k * 0.05), y + h * 0.42)], fill=(240, 220, 120), width=3)
        d.ellipse([x + w * 0.7, y + h * 0.3, x + w * 0.76, y + h * 0.38], fill=(178, 40, 40))
        d.line([(x + w * 0.7, y + h * 0.3), (x + w * 0.5, y + h * 0.55)],
               fill=(178, 40, 40), width=2)
    else:
        sky(d, x, y, w, h, (120, 140, 170), (220, 210, 180))
        sun(d, x + w * 0.5, y + h * 0.4, 12, (255, 200, 100))


HEROES = [
    dict(num=1, kicker="1 · ODISHA · STORM", scene="storm",
         head="Akvan comes ashore on the Odisha coast",
         dek=("Cyclone Akvan crossed the coast near Gopalpur at noon, winds 90-100 km/h "
              "gusting to 110. 300,000 people moved to safety, 423 rescue teams deployed."),
         src="IMD · THE HINDU"),
    dict(num=2, kicker="2 · RIYADH · ATTACK", scene="missile",
         head="Houthi missile hits Riyadh's KAFD financial district",
         dek=("A Houthi missile damaged a wealth-fund tower in the financial district, "
              "one of Riyadh's tallest. No casualties are reported."),
         src="ARAB NEWS · REUTERS"),
    dict(num=3, kicker="3 · SHENZHEN · DIPLOMACY", scene="summit",
         head="Trump, Xi and Putin issue a joint declaration",
         dek=("No big peace deal from the trilateral's second day. Trump says the Iran war "
              "call waits until 2027 and rates the summit '12 out of 10'."),
         src="REUTERS · AP"),
]

PICTURED = [
    dict(num=4, kicker="4 · KERCH STRAIT · WAR", scene="bridge",
         head="Crimean Bridge hit a third time this week; rail halted",
         dek=("A Ukrainian naval drone strike disrupted rail traffic on the bridge. "
              "Rail partly resumes; Putin vows retaliation, and Kyiv was hit by drones."),
         src="CLAIM · KYIV"),
    dict(num=5, kicker="5 · SHENZHEN · SUMMIT", scene="diplomacy",
         head="APEC leaders meet in Shenzhen",
         dek=("Leaders gather in China for the APEC summit. Xi urges APEC economies "
              "to back open trade and new technology."),
         src="AP"),
    dict(num=6, kicker="6 · ANTALYA · CLIMATE", scene="climate",
         head="COP31's final day: fossil fuels cut from the text",
         dek=("A revised draft strips out every fossil-fuel phase-out pledge. Delegates "
              "push back as the final plenary meets today."),
         src="UNFCCC · AFP"),
    dict(num=7, kicker="7 · THE HAGUE · LAW", scene="law",
         head="The world answers the genocide verdict",
         dek=("Britain expels Myanmar's defence attache and seeks an urgent Security "
              "Council meeting. The Gambia hails a 'historic' verdict."),
         src="AP · BBC"),
    dict(num=8, kicker="8 · NEW YORK · MARKETS", scene="markets",
         head="Anthropic's debut can't stop the slide",
         dek=("The Dow fell 1,084 points, the S&P 2.02% and the Nasdaq 2.25%, as the AI "
              "selloff bit a day after Anthropic's record debut."),
         src="BLOOMBERG"),
    dict(num=9, kicker="9 · VICE CITY · GAMES", scene="games",
         head="GTA VI passes The Odyssey's $1.84bn",
         dek=("Launch-day sales top The Odyssey's $1.80bn global run, Sensor Tower "
              "estimates. Reviews land; Rockstar calls it the highest-rated game ever."),
         src="SENSOR TOWER"),
    dict(num=10, kicker="10 · SPACE · SCIENCE", scene="space",
         head="NASA confirms Voyager 1's light-day milestone",
         dek=("The probe is now a full light-day from Earth - 16 billion miles out, "
              "the farthest any human-made object has ever travelled."),
         src="NASA · JPL"),
    dict(num=11, kicker="11 · SEOUL · LAW", scene="court",
         head="South Korea clears ex-PM Han",
         dek=("The Supreme Court overturns former prime minister Han Duck-soo's "
              "conviction, in the case tied to the 2024 martial-law declaration."),
         src="KOREA TIMES"),
    dict(num=12, kicker="12 · SUVA · CLIMATE", scene="drought",
         head="Fiji declares a national disaster over drought",
         dek=("Fiji declares a national disaster over drought and water shortages. "
              "El Nino leaves water short across the islands."),
         src="AFP"),
    dict(num=13, kicker="13 · VIENNA · SECURITY", scene="nuclear",
         head="North Korea expands uranium enrichment at Yongbyon",
         dek=("The UN watchdog reports growth at the nuclear site, in its latest "
              "assessment of the Yongbyon complex."),
         src="IAEA"),
    dict(num=14, kicker="14 · CARACAS · DIPLOMACY", scene="diplomacy",
         head="US and Venezuela restore military cooperation",
         dek=("The two countries sign an agreement to work together again, restoring "
              "a military channel closed for years."),
         src="REUTERS"),
    dict(num=15, kicker="15 · HORMUZ · CONFLICT", scene="tanker",
         head="ADNOC vessel attacked in the Strait of Hormuz",
         dek=("One crew member is missing after the strike on the ADNOC vessel "
              "in the strait."),
         src="REUTERS"),
    dict(num=16, kicker="16 · WELLINGTON · CRICKET", scene="cricket",
         head="Day two at the Basin: Nicholls' 113 anchors New Zealand",
         dek=("New Zealand build on Henry Nicholls' unbeaten 113 as India hunt early "
              "wickets, in the first Test at the Basin Reserve."),
         src="AP"),
]

BRIEFS = [
    (17, "BRUSSELS", "EU-UK summit opens"),
    (18, "NEW DELHI", "Modi meets William and Kate"),
    (19, "DHAKA", "Fire at the Yunus home; arson feared"),
    (20, "MUMBAI", "Sensex +1.21%, Nifty +1.14% on the day"),
    (21, "TOKYO", "Hayabusa2 gives up landing; mission rewritten"),
    (22, "BERLIN", "Coalition of the Willing meets in Berlin"),
    (23, "BERLIN", "Merz hosts Qatar's emir in Berlin"),
    (24, "NEW DELHI", "Pakistan minister leads delegation to Delhi for SCO"),
    (25, "MANILA", "Philippines-Chile trade deal signed"),
    (26, "MANILA", "Musk plans Philippines projects"),
    (27, "HONG KONG", "India beats Malaysia, Asian Hockey Trophy opens"),
    (28, "IPOH", "Harimau Shakti exercise opens in Ipoh"),
    (29, "NEW DELHI", "India's electronics exports jump 44%"),
    (30, "NEW DELHI", "ICMR completes 100 tech transfers"),
    (31, "NEW DELHI", "India unveils its first bird-flu vaccine"),
    (32, "GENEVA", "World Children's Day marked worldwide"),
    (33, "EUROPE", "Youth anti-war protests across Europe"),
    (34, "BRUSSELS", "EU delays its methane rules by 24 months"),
    (35, "COLOGNE", "Bayern Munich beat Koln 3-0"),
    (36, "U17 CUP", "Argentina 0-2 Australia at the U17 Cup"),
    (37, "WASHINGTON", "Jobless claims come in at 203,000"),
    (38, "STRASBOURG", "NATO's assembly opens its 72nd session"),
    (39, "HANOI", "Azerbaijan's Aliyev visits Vietnam"),
    (40, "MARKETS", "Crude futures fall over 3%"),
    (41, "KHARTOUM", "Sudan army: two-year El Obeid siege broken"),
    (42, "MOGADISHU", "Somalia gives UAE ambassador 72 hours to leave"),
    (43, "SAN SALVADOR", "Migrant boat capsizes off El Salvador; dozens missing"),
    (44, "PORT-AU-PRINCE", "Haiti approves Salvadoran troop deal vs gangs"),
    (45, "ARABIAN SEA", "Amur falcons cross the Arabian Sea"),
    (46, "NEW YORK", "Al-Saadi appears in a New York court over a UK plot"),
    (47, "KYIV", "Witkoff and Kushner brief Zelenskyy"),
    (48, "BEIJING", "Xi urges APEC to back open trade, new tech"),
]

TIMELINE = [
    ("OVERNIGHT", "Crimean Bridge hit a third time"),
    ("~06:00 UTC", "APEC leaders meet in Shenzhen"),
    ("~10:00 UTC", "Trilateral declaration issued"),
    ("~12:00 UTC", "Akvan makes landfall in Odisha"),
    ("~14:00 UTC", "Houthi missile hits Riyadh KAFD"),
    ("LATE", "Wall Street slides; Dow -1,084"),
]

REGIONS = [
    ("EUROPE", 13, (52, 84, 140)),
    ("THE AMERICAS", 8, (46, 120, 80)),
    ("ASIA-PACIFIC", 19, (176, 60, 50)),
    ("MIDEAST", 2, (110, 80, 140)),
    ("AFRICA", 2, (200, 120, 40)),
    ("OCEANIA", 2, (40, 130, 130)),
    ("WORLD", 2, (110, 110, 110)),
]

DATECHECK = ("Left out - they broke before Friday: the ICJ genocide ruling on Myanmar itself "
             "(Thursday 19 Nov) - Friday's news is the world's answer to it - Denmark's "
             "Greenland-US pact (19 Nov) - Anthropic's $81.34bn IPO (19 Nov); its first "
             "trading day was Thursday - Germany's electricity-tax cut (18 Nov) - the "
             "Crimean Bridge span collapse (17-18 Nov). Not yet: the trilateral's first "
             "meeting was 19 Nov; the joint declaration is Friday's.")

FOOT1 = ("Every story here happened, or was first reported, on Friday 20 November 2026, "
         "in some time zone. Disputed claims are attributed, not stated as fact.")
FOOT2 = ("Sources: Reuters - AP - AFP - BBC - Bloomberg - IMD - NASA - IAEA - The Hindu - "
         "Arab News - Sensor Tower. Original drawings, drawn for this page.")

PINS = {
    4: (36, 45), 5: (114, 22), 6: (30, 37), 7: (4, 52), 8: (-74, 41),
    9: (-80, 26), 10: (-95, 25), 11: (127, 37), 12: (178, -18),
    13: (126, 40), 14: (-67, 10), 15: (56, 26), 16: (175, -41),
}


CONTINENTS = [
    [(-168, 66), (-150, 70), (-130, 71), (-110, 72), (-95, 80), (-80, 73),
     (-65, 62), (-55, 52), (-60, 46), (-70, 42), (-75, 35), (-81, 26),
     (-87, 21), (-95, 16), (-100, 20), (-108, 25), (-117, 32), (-124, 42),
     (-130, 55), (-150, 60), (-165, 60)],
    [(-80, 9), (-72, 11), (-62, 9), (-52, 4), (-44, -3), (-35, -8),
     (-39, -15), (-41, -22), (-48, -27), (-57, -34), (-66, -41), (-69, -52),
     (-72, -54), (-74, -44), (-73, -30), (-72, -18), (-77, -8), (-81, -1)],
    [(-10, 36), (-2, 37), (3, 38), (8, 39), (14, 40), (19, 42), (23, 36),
     (26, 38), (28, 41), (30, 44), (28, 50), (24, 56), (21, 60), (18, 62),
     (12, 61), (6, 58), (4, 55), (-1, 50), (-5, 48), (-9, 43)],
    [(-17, 15), (-15, 25), (-9, 30), (-2, 35), (8, 37), (11, 34), (20, 32),
     (30, 31), (34, 28), (38, 22), (43, 12), (51, 11), (48, 2), (41, -6),
     (40, -15), (36, -22), (32, -28), (26, -33), (20, -35), (16, -30),
     (13, -20), (12, -12), (9, -4), (9, 4), (-8, 5), (-13, 9)],
    [(30, 44), (38, 46), (44, 48), (50, 52), (58, 55), (66, 60), (70, 68),
     (78, 72), (90, 75), (105, 77), (120, 74), (135, 72), (150, 70),
     (162, 68), (170, 66), (178, 65), (172, 62), (162, 58), (156, 52),
     (146, 46), (140, 40), (132, 36), (128, 34), (122, 30), (118, 24),
     (110, 20), (106, 10), (101, 7), (97, 12), (92, 20), (88, 22), (80, 16),
     (76, 10), (72, 20), (66, 25), (60, 25), (54, 27), (48, 29), (43, 33),
     (40, 37), (35, 42)],
    [(113, -22), (114, -30), (116, -35), (124, -33), (130, -32), (136, -35),
     (140, -38), (146, -39), (150, -37), (153, -28), (150, -23), (146, -19),
     (142, -16), (137, -12), (132, -12), (127, -14), (122, -17), (118, -20)],
]


def inside(lon, lat, poly):
    ok = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > lat) != (y2 > lat):
            xin = x1 + (lat - y1) * (x2 - x1) / (y2 - y1)
            if lon < xin:
                ok = not ok
    return ok


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(26, 38, 62))
    step = 7
    gy = y
    while gy < y + h:
        gx = x
        while gx < x + w:
            lon = (gx - x) / w * 360 - 180
            lat = 80 - (gy - y) / h * 140
            if any(inside(lon, lat, p) for p in CONTINENTS):
                d.rectangle([gx, gy, gx + 2, gy + 2], fill=(200, 205, 220))
            gx += step
        gy += step
    for num, (lon, lat) in PINS.items():
        px = x + (lon + 180) / 360 * w
        py = y + (80 - lat) / 140 * h
        d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=RED, outline=CREAM, width=2)
        t = str(num)
        f = F(BOLD, 11)
        d.text((px - d.textlength(t, font=f) / 2, py - 7), t, font=f, fill=CREAM)


def trunc(d, text, font, w):
    if d.textlength(text, font=font) <= w:
        return text
    while len(text) > 4 and d.textlength(text + "…", font=font) > w:
        text = text[:-1]
    return text + "…"


def panel_border(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=PAPER2, outline=TERRA, width=2)
    d.rectangle([x + 3, y + 3, x + w - 3, y + h - 3], outline=GOLD, width=1)


def hero_panel(d, x, y, w, h, s):
    panel_border(d, x, y, w, h)
    scene(d, x + 5, y + 5, 252, h - 10, s["scene"])
    tx = x + 268
    tw = w - 280
    d.text((tx, y + 9), s["kicker"], font=F(BOLD, 15), fill=TERRA)
    f = F(BOLD, 12)
    d.text((x + w - 10 - d.textlength(s["src"], font=f), y + 9),
           s["src"], font=f, fill=MUT)
    y2 = text_block(d, tx, y + 31, s["head"], FLF(SERIFB, 24), tw, 27, INK, max_lines=2)
    text_block(d, tx, y2 + 3, s["dek"], F(SANS, 13), tw, 15, (70, 60, 48), max_lines=2)


def pictured_panel(d, x, y, w, h, s):
    panel_border(d, x, y, w, h)
    scene(d, x + 4, y + 4, w - 8, 70, s["scene"])
    yy = y + 78
    d.text((x + 8, yy), s["kicker"], font=F(BOLD, 13), fill=TERRA)
    f = F(BOLD, 10)
    d.text((x + w - 8 - d.textlength(s["src"], font=f), yy),
           s["src"], font=f, fill=MUT)
    yy = text_block(d, x + 8, yy + 17, s["head"], FLF(SERIFB, 15), w - 16, 18, INK,
                    max_lines=2)
    text_block(d, x + 8, yy + 1, s["dek"], F(SANS, 11), w - 16, 13, (70, 60, 48),
               max_lines=2)


def center_text(d, cx, y, text, font, color):
    w = d.textlength(text, font=font)
    d.text((cx - w / 2, y), text, font=font, fill=color)
    return w


def main():
    im = paper(W, H, PAPER)
    d = ImageDraw.Draw(im)
    d.rectangle([26, 26, W - 26, H - 26], outline=TERRA, width=3)
    d.rectangle([38, 38, W - 38, H - 38], outline=GOLD, width=2)

    # top line
    d.text((48, 54), "ONE DAY OF WORLD NEWS, ONE PICTURE", font=F(BOLD, 20), fill=INK)
    f = F(BOLD, 20)
    t = "48 STORIES · 7 REGIONS"
    d.text((1552 - d.textlength(t, font=f), 54), t, font=f, fill=INK)
    d.line([(48, 84), (1552, 84)], fill=INK, width=2)

    # masthead
    f = FLF(SERIFB, 96)
    center_text(d, 800, 96, "Friday 20 November 2026", f, INK)
    center_text(d, 800, 198,
                "Akvan comes ashore · A missile over Riyadh · Trump puts the Iran "
                "decision off to 2027 · The world answers the genocide verdict",
                FLF(SERIFI, 23), RED)

    # timeline band
    d.rectangle([48, 232, 1552, 300], fill=PAPER2, outline=GOLD, width=1)
    d.text((58, 236), "THE DAY IN UTC", font=F(BOLD, 15), fill=TERRA)
    for i, (tm, txt) in enumerate(TIMELINE):
        col = i % 3
        row = i // 3
        cx = 220 + col * 445
        cy = 238 + row * 30
        d.text((cx, cy), tm, font=F(BOLD, 14), fill=TERRA)
        d.text((cx + 118, cy), txt, font=F(SANS, 14), fill=INK)

    # region strip
    x = 48
    cw = 1520 / 7
    for name, n, col in REGIONS:
        d.rectangle([x, 308, x + cw, 340], fill=col)
        center_text(d, x + cw / 2, 316, "%s %d" % (name, n), F(BOLD, 16), CREAM)
        x += cw

    # heroes stacked on the left
    hy = 352
    for s in HEROES:
        hero_panel(d, 48, hy, 812, 144, s)
        hy += 152

    # briefs column on the right
    d.text((880, 352), "ALSO ON FRIDAY 20 NOVEMBER — 32 MORE STORIES",
           font=F(BOLD, 17), fill=TERRA)
    d.line([(880, 378), (1552, 378)], fill=TERRA, width=2)
    for i, (num, place, txt) in enumerate(BRIEFS):
        col = i // 16
        row = i % 16
        bx = 880 + col * 340
        by = 388 + row * 26
        line = "%d %s — %s" % (num, place, txt)
        f = F(SANS, 13)
        line = trunc(d, line, f, 330)
        d.text((bx, by), line, font=f, fill=INK)

    # pictured grid 4 / 5 / 4
    rows = [PICTURED[0:4], PICTURED[4:9], PICTURED[9:13]]
    py = 812
    for group in rows:
        n = len(group)
        pw = (1520 - (n - 1) * 10) / n
        px = 48
        for s in group:
            pictured_panel(d, px, py, pw, 168, s)
            px += pw + 10
        py += 176

    # map + date check
    d.text((48, 1344), "WHERE IT HAPPENED", font=F(BOLD, 17), fill=TERRA)
    draw_map(d, 48, 1370, 652, 148)
    d.rectangle([720, 1344, 1552, 1518], fill=PAPER2, outline=TERRA, width=2)
    d.rectangle([720, 1344, 1552, 1372], fill=TERRA)
    d.text((730, 1348), "DATE CHECK", font=F(BOLD, 16), fill=CREAM)
    text_block(d, 730, 1382, DATECHECK, F(SANS, 14), 812, 18, INK)

    # footer
    center_text(d, 800, 1530, FOOT1, FLF(SERIFI, 14), MUT)
    center_text(d, 800, 1550, FOOT2, F(SANS, 12), MUT)

    im.resize((1024, 1024), Image.LANCZOS).save("entry.png")


if __name__ == "__main__":
    main()
