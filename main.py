#!/usr/bin/env python3
# main.py - news-image-20261120 entry for wallet w9 ("Warm Postcard" front page).
# Editor's note (w9): the dek under the masthead carries the four biggest stories.
# One image that sums up Friday 20 November 2026: 48 stories, 7 regions.
# Self-contained: running this file writes entry.png (1024x1024).
# Story index (48):
#    1. Akvan comes ashore on the Odisha coast
#    2. Houthi missile hits Riyadh's KAFD financial district
#    3. Trump, Xi and Putin issue a joint declaration
#    4. Crimean Bridge hit a third time this week; rail halted
#    5. APEC leaders meet in Shenzhen
#    6. COP31's final day: fossil fuels cut from the text
#    7. The world answers the genocide verdict
#    8. Anthropic's debut can't stop the slide
#    9. GTA VI passes The Odyssey's $1.84bn
#   10. NASA confirms Voyager 1's light-day milestone
#   11. South Korea clears ex-PM Han
#   12. Fiji declares a national disaster over drought
#   13. North Korea expands uranium enrichment at Yongbyon
#   14. US and Venezuela restore military cooperation
#   15. ADNOC vessel attacked in the Strait of Hormuz
#   16. Day two at the Basin: Nicholls' 113 anchors New Zealand
#   17. BRUSSELS - EU-UK summit opens
#   18. NEW DELHI - Modi meets William and Kate
#   19. DHAKA - Fire at the Yunus home; arson feared
#   20. MUMBAI - Sensex +1.21%, Nifty +1.14% on the day
#   21. TOKYO - Hayabusa2 gives up landing; mission rewritten
#   22. BERLIN - Coalition of the Willing meets in Berlin
#   23. BERLIN - Merz hosts Qatar's emir in Berlin
#   24. NEW DELHI - Pakistan minister leads delegation to Delhi for SCO
#   25. MANILA - Philippines-Chile trade deal signed
#   26. MANILA - Musk plans Philippines projects
#   27. HONG KONG - India beats Malaysia, Asian Hockey Trophy opens
#   28. IPOH - Harimau Shakti exercise opens in Ipoh
#   29. NEW DELHI - India's electronics exports jump 44%
#   30. NEW DELHI - ICMR completes 100 tech transfers
#   31. NEW DELHI - India unveils its first bird-flu vaccine
#   32. GENEVA - World Children's Day marked worldwide
#   33. EUROPE - Youth anti-war protests across Europe
#   34. BRUSSELS - EU delays its methane rules by 24 months
#   35. COLOGNE - Bayern Munich beat Koln 3-0
#   36. U17 CUP - Argentina 0-2 Australia at the U17 Cup
#   37. WASHINGTON - Jobless claims come in at 203,000
#   38. STRASBOURG - NATO's assembly opens its 72nd session
#   39. HANOI - Azerbaijan's Aliyev visits Vietnam
#   40. MARKETS - Crude futures fall over 3%
#   41. KHARTOUM - Sudan army: two-year El Obeid siege broken
#   42. MOGADISHU - Somalia gives UAE ambassador 72 hours to leave
#   43. SAN SALVADOR - Migrant boat capsizes off El Salvador; dozens missing
#   44. PORT-AU-PRINCE - Haiti approves Salvadoran troop deal vs gangs
#   45. ARABIAN SEA - Amur falcons cross the Arabian Sea
#   46. NEW YORK - Al-Saadi appears in a New York court over a UK plot
#   47. KYIV - Witkoff and Kushner brief Zelenskyy
#   48. BEIJING - Xi urges APEC to back open trade, new tech
"""Warm Postcard front page: Friday 20 November 2026 on warm paper - 48 stories, 7 regions, one image generated with Pillow."""
import math, os, random, sys
from PIL import Image, ImageDraw, ImageFont

VARIANT = "c"
SEED = 17
TINT = 1

FD = "/usr/share/fonts/truetype/dejavu/"
FL = "/usr/share/fonts/truetype/liberation/"
def F(name, size): return ImageFont.truetype(FD + name, size)
def FLF(name, size):
    try: return ImageFont.truetype(FL + name, size)
    except Exception: return ImageFont.truetype(FD + name, size)
SANS = "DejaVuSans.ttf"; BOLD = "DejaVuSans-Bold.ttf"; MONO = "DejaVuSansMono.ttf"; MONOB = "DejaVuSansMono-Bold.ttf"
SERIF = "LiberationSerif-Regular.ttf"; SERIFB = "LiberationSerif-Bold.ttf"; SERIFI = "LiberationSerif-Italic.ttf"

def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def fit1(d, text, font, width):
    if d.textlength(text, font=font) <= width: return text
    while text and d.textlength(text + "…", font=font) > width: text = text[:-1]
    return text.rstrip() + "…"

def text_block(d, x, y, text, font, width, lh, fill, max_lines=None):
    lines = wrap(d, text, font, width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and d.textlength(last + "…", font=font) > width: last = last[:-1]
        lines[-1] = last.rstrip() + "…"
    for i, ln in enumerate(lines): d.text((x, y + i * lh), ln, font=font, fill=fill)
    return y + len(lines) * lh

def paper(w, h, base, seed=7, amp=7):
    im = Image.new("RGB", (w, h), base)
    # per-pixel paper grain; rng is local so layouts stay reproducible
    px = im.load(); rng = random.Random(seed)
    for yy in range(h):
        for xx in range(w):
            if rng.random() < 0.30:
                n = rng.randint(-amp, amp)
                r, g, b = px[xx, yy]
                px[xx, yy] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))
    return im

# ---------- peta dunia dot-matrix dari poligon kasar (lon,lat) ----------
NAMER = [(-168,66),(-140,70),(-120,71),(-100,69),(-90,79),(-82,70),(-78,62),(-65,50),(-55,52),(-64,44),(-70,42),(-74,39),(-76,35),(-80,31),(-81,26),(-84,22),(-87,21),(-91,19),(-96,16),(-94,17),(-87,13),(-83,9),(-86,12),(-95,16),(-101,19),(-106,22),(-111,25),(-115,30),(-121,34),(-124,41),(-125,48),(-131,55),(-150,60),(-166,60)]
GRLND = [(-46,60),(-32,68),(-22,70),(-19,76),(-28,82),(-48,81),(-55,73),(-53,64)]
SAMER = [(-79,9),(-72,12),(-63,10),(-55,6),(-50,0),(-44,-3),(-35,-8),(-39,-18),(-46,-26),(-52,-33),(-58,-39),(-62,-41),(-65,-46),(-67,-51),(-68,-54),(-71,-54),(-73,-47),(-73,-37),(-71,-29),(-70,-19),(-75,-15),(-79,-8),(-81,-4),(-80,1),(-77,5)]
EURASIA = [(-9,37),(-9,43),(-2,44),(-9,48),(-5,50),(0,51),(5,53),(8,56),(7,58),(12,56),(18,56),(21,60),(25,60),(28,63),(30,66),(35,65),(45,67),(60,69),(80,70),(105,71),(130,71),(155,71),(178,69),(178,65),(162,61),(156,55),(143,54),(141,50),(137,46),(131,43),(127,40),(122,38),(121,34),(122,30),(118,27),(110,24),(108,19),(106,14),(103,7),(100,9),(98,14),(94,17),(91,22),(88,22),(86,20),(82,16),(80,13),(77,8),(75,13),(72,19),(70,22),(66,25),(61,25),(57,26),(52,27),(50,29),(48,30),(44,29),(43,33),(40,36),(36,36),(33,36),(30,36),(26,38),(22,37),(19,40),(15,38),(12,39),(10,37),(5,37),(2,37),(-2,37)]
AFRICA = [(-6,35),(3,37),(10,37),(20,32),(30,31),(33,30),(35,28),(38,23),(40,19),(43,12),(48,11),(51,11),(47,4),(41,-4),(40,-14),(37,-21),(35,-27),(31,-29),(27,-34),(20,-35),(17,-32),(15,-26),(13,-19),(12,-13),(13,-8),(9,-3),(9,3),(3,6),(-4,5),(-9,5),(-14,8),(-17,13),(-17,16),(-16,21),(-15,26),(-13,29),(-10,32)]
AUS = [(113,-22),(114,-29),(115,-34),(119,-35),(124,-33),(130,-32),(133,-32),(135,-35),(137,-35),(139,-37),(142,-38),(146,-38),(149,-37),(150,-36),(153,-31),(153,-26),(150,-22),(146,-19),(143,-15),(142,-11),(140,-13),(136,-12),(135,-15),(132,-11),(129,-13),(125,-14),(122,-17),(118,-20)]
BLOBS = [(-2.5,53.5,3.2,3.0),(138,37.5,4.5,3.2),(107,-6.5,9.0,2.6),(119,-2.0,5.0,3.2),(122,13.5,2.6,3.6),(172,-41.5,2.6,2.2),(47,-19.0,2.2,4.2),(103,1.5,3.0,2.0)]
def _inpoly(x, y, poly):
    inside = False; j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]; xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi): inside = not inside
        j = i
    return inside
