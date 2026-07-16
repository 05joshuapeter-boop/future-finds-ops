import sys

segs = [
    (0.427, 0.626, "Oh..."),
    (1.198, 1.884, "while I've got you."),
    (2.327, 3.053, "Jam first."),
    (3.323, 3.945, "On a scone."),
    (4.328, 5.254, "It's structural..."),
    (5.507, 6.820, "the cream sits better on top."),
    (7.754, 9.175, "I know exactly what I've just started..."),
    (9.459, 10.05, "sorry."),
]

PLAY_RES_X = 720
PLAY_RES_Y = 1280

def ts(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: {resx}
PlayResY: {resy}
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
{styles}

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

# ---------- STYLE A: "Whisper" - clean phrase-level, thin, off-white, minimal ----------
def style_a():
    styles = "Style: Whisper,Avenir Next,15,&H00F5F0EB,&H00F5F0EB,&H001a1a1a,&H64000000,0,0,0,0,100,100,2.2,0,1,1.1,0,2,60,60,120,1"
    lines = []
    for (a, b, text) in segs:
        lines.append(f"Dialogue: 0,{ts(a)},{ts(b)},Whisper,,0,0,0,,{text.upper()}")
    return HEADER.format(resx=PLAY_RES_X, resy=PLAY_RES_Y, styles=styles) + "\n".join(lines)

# ---------- STYLE B: "Signal" - word-by-word highlight, warm accent pop on active word ----------
def style_b():
    base_style = "Style: SignalBase,Avenir Next,16,&H00F5F0EB,&H00F5F0EB,&H001a1a1a,&H64000000,1,0,0,0,100,100,1.0,0,1,1.2,0,2,60,60,120,1"
    styles = base_style
    lines = []
    ACCENT = "&H0047A8FF"  # warm amber/orange in BGR hex (spectrum gradient warm end)
    BASE = "&H00F5F0EB"    # off-white
    for (a, b, text) in segs:
        words_upper = text.upper().split(" ")
        dur = b - a
        total_chars = sum(len(w) for w in words_upper) or 1
        t = a
        for i, w in enumerate(words_upper):
            w_dur = dur * (len(w) / total_chars)
            w_end = min(t + w_dur, b)
            # build the line: words before = base color, current word = accent+bold, words after = base
            # uppercase FIRST, then wrap in override tags (tags are case-sensitive, must stay lowercase)
            parts = []
            for j, w2 in enumerate(words_upper):
                if j == i:
                    parts.append("{\\c" + ACCENT + "\\b1}" + w2 + "{\\c" + BASE + "\\b0}")
                else:
                    parts.append(w2)
            line_text = " ".join(parts)
            lines.append(f"Dialogue: 0,{ts(t)},{ts(w_end)},SignalBase,,0,0,0,,{line_text}")
            t = w_end
    return HEADER.format(resx=PLAY_RES_X, resy=PLAY_RES_Y, styles=styles) + "\n".join(lines)

# ---------- STYLE C: "Precision" - letter-spaced small caps, geometric tick underline ----------
def style_c():
    styles = "Style: Precision,Avenir Next,13,&H00F5F0EB,&H00F5F0EB,&H001a1a1a,&H64000000,0,0,0,0,100,100,3.5,0,1,1.0,0,2,60,60,130,1"
    lines = []
    for (a, b, text) in segs:
        # small geometric tick before text using a thin line character, letter-spaced via ASS \fsp already in style
        lines.append(f"Dialogue: 0,{ts(a)},{ts(b)},Precision,,0,0,0,,{{\\fscx100}}—  {text.upper()}")
    return HEADER.format(resx=PLAY_RES_X, resy=PLAY_RES_Y, styles=styles) + "\n".join(lines)

if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    with open(f"{outdir}/style_A_whisper.ass", "w", encoding="utf-8") as f:
        f.write(style_a())
    with open(f"{outdir}/style_B_signal.ass", "w", encoding="utf-8") as f:
        f.write(style_b())
    with open(f"{outdir}/style_C_precision.ass", "w", encoding="utf-8") as f:
        f.write(style_c())
    print("wrote 3 ASS files")