def is_land(lon, lat):
    for c in (NAMER, GRLND, SAMER, EURASIA, AFRICA, AUS):
        if _inpoly(lon, lat, c): return True
    for cx, cy, rx, ry in BLOBS:
        if ((lon - cx) / rx) ** 2 + ((lat - cy) / ry) ** 2 <= 1: return True
    return False

def draw_map(d, x, y, w, h, dot, land, sea=None, r=2):
    if sea: d.rectangle([x, y, x + w, y + h], fill=sea)
    cols = int(w / (r * 2 + 2)); rows = int(h / (r * 2 + 2))
    for i in range(cols):
        lon = -180 + 360 * (i + 0.5) / cols
        for j in range(rows):
            lat = 84 - 148 * (j + 0.5) / rows
            if is_land(lon, lat):
                cx = x + (i + 0.5) * w / cols; cy = y + (j + 0.5) * h / rows
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=land)
    return (x, y, w, h)

def pin_xy(box, fx, fy):
    x, y, w, h = box; return (x + fx * w, y + fy * h)

# ---------- ikon adegan (kotak x,y,w,h) ----------
def _sun(d, cx, cy, r, col):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
def scene(d, idx, x, y, w, h, pal):
    """Gambar adegan datar sederhana per indeks PICTURED (0..11) / hero (100,101)."""
    bg, ac, ac2, dk = pal
    d.rectangle([x, y, x + w, y + h], fill=bg)
    cx, cy = x + w / 2, y + h / 2
    if idx == 100:  # summit: skyline + 3 bendera
        for i, bx in enumerate(range(int(x + w * 0.08), int(x + w * 0.95), max(18, w // 16))):
            bh = h * (0.25 + 0.3 * ((i * 37) % 10) / 10)
            d.rectangle([bx, y + h - bh, bx + max(10, w // 22), y + h], fill=dk)
        _sun(d, x + w * 0.82, y + h * 0.26, h * 0.13, ac2)
        for i, c in enumerate([(178, 34, 52), (222, 41, 16), (33, 71, 160)]):
            fx = x + w * (0.24 + 0.22 * i)
            d.line([fx, y + h * 0.14, fx, y + h * 0.62], fill=(240, 240, 235), width=3)
            d.polygon([(fx, y + h * 0.14), (fx + w * 0.13, y + h * 0.22), (fx, y + h * 0.32)], fill=c)
    elif idx == 101:  # GTA: sunset + palma + skyline
        for i in range(12):
            t = i / 12; col = tuple(int(ac[k] + (ac2[k] - ac[k]) * t) for k in range(3))
            d.rectangle([x, y + h * t, x + w, y + h * (t + 1 / 12) + 1], fill=col)
        _sun(d, cx, y + h * 0.62, h * 0.20, (255, 214, 120))
        for i, bx in enumerate(range(int(x + 4), int(x + w - 8), max(16, w // 14))):
            bh = h * (0.2 + 0.35 * ((i * 53) % 10) / 10)
            d.rectangle([bx, y + h - bh, bx + max(9, w // 24), y + h], fill=(16, 14, 34))
        for px_ in (x + w * 0.16, x + w * 0.84):
            d.line([px_, y + h, px_, y + h * 0.42], fill=(10, 26, 18), width=4)
            for a in range(6):
                ang = math.pi * (0.08 + 0.16 * a)
                d.arc([px_ - w * 0.09, y + h * 0.30, px_ + w * 0.09, y + h * 0.54], start=180 + a * 28, end=205 + a * 28, fill=(10, 40, 22), width=3)
    elif idx == 0:  # ICJ: kolom + palu
        for i in range(4):
            fx = x + w * (0.18 + 0.17 * i)
            d.rectangle([fx, y + h * 0.30, fx + w * 0.07, y + h * 0.82], fill=ac2)
        d.polygon([(x + w * 0.10, y + h * 0.28), (x + w * 0.90, y + h * 0.28), (cx, y + h * 0.10)], fill=ac2)
        d.rectangle([x + w * 0.10, y + h * 0.82, x + w * 0.90, y + h * 0.88], fill=ac2)
        d.line([x + w * 0.60, y + h * 0.60, x + w * 0.84, y + h * 0.38], fill=dk, width=5)
        d.rectangle([x + w * 0.80, y + h * 0.28, x + w * 0.94, y + h * 0.40], fill=dk)
    elif idx == 1:  # IPO: grafik naik + lonceng
        pts = [(x + w * 0.08, y + h * 0.80), (x + w * 0.30, y + h * 0.62), (x + w * 0.46, y + h * 0.70), (x + w * 0.66, y + h * 0.40), (x + w * 0.90, y + h * 0.18)]
        d.line(pts, fill=ac2, width=5)
        d.polygon([(x + w * 0.90, y + h * 0.18), (x + w * 0.78, y + h * 0.20), (x + w * 0.87, y + h * 0.32)], fill=ac2)
        d.arc([x + w * 0.36, y + h * 0.52, x + w * 0.62, y + h * 0.92], start=180, end=360, fill=dk, width=4)
        d.rectangle([x + w * 0.47, y + h * 0.70, x + w * 0.51, y + h * 0.78], fill=dk)
    elif idx == 2:  # jembatan + ledakan
        d.arc([x - w * 0.1, y + h * 0.30, x + w * 1.1, y + h * 1.15], start=180, end=360, fill=ac2, width=5)
        for i in range(5):
            fx = x + w * (0.12 + 0.19 * i)
            d.line([fx, y + h * (0.52 - 0.10 * abs(i - 2)), fx, y + h * 0.92], fill=ac2, width=3)
        d.rectangle([x, y + h * 0.90, x + w, y + h], fill=(38, 74, 110))
        sx, sy = x + w * 0.52, y + h * 0.30
        for a in range(8):
            ang = math.radians(a * 45)
            d.line([sx, sy, sx + math.cos(ang) * w * 0.10, sy + math.sin(ang) * w * 0.10], fill=(255, 166, 0), width=4)
        _sun(d, sx, sy, w * 0.045, (255, 120, 40))
    elif idx == 3:  # COP31: globe + daun
        _sun(d, cx, cy, h * 0.34, (64, 145, 200))
        d.arc([cx - h * 0.34, cy - h * 0.34, cx + h * 0.34, cy + h * 0.34], start=0, end=360, fill=(30, 90, 60), width=3)
        d.ellipse([cx - h * 0.16, cy - h * 0.20, cx + h * 0.05, cy - h * 0.02], fill=(52, 168, 83))
        d.ellipse([cx - h * 0.02, cy + h * 0.04, cx + h * 0.20, cy + h * 0.22], fill=(52, 168, 83))
        d.polygon([(cx + h * 0.10, cy - h * 0.30), (cx + h * 0.30, cy - h * 0.34), (cx + h * 0.16, cy - h * 0.12)], fill=(52, 168, 83))
    elif idx == 4:  # EU: lingkaran bintang + euro
        for i in range(12):
            ang = math.radians(i * 30 - 90)
            sx, sy = cx + math.cos(ang) * h * 0.33, cy + math.sin(ang) * h * 0.33
            d.polygon([(sx, sy - 4), (sx + 4, sy + 3), (sx - 4, sy + 3)], fill=(255, 204, 0))
        d.text((cx, cy), "€", font=F(BOLD, int(h * 0.52)), anchor="mm", fill=(255, 255, 255))
    elif idx == 5:  # Van Gogh: bingkai + pusaran
        d.rectangle([x + w * 0.10, y + h * 0.08, x + w * 0.90, y + h * 0.92], outline=(146, 106, 32), width=6)
        for i, rr in enumerate(range(int(h * 0.30), 6, -7)):
            d.arc([cx - rr, cy - rr * 0.7, cx + rr, cy + rr * 0.7], start=i * 40, end=i * 40 + 200, fill=(240, 200, 60) if i % 2 else (90, 120, 200), width=3)
        _sun(d, x + w * 0.26, y + h * 0.26, 5, (255, 240, 180))
    elif idx == 6:  # Voyager: piringan + sinyal
        d.arc([x + w * 0.16, y + h * 0.22, x + w * 0.52, y + h * 0.78], start=300, end=120, fill=ac2, width=5)
        d.line([x + w * 0.34, y + h * 0.50, x + w * 0.62, y + h * 0.24], fill=ac2, width=3)
        for i, rr in enumerate((0.10, 0.17, 0.24)):
            d.arc([x + w * (0.62 - rr), y + h * (0.24 - rr), x + w * (0.62 + rr), y + h * (0.24 + rr)], start=300, end=60, fill=(140, 200, 255), width=3)
        rnd = random.Random(6)
        for _ in range(26):
            sx, sy = x + rnd.random() * w, y + rnd.random() * h
            d.point((sx, sy), fill=(230, 238, 255))
    elif idx == 7:  # Gaza: skyline + matahari + merpati sederhana
        _sun(d, x + w * 0.78, y + h * 0.30, h * 0.14, (245, 197, 66))
        for i, bx in enumerate(range(int(x + 4), int(x + w - 10), max(14, w // 12))):
            bh = h * (0.25 + 0.3 * ((i * 41) % 9) / 9)
            d.rectangle([bx, y + h - bh, bx + max(8, w // 20), y + h], fill=dk)
        d.arc([x + w * 0.30, y + h * 0.18, x + w * 0.52, y + h * 0.40], start=200, end=330, fill=(250, 250, 250), width=3)
        d.arc([x + w * 0.40, y + h * 0.14, x + w * 0.58, y + h * 0.34], start=200, end=330, fill=(250, 250, 250), width=3)
    elif idx == 8:  # Hormuz: kapal tanker di selat
        d.polygon([(x, y + h * 0.30), (x + w * 0.30, y + h * 0.30), (x + w * 0.22, y + h * 0.55), (x, y + h * 0.62)], fill=(150, 120, 84))
        d.polygon([(x + w, y + h * 0.34), (x + w * 0.72, y + h * 0.34), (x + w * 0.80, y + h * 0.58), (x + w, y + h * 0.66)], fill=(150, 120, 84))
        d.rectangle([x, y + h * 0.60, x + w, y + h], fill=(36, 84, 124))
        d.polygon([(x + w * 0.36, y + h * 0.62), (x + w * 0.68, y + h * 0.62), (x + w * 0.62, y + h * 0.74), (x + w * 0.42, y + h * 0.74)], fill=(30, 30, 30))
        d.rectangle([x + w * 0.44, y + h * 0.50, x + w * 0.60, y + h * 0.62], fill=(178, 44, 44))
    elif idx == 9:  # Bangladesh: bendera + kerumunan
        d.rectangle([x + w * 0.08, y + h * 0.10, x + w * 0.62, y + h * 0.52], fill=(0, 106, 78))
        _sun(d, x + w * 0.33, y + h * 0.31, h * 0.11, (244, 42, 65))
        for i in range(7):
            hx = x + w * (0.10 + 0.12 * i); hy = y + h * (0.70 + 0.10 * (i % 2))
            _sun(d, hx, hy, 6, dk)
            d.rectangle([hx - 6, hy + 6, hx + 6, y + h * 0.98], fill=dk)
    elif idx == 10:  # kapal kontainer
        d.rectangle([x, y + h * 0.66, x + w, y + h], fill=(30, 70, 110))
        d.polygon([(x + w * 0.08, y + h * 0.66), (x + w * 0.94, y + h * 0.66), (x + w * 0.86, y + h * 0.80), (x + w * 0.16, y + h * 0.80)], fill=(40, 40, 40))
        cols = [(178, 44, 44), (44, 110, 178), (44, 150, 84), (220, 150, 40)]
        for r_ in range(2):
            for c_ in range(4):
                d.rectangle([x + w * (0.16 + 0.17 * c_), y + h * (0.34 + 0.15 * r_), x + w * (0.31 + 0.17 * c_), y + h * (0.47 + 0.15 * r_)], fill=cols[(r_ + c_) % 4])
        d.rectangle([x + w * 0.80, y + h * 0.16, x + w * 0.86, y + h * 0.34], fill=(230, 230, 230))
    elif idx == 11:  # bank / Fed
        d.polygon([(x + w * 0.08, y + h * 0.26), (x + w * 0.92, y + h * 0.26), (cx, y + h * 0.06)], fill=ac2)
        for i in range(4):
            fx = x + w * (0.16 + 0.19 * i)
            d.rectangle([fx, y + h * 0.34, fx + w * 0.08, y + h * 0.78], fill=ac2)
        d.rectangle([x + w * 0.08, y + h * 0.82, x + w * 0.92, y + h * 0.90], fill=ac2)
        d.text((x + w * 0.86, y + h * 0.16), "%", font=F(BOLD, int(h * 0.30)), anchor="mm", fill=dk)
    else:  # generik: pin lokasi
        _sun(d, cx, cy - h * 0.08, h * 0.16, ac2)
        d.polygon([(cx - h * 0.10, cy + h * 0.02), (cx + h * 0.10, cy + h * 0.02), (cx, cy + h * 0.30)], fill=ac2)

# Dataset NI20 — Jumat 20 Nov 2026. Sumber: bedah artifact Top-20 leaderboard
# news-image-20261120 (pull 20 Nov ±10:05 WIB, run-20261120-1020/top20/) —
# story dikorroborasi silang lintas artifact independen r01 + r10 + judul
# Top-25. Kerangka pemenang: masthead tanggal serif raksasa, hero beradegan,
# panel bergambar + dek, peta + pin, brief telegrafis, DATE CHECK, footer
# kredibilitas. Angka kunci: Akvan 300.000 dievakuasi / 423 tim / 11 distrik;
# GTA VI $1,84bn hari pertama (Sensor Tower); Dow -1.084; Voyager 16bn mil.
# region: EUR, AME, ASP, MID, AFR, OCE, WLD
DATE_LONG = "Friday 20 November 2026"
DEK = "Akvan comes ashore · A missile over Riyadh · Trump puts the Iran decision off to 2027 · The world answers the genocide verdict"

HEROES = [
    ("ASP", "1 · ODISHA · STORM", "Akvan comes ashore on the Odisha coast",
     "Cyclone Akvan crossed the coast near Gopalpur at noon, winds 90-100 km/h gusting to 110. Three hundred thousand people are out of harm's way, 423 rescue teams deployed, red alerts in 11 districts.", "IMD · The Hindu", "storm"),
    ("MID", "2 · RIYADH · ATTACK", "Houthi missile hits Riyadh's KAFD financial district",
     "A Houthi missile damaged a wealth-fund tower in the financial district, one of Riyadh's tallest. No casualties are reported, as air defences answered the strike.", "Arab News · Reuters", "missile"),
    ("ASP", "3 · SHENZHEN · DIPLOMACY", "Trump, Xi and Putin issue a joint declaration",
     "No big peace deal from the trilateral's second day. Trump says the Iran war call waits until 2027, rates the summit '12 out of 10', and Putin may attend December's G20 in Miami.", "Reuters · AP", "summit"),
]

# (region, kicker, headline, dek, source, scene_key, pin_fx, pin_fy atau None)
PICTURED = [
    ("EUR", "4 · KERCH STRAIT · WAR", "Crimean Bridge hit a third time this week; rail halted",
     "A Ukrainian naval drone strike disrupted rail traffic on the bridge. Rail partly resumes; Putin vows retaliation, and Kyiv was hit by drones.", "CLAIM · Kyiv", "bridge", 0.594, 0.264),
    ("ASP", "5 · SHENZHEN · SUMMIT", "APEC leaders meet in Shenzhen",
     "Leaders gather in China for the APEC summit. Xi urges APEC economies to back open trade and new technology.", "AP", "apec", 0.825, 0.430),
    ("EUR", "6 · ANTALYA · CLIMATE", "COP31's final day: fossil fuels cut from the text",
     "A revised draft strips out every fossil-fuel phase-out pledge. Delegates push back as the final plenary meets today.", "UNFCCC · AFP", "cop", 0.585, 0.318),
    ("EUR", "7 · THE HAGUE · LAW", "The world answers the genocide verdict",
     "Britain expels Myanmar's defence attache and seeks an urgent Security Council meeting. The Gambia hails a 'historic' verdict.", "AP · BBC", "court", 0.513, 0.216),
    ("AME", "8 · NEW YORK · MARKETS", "Anthropic's debut can't stop the slide",
     "The Dow fell 1,084 points, the S&P 2.02% and the Nasdaq 2.25%, as the AI selloff bit a day after Anthropic's record debut.", "Bloomberg", "chart", 0.285, 0.278),
    ("AME", "9 · VICE CITY · GAMES", "GTA VI passes The Odyssey's $1.84bn",
     "Launch-day sales top The Odyssey's $1.80bn global run, Sensor Tower estimates. Reviews land; Rockstar calls it the highest-rated game ever.", "Sensor Tower", "game", 0.278, 0.385),
    ("WLD", "10 · SPACE · SCIENCE", "NASA confirms Voyager 1's light-day milestone",
     "The probe is now a full light-day from Earth - 16 billion miles out, the farthest any human-made object has ever travelled.", "NASA · JPL", "voyager", None, None),
    ("ASP", "11 · SEOUL · LAW", "South Korea clears ex-PM Han",
     "The Supreme Court overturns former prime minister Han Duck-soo's conviction, in the case tied to the 2024 martial-law declaration.", "Korea Times", "gavel", 0.853, 0.314),
    ("OCE", "12 · SUVA · CLIMATE", "Fiji declares a national disaster over drought",
     "Fiji declares a national disaster over drought and water shortages. El Nino leaves water short across the islands.", "AFP", "drought", 0.905, 0.560),
    ("ASP", "13 · VIENNA · SECURITY", "North Korea expands uranium enrichment at Yongbyon",
     "The UN watchdog reports growth at the nuclear site, in its latest assessment of the Yongbyon complex.", "IAEA", "atom", 0.845, 0.300),
    ("AME", "14 · CARACAS · DIPLOMACY", "US and Venezuela restore military cooperation",
     "The two countries sign an agreement to work together again, restoring a military channel closed for years.", "Reuters", "hands", 0.300, 0.520),
    ("MID", "15 · HORMUZ · CONFLICT", "ADNOC vessel attacked in the Strait of Hormuz",
     "One crew member is missing after the strike on the ADNOC vessel in the strait.", "Reuters", "ship", 0.619, 0.453),
    ("OCE", "16 · WELLINGTON · CRICKET", "Day two at the Basin: Nicholls' 113 anchors New Zealand",
     "New Zealand build on Henry Nicholls' unbeaten 113 as India hunt early wickets, in the first Test at the Basin Reserve.", "AP", "cricket", 0.885, 0.640),
]

# (region, CITY, telegrafis satu baris)
BRIEFS = [
    ("EUR", "BRUSSELS", "EU-UK summit opens"),
    ("ASP", "NEW DELHI", "Modi meets William and Kate"),
    ("ASP", "DHAKA", "Fire at the Yunus home; arson feared"),
    ("ASP", "MUMBAI", "Sensex +1.21%, Nifty +1.14% on the day"),
    ("ASP", "TOKYO", "Hayabusa2 gives up landing; mission rewritten"),
    ("EUR", "BERLIN", "Coalition of the Willing meets in Berlin"),
    ("EUR", "BERLIN", "Merz hosts Qatar's emir in Berlin"),
    ("ASP", "NEW DELHI", "Pakistan minister leads delegation to Delhi for SCO"),
    ("ASP", "MANILA", "Philippines-Chile trade deal signed"),
    ("ASP", "MANILA", "Musk plans Philippines projects"),
    ("ASP", "HONG KONG", "India beats Malaysia, Asian Hockey Trophy opens"),
    ("ASP", "IPOH", "Harimau Shakti exercise opens in Ipoh"),
    ("ASP", "NEW DELHI", "India's electronics exports jump 44%"),
    ("ASP", "NEW DELHI", "ICMR completes 100 tech transfers"),
    ("ASP", "NEW DELHI", "India unveils its first bird-flu vaccine"),
    ("WLD", "GENEVA", "World Children's Day marked worldwide"),
    ("EUR", "EUROPE", "Youth anti-war protests across Europe"),
    ("EUR", "BRUSSELS", "EU delays its methane rules by 24 months"),
    ("EUR", "COLOGNE", "Bayern Munich beat Koln 3-0"),
    ("WLD", "U17 CUP", "Argentina 0-2 Australia at the U17 Cup"),
    ("AME", "WASHINGTON", "Jobless claims come in at 203,000"),
    ("EUR", "STRASBOURG", "NATO's assembly opens its 72nd session"),
    ("ASP", "HANOI", "Azerbaijan's Aliyev visits Vietnam"),
    ("MID", "MARKETS", "Crude futures fall over 3%"),
    ("AFR", "KHARTOUM", "Sudan army: two-year El Obeid siege broken"),
    ("AFR", "MOGADISHU", "Somalia gives UAE ambassador 72 hours to leave"),
    ("AME", "SAN SALVADOR", "Migrant boat capsizes off El Salvador; dozens missing"),
    ("AME", "PORT-AU-PRINCE", "Haiti approves Salvadoran troop deal vs gangs"),
    ("WLD", "ARABIAN SEA", "Amur falcons cross the Arabian Sea"),
    ("AME", "NEW YORK", "Al-Saadi appears in a New York court over a UK plot"),
    ("EUR", "KYIV", "Witkoff and Kushner brief Zelenskyy"),
    ("ASP", "BEIJING", "Xi urges APEC to back open trade, new tech"),
]

FIGURES = [
    ("300,000", "people evacuated ahead of Cyclone Akvan"),
    ("$1.84bn", "GTA VI's first-day sales, Sensor Tower estimates"),
    ("-1,084", "points the Dow lost in Friday's slide"),
    ("16bn miles", "Voyager 1 from Earth - one light-day out"),
    ("7.91m", "peak viewers watching GTA VI at once"),
    ("9-6", "the ICJ vote finding Myanmar guilty"),
]

DATE_CHECK = ("the ICJ genocide ruling on Myanmar itself (Thursday 19 Nov) - Friday's news is the world's answer to it - "
              "Denmark's Greenland-US pact (19 Nov) - Anthropic's $81.34bn IPO (19 Nov); its first trading day was Thursday - "
              "Germany's electricity-tax cut (18 Nov) - the Crimean Bridge span collapse (17-18 Nov). "
              "Not yet: the trilateral's first meeting was 19 Nov; the joint declaration is Friday's.")

FOOTER1 = "Every story here happened, or was first reported, on Friday 20 November 2026, in some time zone. Disputed claims are attributed, not stated as fact."
FOOTER2 = "Sources: Reuters - AP - AFP - BBC - Bloomberg - IMD - NASA - IAEA - The Hindu - Arab News - Sensor Tower. Original drawings, drawn for this page."

REGION_NAMES = {"EUR": "EUROPE", "AME": "THE AMERICAS", "ASP": "ASIA-PACIFIC", "MID": "MIDEAST",
                "AFR": "AFRICA", "OCE": "OCEANIA", "WLD": "WORLD"}
REGION_ORDER = ["EUR", "AME", "ASP", "MID", "AFR", "OCE"]
REGION_COLORS = {"EUR": (38, 84, 150), "AME": (46, 140, 80), "ASP": (178, 44, 44), "MID": (196, 132, 36),
                 "AFR": (122, 82, 160), "OCE": (36, 148, 168), "WLD": (96, 96, 96)}


import types as _types
D = _types.SimpleNamespace(**{k: globals()[k] for k in list(globals()) if k.isupper()})

W = H = 1600
INK = (26, 24, 20); GREY = (96, 92, 84)

def grad(d, x, y, w, h, top, bot, steps=14):
    for i in range(steps):
        t = i / steps
        col = tuple(int(top[k] + (bot[k] - top[k]) * t) for k in range(3))
        d.rectangle([x, y + h * t, x + w, y + h * (t + 1 / steps) + 1], fill=col)

def skyline(d, x, y, w, h, col, seed, base=0.55):
    rnd = random.Random(seed)
    bx = x + 2
    while bx < x + w - 8:
        bw = rnd.randint(max(8, w // 26), max(12, w // 13))
        bh = h * (base - 0.3 + 0.55 * rnd.random())
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=col)
        bx += bw + rnd.randint(1, 4)

def flag_us(d, x, y, w, h):
    for i in range(5):
        d.rectangle([x, y + h * i / 5, x + w, y + h * (i + 1) / 5], fill=(178, 34, 52) if i % 2 == 0 else (240, 238, 232))
    d.rectangle([x, y, x + w * 0.45, y + h * 0.6], fill=(33, 71, 160))

def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.ellipse([x + w * 0.10, y + h * 0.14, x + w * 0.30, y + h * 0.40], fill=(255, 222, 0))

def flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(240, 238, 232))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(33, 71, 160))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(200, 40, 40))

def sun(d, cx, cy, r, col=(250, 214, 110)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)

def scene(d, key, x, y, w, h, seed=3):
    cx, cy = x + w / 2, y + h / 2
    if key == "storm":
        grad(d, x, y, w, h, (24, 52, 66), (70, 110, 120))
        for i in range(3):
            r = h * (0.30 - i * 0.08)
            d.arc([cx - r, cy - r * 0.7 - h * 0.12, cx + r, cy + r * 0.7 - h * 0.12], start=20 + i * 40, end=300 + i * 30, fill=(220, 235, 240), width=5)
        rnd = random.Random(seed)
        for _ in range(26):
            sx = x + rnd.random() * w; sy = y + rnd.random() * h * 0.7
            d.line([sx, sy, sx - 5, sy + 12], fill=(170, 205, 220), width=2)
        for i in range(4):
            d.arc([x - w * 0.1 + i * w * 0.28, y + h * 0.78, x + w * 0.25 + i * w * 0.28, y + h * 1.02], start=180, end=360, fill=(200, 225, 235), width=4)
        d.rectangle([x, y + h * 0.92, x + w, y + h], fill=(16, 40, 54))
    elif key == "missile":
        grad(d, x, y, w, h, (14, 18, 38), (52, 44, 66))
        skyline(d, x, y + h * 0.30, w, h * 0.70, (10, 12, 24), seed, base=0.7)
        pts = [(x + w * 0.06, y + h * 0.16), (x + w * 0.34, y + h * 0.30), (x + w * 0.58, y + h * 0.52), (x + w * 0.76, y + h * 0.72)]
        d.line(pts, fill=(255, 170, 60), width=4)
        sx, sy = pts[-1]
        for a in range(10):
            ang = math.radians(a * 36)
            d.line([sx, sy, sx + math.cos(ang) * w * 0.07, sy + math.sin(ang) * w * 0.07], fill=(255, 120, 40), width=4)
        sun(d, sx, sy, w * 0.03, (255, 90, 30))
        rnd = random.Random(seed + 1)
        for _ in range(20):
            d.point((x + rnd.random() * w, y + rnd.random() * h * 0.5), fill=(220, 225, 245))
    elif key == "summit":
        grad(d, x, y, w, h, (70, 100, 150), (214, 196, 160))
        sun(d, x + w * 0.84, y + h * 0.24, h * 0.11)
        skyline(d, x, y + h * 0.18, w, h * 0.82, (44, 56, 84), seed)
        for i, fl in enumerate((flag_us, flag_cn, flag_ru)):
            fx = x + w * (0.20 + 0.26 * i)
            d.line([fx, y + h * 0.16, fx, y + h * 0.78], fill=(235, 232, 225), width=3)
            fl(d, fx + 2, y + h * 0.16, w * 0.15, h * 0.20)
        d.rectangle([x, y + h * 0.86, x + w, y + h], fill=(30, 34, 48))
    elif key == "bridge":
        grad(d, x, y, w, h, (96, 120, 150), (170, 190, 205))
        d.arc([x - w * 0.08, y + h * 0.22, x + w * 1.08, y + h * 1.05], start=180, end=360, fill=(40, 44, 52), width=6)
        for i in range(5):
            fx = x + w * (0.12 + 0.19 * i)
            d.line([fx, y + h * (0.55 - 0.10 * abs(i - 2)), fx, y + h * 0.86], fill=(40, 44, 52), width=3)
        d.rectangle([x, y + h * 0.86, x + w, y + h], fill=(38, 74, 110))
        sx, sy = x + w * 0.55, y + h * 0.34
        for a in range(8):
            ang = math.radians(a * 45)
            d.line([sx, sy, sx + math.cos(ang) * w * 0.09, sy + math.sin(ang) * w * 0.09], fill=(255, 166, 0), width=4)
        sun(d, sx, sy, w * 0.04, (255, 120, 40))
    elif key == "apec":
        grad(d, x, y, w, h, (60, 96, 140), (200, 210, 200))
        sun(d, x + w * 0.16, y + h * 0.26, h * 0.12, (255, 226, 130))
        skyline(d, x, y + h * 0.22, w, h * 0.78, (40, 58, 82), seed)
        for i, c in enumerate([(222, 41, 16), (33, 71, 160), (46, 140, 80), (255, 200, 40), (150, 60, 160)]):
            fx = x + w * (0.14 + 0.17 * i)
            d.line([fx, y + h * 0.30, fx, y + h * 0.66], fill=(240, 238, 230), width=2)
            d.polygon([(fx, y + h * 0.30), (fx + w * 0.10, y + h * 0.37), (fx, y + h * 0.44)], fill=c)
    elif key == "cop":
        grad(d, x, y, w, h, (30, 80, 110), (90, 160, 140))
        sun(d, cx, cy, h * 0.32, (64, 145, 200))
        d.ellipse([cx - h * 0.16, cy - h * 0.20, cx + h * 0.05, cy - h * 0.02], fill=(52, 168, 83))
        d.ellipse([cx - h * 0.02, cy + h * 0.04, cx + h * 0.20, cy + h * 0.22], fill=(52, 168, 83))
        d.polygon([(cx + h * 0.08, cy - h * 0.30), (cx + h * 0.28, cy - h * 0.34), (cx + h * 0.14, cy - h * 0.12)], fill=(52, 168, 83))
    elif key == "court":
        grad(d, x, y, w, h, (120, 116, 104), (196, 188, 168))
        for i in range(4):
            fx = x + w * (0.18 + 0.17 * i)
            d.rectangle([fx, y + h * 0.32, fx + w * 0.07, y + h * 0.82], fill=(238, 234, 224))
        d.polygon([(x + w * 0.10, y + h * 0.30), (x + w * 0.90, y + h * 0.30), (cx, y + h * 0.10)], fill=(238, 234, 224))
        d.rectangle([x + w * 0.10, y + h * 0.82, x + w * 0.90, y + h * 0.88], fill=(238, 234, 224))
        d.line([x + w * 0.58, y + h * 0.62, x + w * 0.84, y + h * 0.40], fill=(40, 36, 30), width=5)
        d.rectangle([x + w * 0.80, y + h * 0.30, x + w * 0.94, y + h * 0.42], fill=(40, 36, 30))
    elif key == "chart":
        grad(d, x, y, w, h, (250, 248, 244), (232, 226, 218))
        for i, bh in enumerate((0.30, 0.42, 0.36, 0.55, 0.48, 0.66, 0.60)):
            bx = x + w * (0.06 + 0.13 * i)
            d.rectangle([bx, y + h * (1 - bh) - h * 0.08, bx + w * 0.08, y + h * 0.92], fill=(190, 190, 186))
        pts = [(x + w * 0.06, y + h * 0.18), (x + w * 0.28, y + h * 0.30), (x + w * 0.44, y + h * 0.26), (x + w * 0.64, y + h * 0.52), (x + w * 0.90, y + h * 0.74)]
        d.line(pts, fill=(178, 32, 40), width=6)
        d.polygon([(x + w * 0.90, y + h * 0.74), (x + w * 0.78, y + h * 0.70), (x + w * 0.86, y + h * 0.58)], fill=(178, 32, 40))
    elif key == "game":
        grad(d, x, y, w, h, (120, 40, 130), (255, 138, 76))
        sun(d, cx, y + h * 0.52, h * 0.20, (255, 208, 110))
        skyline(d, x, y + h * 0.10, w, h * 0.90, (18, 14, 36), seed)
        for px_ in (x + w * 0.13, x + w * 0.87):
            d.line([px_, y + h, px_, y + h * 0.40], fill=(8, 24, 14), width=4)
            for a in range(6):
                ang = math.radians(195 + a * 26)
                d.line([px_, y + h * 0.40, px_ + math.cos(ang) * w * 0.075, y + h * 0.40 + math.sin(ang) * w * 0.075], fill=(8, 40, 20), width=3)
    elif key == "voyager":
        d.rectangle([x, y, x + w, y + h], fill=(8, 10, 26))
        rnd = random.Random(seed + 7)
        for _ in range(40):
            d.point((x + rnd.random() * w, y + rnd.random() * h), fill=(225, 232, 250))
        d.arc([x + w * 0.14, y + h * 0.20, x + w * 0.52, y + h * 0.80], start=300, end=120, fill=(210, 214, 220), width=5)
        d.line([x + w * 0.33, y + h * 0.50, x + w * 0.62, y + h * 0.24], fill=(210, 214, 220), width=3)
        for rr in (0.10, 0.17, 0.24):
            d.arc([x + w * (0.62 - rr), y + h * (0.24 - rr), x + w * (0.62 + rr), y + h * (0.24 + rr)], start=300, end=60, fill=(140, 200, 255), width=3)
    elif key == "gavel":
        grad(d, x, y, w, h, (104, 84, 60), (168, 148, 116))
        d.line([x + w * 0.30, y + h * 0.66, x + w * 0.66, y + h * 0.30], fill=(52, 38, 22), width=8)
        d.rectangle([x + w * 0.58, y + h * 0.16, x + w * 0.80, y + h * 0.32], fill=(52, 38, 22))
        d.rectangle([x + w * 0.18, y + h * 0.78, x + w * 0.62, y + h * 0.86], fill=(52, 38, 22))
    elif key == "drought":
        grad(d, x, y, w, h, (240, 200, 120), (214, 164, 96))
        sun(d, x + w * 0.80, y + h * 0.24, h * 0.14, (255, 240, 170))
        d.ellipse([x + w * 0.16, y + h * 0.52, x + w * 0.84, y + h * 0.94], fill=(186, 138, 84))
        rnd = random.Random(seed + 3)
        for _ in range(12):
            sx = x + w * (0.24 + rnd.random() * 0.5); sy = y + h * (0.58 + rnd.random() * 0.28)
            d.line([sx, sy, sx + rnd.randint(-30, 30), sy + rnd.randint(4, 16)], fill=(120, 86, 48), width=2)
    elif key == "atom":
        grad(d, x, y, w, h, (16, 22, 44), (36, 52, 88))
        sun(d, cx, cy, h * 0.10, (255, 120, 90))
        for ang in (0, 60, 120):
            bbox = [cx - w * 0.34, cy - h * 0.17, cx + w * 0.34, cy + h * 0.17]
            d.arc(bbox, start=ang, end=ang + 330, fill=(150, 200, 255), width=3)
        sun(d, x + w * 0.22, y + h * 0.24, 4, (200, 230, 255)); sun(d, x + w * 0.78, y + h * 0.72, 4, (200, 230, 255))
    elif key == "hands":
        grad(d, x, y, w, h, (36, 66, 120), (90, 130, 170))
        flag_us(d, x + w * 0.10, y + h * 0.20, w * 0.32, h * 0.30)
        d.rectangle([x + w * 0.58, y + h * 0.20, x + w * 0.90, y + h * 0.50], fill=(252, 209, 22))
        d.rectangle([x + w * 0.58, y + h * 0.30, x + w * 0.90, y + h * 0.40], fill=(0, 56, 147))
        d.rectangle([x + w * 0.58, y + h * 0.40, x + w * 0.90, y + h * 0.50], fill=(206, 17, 38))
        d.arc([x + w * 0.36, y + h * 0.52, x + w * 0.64, y + h * 0.86], start=0, end=180, fill=(240, 240, 235), width=4)
    elif key == "ship":
        grad(d, x, y, w, h, (70, 100, 128), (120, 150, 160))
        d.polygon([(x, y + h * 0.26), (x + w * 0.30, y + h * 0.26), (x + w * 0.22, y + h * 0.52), (x, y + h * 0.60)], fill=(150, 120, 84))
        d.polygon([(x + w, y + h * 0.30), (x + w * 0.72, y + h * 0.30), (x + w * 0.80, y + h * 0.56), (x + w, y + h * 0.64)], fill=(150, 120, 84))
        d.rectangle([x, y + h * 0.60, x + w, y + h], fill=(36, 84, 124))
        d.polygon([(x + w * 0.36, y + h * 0.62), (x + w * 0.68, y + h * 0.62), (x + w * 0.62, y + h * 0.76), (x + w * 0.42, y + h * 0.76)], fill=(28, 28, 28))
        d.rectangle([x + w * 0.44, y + h * 0.48, x + w * 0.60, y + h * 0.62], fill=(178, 44, 44))
    elif key == "cricket":
        grad(d, x, y, w, h, (52, 130, 66), (88, 166, 92))
        d.rectangle([x + w * 0.42, y + h * 0.14, x + w * 0.58, y + h * 0.90], fill=(216, 198, 150))
        for sx in (0.47, 0.53):
            for sy in (0.22, 0.78):
                d.line([x + w * sx, y + h * sy, x + w * sx, y + h * (sy + 0.08)], fill=(240, 240, 235), width=3)
        sun(d, x + w * 0.68, y + h * 0.55, 6, (200, 30, 40))
        skyline(d, x, y, w, h * 0.14, (30, 90, 44), seed)
    else:
        grad(d, x, y, w, h, (90, 100, 120), (170, 178, 190))
        sun(d, cx, cy, h * 0.16, (255, 220, 120))

def region_counts():
    counts = {}
    for reg, *_ in D.HEROES + [(p[0],) for p in D.PICTURED] + [(b[0],) for b in D.BRIEFS]:
        counts[reg] = counts.get(reg, 0) + 1
    return counts

def total_stories():
    return len(D.HEROES) + len(D.PICTURED) + len(D.BRIEFS)

def strip_regions(d, x, y, w, h, counts, font_sz=25):
    regs = [r for r in D.REGION_ORDER if counts.get(r)]
    if counts.get("WLD"): regs = regs + ["WLD"]
    tw = sum(counts[r] for r in regs)
    cx = x
    for r in regs:
        seg = w * counts[r] / tw
        d.rectangle([cx, y, cx + seg, y + h], fill=D.REGION_COLORS[r])
        label = f"{D.REGION_NAMES[r]} {counts[r]}"
        fnt = FLF(BOLD, font_sz)
        if d.textlength(label, font=fnt) <= seg - 10:
            d.text((cx + seg / 2, y + h / 2), label, font=fnt, anchor="mm", fill=(255, 255, 255))
        cx += seg

def panel(d, x, y, w, p, scene_h, seed, head_sz=27, dek_sz=21, stamp=None, dek_lines=3, ink=INK):
    reg, kicker, head, dek, src, key = p[0], p[1], p[2], p[3], p[4], p[5]
    scene(d, key, x, y, w, scene_h, seed)
    yy = y + scene_h + 8
    d.rectangle([x, yy + 2, x + 10, yy + 20], fill=D.REGION_COLORS[reg])
    d.text((x + 16, yy), kicker, font=FLF(BOLD, 19), fill=ink)
    if src:
        kw = d.textlength(kicker, font=FLF(BOLD, 19)) + 22
        sw = d.textlength(src.upper(), font=FLF(BOLD, 16))
        if kw + sw + 8 <= w:
            d.text((x + w, yy), src.upper(), font=FLF(BOLD, 16), anchor="ra", fill=GREY)
    yy += 26
    yy = text_block(d, x, yy, head, FLF(SERIFB, head_sz), w, int(head_sz * 1.12), ink, max_lines=2)
    yy += 2
    text_block(d, x, yy, dek, FLF(SERIF, dek_sz), w, int(dek_sz * 1.18), (52, 50, 46) if ink == INK else (220, 216, 208), max_lines=dek_lines)
    if stamp:
        d.rectangle([x + w - 86, y + 8, x + w - 8, y + 34], fill=(168, 32, 40))
        d.text((x + w - 47, y + 21), stamp, font=FLF(BOLD, 17), anchor="mm", fill=(255, 255, 255))

def briefs_block(d, x, y, w, start_num, cols=2, font_sz=20, lh=27, title=None):
    if title:
        d.text((x, y), title, font=FLF(BOLD, 24), fill=(168, 32, 40))
        y += 34
    colw = (w - 24) // cols
    per = (len(D.BRIEFS) + cols - 1) // cols
    for ci in range(cols):
        for ri, b in enumerate(D.BRIEFS[ci * per:(ci + 1) * per]):
            n = start_num + ci * per + ri
            bx, by = x + ci * (colw + 24), y + ri * lh
            d.ellipse([bx, by + 6, bx + 9, by + 15], fill=D.REGION_COLORS[b[0]])
            txt = f"{n} {b[1]} - {b[2]}"
            d.text((bx + 15, by), fit1(d, txt, FLF(SANS, font_sz), colw - 15), font=FLF(SANS, font_sz), fill=INK)
    return y + per * lh

def date_check(d, x, y, w, accent=(168, 32, 40)):
    d.rectangle([x, y, x + w, y + 86], outline=accent, width=3)
    d.rectangle([x, y, x + 168, y + 86], fill=accent)
    d.text((x + 84, y + 43), "DATE CHECK", font=FLF(BOLD, 24), anchor="mm", fill=(255, 255, 255))
    txt = "Left out - they broke before Friday: " + D.DATE_CHECK
    text_block(d, x + 184, y + 10, txt, FLF(SERIF, 20), w - 200, 24, INK, max_lines=3)
    return y + 86

def footer(d, x, y, w):
    d.text((x, y), D.FOOTER1, font=FLF(SERIFI, 20), fill=(52, 50, 46))
    d.text((x, y + 26), D.FOOTER2, font=FLF(SANS, 18), fill=GREY)

TIMELINE = [
    ("Overnight", "Crimean Bridge hit a third time"),
    ("~06:00 UTC", "APEC leaders meet in Shenzhen"),
    ("~10:00 UTC", "Trilateral declaration issued"),
    ("~12:00 UTC", "Akvan makes landfall in Odisha"),
    ("~14:00 UTC", "Houthi missile hits Riyadh KAFD"),
    ("Late", "Wall Street slides; Dow -1,084"),
]

def timeline(d, x, y, w, accent=(168, 32, 40)):
    d.rectangle([x, y, x + 128, y + 54], fill=accent)
    d.text((x + 64, y + 15), "THE DAY", font=FLF(BOLD, 20), anchor="ma", fill=(255, 255, 255))
    d.text((x + 64, y + 37), "IN UTC", font=FLF(BOLD, 20), anchor="ma", fill=(255, 255, 255))
    seg = (w - 140) // 6
    for i, (t, s) in enumerate(TIMELINE):
        sx = x + 140 + i * seg
        d.text((sx, y + 2), t, font=FLF(BOLD, 19), fill=accent)
        text_block(d, sx, y + 26, s, FLF(SANS, 17), seg - 8, 20, INK, max_lines=2)

def hero_panel(d, x, y, w, hp, seed, accent):
    p = (hp[0], hp[1], hp[2], hp[3], hp[4], hp[5], None, None)
    panel(d, x, y, w, p, 126, seed, head_sz=27, dek_sz=18, dek_lines=3)

def pic_rows(d, y, rows_spec, seed0, stamp=None):
    yy = y
    for row, n in rows_spec:
        pw = (W - 88 - (n - 1) * 12) // n
        for i, p in enumerate(row):
            panel(d, 44 + i * (pw + 12), yy, pw, p, 56, seed0 + i, head_sz=21, dek_sz=16, dek_lines=2, stamp=stamp)
        yy += 182
    return yy

def bottom_band(d, y, accent, map_h=252):
    d.text((44, y), "WHERE IT HAPPENED", font=FLF(BOLD, 22), fill=accent)
    d.text((500, y), f"ALSO ON FRIDAY 20 NOVEMBER - {len(D.BRIEFS)} MORE STORIES", font=FLF(BOLD, 22), fill=accent)
    box = draw_map(d, 44, y + 32, 440, map_h, 4, (120, 130, 140), sea=(16, 32, 52), r=2)
    for p in D.PICTURED:
        if p[6] is not None:
            px, py = pin_xy(box, p[6], p[7])
            num = p[1].split(" ")[0]
            d.ellipse([px - 13, py - 13, px + 13, py + 13], fill=(200, 40, 40))
            d.text((px, py), num, font=FLF(BOLD, 17), anchor="mm", fill=(255, 255, 255))
    # briefs: 3 kolom di kanan peta
    x0, y0 = 500, y + 34
    colw = (W - 44 - x0 - 32) // 3
    per = (len(D.BRIEFS) + 2) // 3
    for ci in range(3):
        for ri, b in enumerate(D.BRIEFS[ci * per:(ci + 1) * per]):
            n = 17 + ci * per + ri
            bx, by = x0 + ci * (colw + 16), y0 + ri * 22
            d.ellipse([bx, by + 5, bx + 8, by + 13], fill=D.REGION_COLORS[b[0]])
            txt = f"{n} {b[1]} - {b[2]}"
            d.text((bx + 14, by), fit1(d, txt, FLF(SANS, 16), colw - 14), font=FLF(SANS, 16), fill=INK)

def layout_a(seed=3, tint=0):
    base = (247, 243, 233) if tint == 0 else (245, 240, 228)
    im = paper(W, H, base, seed=seed)
    d = ImageDraw.Draw(im)
    accent = (168, 32, 40)
    counts = region_counts(); total = total_stories()
    d.text((44, 24), "ONE DAY OF WORLD NEWS, ONE PICTURE", font=FLF(BOLD, 22), fill=accent)
    d.text((W - 44, 24), f"{total} STORIES - 7 REGIONS - EVERY ONE FROM THIS FRIDAY", font=FLF(BOLD, 22), anchor="ra", fill=INK)
    d.line([44, 56, W - 44, 56], fill=INK, width=3)
    d.text((44, 64), D.DATE_LONG, font=FLF(SERIFB, 102), fill=INK)
    timeline(d, 44, 186, W - 88, accent)
    strip_regions(d, 44, 252, W - 88, 34, counts, font_sz=21)
    hw = (W - 88 - 24) // 3
    for i, hp in enumerate(D.HEROES):
        hero_panel(d, 44 + i * (hw + 12), 300, hw, hp, seed + i, accent)
    yy = pic_rows(d, 596, [(D.PICTURED[:5], 5), (D.PICTURED[5:9], 4), (D.PICTURED[9:], 4)], seed + 10)
    bottom_band(d, 1150, accent)
    date_check(d, 44, 1428, W - 88, accent)
    footer(d, 44, 1528, W - 88)
    return im

def layout_b(seed=5, tint=0):
    navy = (18, 26, 48)
    im = paper(W, H, (244, 242, 238), seed=seed)
    d = ImageDraw.Draw(im)
    accent = (168, 32, 40)
    counts = region_counts(); total = total_stories()
    d.rectangle([0, 0, W, 160], fill=navy)
    d.text((44, 20), "THE DAY IN WORLD NEWS - BY THE NUMBERS", font=FLF(BOLD, 22), fill=(240, 200, 90))
    d.text((W - 44, 20), f"{total} STORIES - ONE PAGE", font=FLF(BOLD, 22), anchor="ra", fill=(230, 230, 230))
    d.text((44, 50), D.DATE_LONG, font=FLF(SERIFB, 92), fill=(248, 246, 240))
    fw = (W - 88) // 6
    for i, (big, cap) in enumerate(D.FIGURES):
        fx = 44 + i * fw
        d.text((fx, 172), big, font=FLF(SERIFB, 44), fill=accent)
        text_block(d, fx, 226, cap, FLF(SANS, 16), fw - 14, 20, INK, max_lines=2)
    strip_regions(d, 44, 272, W - 88, 34, counts, font_sz=21)
    hw = (W - 88 - 24) // 3
    for i, hp in enumerate(D.HEROES):
        hero_panel(d, 44 + i * (hw + 12), 318, hw, hp, seed + i, accent)
    yy = pic_rows(d, 614, [(D.PICTURED[:4], 4), (D.PICTURED[4:8], 4), (D.PICTURED[8:], 5)], seed + 20)
    bottom_band(d, 1168, accent, map_h=240)
    date_check(d, 44, 1446, W - 88, accent)
    footer(d, 44, 1546, W - 88)
    return im

def layout_c(seed=8, tint=0):
    im = paper(W, H, (252, 244, 224), seed=seed)
    d = ImageDraw.Draw(im)
    accent = (178, 44, 44)
    counts = region_counts(); total = total_stories()
    d.text((W / 2, 22), "THE WORLD IN ONE DAY", font=FLF(BOLD, 26), anchor="ma", fill=accent)
    d.text((W / 2, 54), D.DATE_LONG, font=FLF(SERIFB, 90), anchor="ma", fill=INK)
    d.text((W / 2, 160), D.DEK, font=FLF(SERIFI, 26), anchor="ma", fill=accent)
    d.line([44, 200, W - 44, 200], fill=accent, width=3)
    strip_regions(d, 44, 212, W - 88, 34, counts, font_sz=21)
    hw = (W - 88 - 24) // 3
    for i, hp in enumerate(D.HEROES):
        p = (hp[0], hp[1], hp[2], hp[3], hp[4], hp[5], None, None)
        panel(d, 44 + i * (hw + 12), 260, hw, p, 138, seed + i, head_sz=27, dek_sz=18, dek_lines=3, stamp="20 NOV")
    yy = pic_rows(d, 578, [(D.PICTURED[:5], 5), (D.PICTURED[5:9], 4), (D.PICTURED[9:], 4)], seed + 30, stamp="20 NOV")
    bottom_band(d, 1132, accent, map_h=258)
    date_check(d, 44, 1428, W - 88, accent)
    footer(d, 44, 1528, W - 88)
    return im


def main():
    fn = {"a": layout_a, "b": layout_b, "c": layout_c}[VARIANT]
    im = fn(seed=SEED, tint=TINT)
    im = im.resize((1024, 1024), Image.LANCZOS)
    im.save("entry.png")
    try:
        os.makedirs("/output", exist_ok=True)
        im.save("/output/entry.png")
    except OSError:
        pass

if __name__ == "__main__":
    main()
