"""Generate self-contained SVG assets for the profile README (Stardew Valley theme).

Outputs (into ./assets):
  - stardew-banner.svg       : static header banner
  - stardew-banner-anim.svg  : animated banner (drifting clouds, swaying grass, blinking caret)
  - stardew-divider.svg      : pixel divider strip
  - stardew-skills.svg       : game-menu style skills panel
  - stardew-avatar.svg       : square pixel avatar / icon

The 'Press Start 2P' pixel font is embedded as base64 so everything renders
identically on GitHub with no external requests.
"""

import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = ASSETS / "pressstart2p.woff2"

font_b64 = base64.b64encode(FONT.read_bytes()).decode("ascii")

# ---------------------------------------------------------------- banner ----
ANIM_CSS = """      .cloud-a { animation: drift 16s ease-in-out infinite alternate; }
      .cloud-b { animation: bdrift 23s ease-in-out infinite alternate; }
      .sun     { animation: pulse 4s ease-in-out infinite; }
      .grass   { animation: sway 3.2s ease-in-out infinite alternate; }
      .caret   { animation: blink 1.1s steps(1) infinite; }
      @keyframes drift { from { transform: translateX(-14px); } to { transform: translateX(14px); } }
      @keyframes bdrift { from { transform: translateX(12px); } to { transform: translateX(-12px); } }
      @keyframes pulse { 0%, 100% { opacity: 0.85; } 50% { opacity: 1; } }
      @keyframes sway { from { transform: translateY(0); } to { transform: translateY(2.5px); } }
      @keyframes blink { 0%, 45% { opacity: 1; } 50%, 100% { opacity: 0; } }"""

BANNER = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="ZetvD - Stardew Valley style banner">
  <defs>
    <style>
      @font-face {
        font-family: 'PS2P';
        src: url(data:font/woff2;base64,__FONT__) format('woff2');
        font-weight: normal;
        font-style: normal;
      }
      .t { font-family: 'PS2P', ui-monospace, 'Courier New', monospace; }
__ANIM_CSS__
    </style>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8FD6F2"/>
      <stop offset="1" stop-color="#D3EEF9"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FCF2DA"/>
      <stop offset="1" stop-color="#EEDAC0"/>
    </linearGradient>
    <clipPath id="frame"><rect x="0" y="0" width="1200" height="300" rx="14"/></clipPath>
    <g id="tree">
      <rect x="-8" y="206" width="16" height="94" fill="#6B4220"/>
      <rect x="4" y="206" width="4" height="94" fill="#4A2C17"/>
      <rect x="-43" y="164" width="86" height="44" fill="#35801F"/>
      <rect x="-49" y="176" width="98" height="32" fill="#46A02E"/>
      <rect x="-29" y="146" width="58" height="44" fill="#54B237"/>
      <rect x="-19" y="152" width="22" height="14" fill="#7AD04F"/>
    </g>
    <g id="tuft">
      <path d="M-7,0 L-4,-11 L-1,0 Z" fill="#3E7B27"/>
      <path d="M-2,0 L2,-14 L6,0 Z" fill="#46A02E"/>
      <path d="M4,0 L8,-9 L11,0 Z" fill="#3E7B27"/>
    </g>
  </defs>

  <g clip-path="url(#frame)">
    <rect x="0" y="0" width="1200" height="300" fill="url(#sky)"/>

    <g class="__SUN__">
      <circle cx="1062" cy="64" r="34" fill="#F7D046"/>
      <circle cx="1062" cy="64" r="22" fill="#FBE38A"/>
    </g>

    <g class="__CA__" fill="#FFFFFF">
      <rect x="150" y="74" width="140" height="20"/>
      <rect x="172" y="58" width="84" height="18"/>
      <rect x="196" y="44" width="44" height="16"/>
      <rect x="150" y="92" width="140" height="7" fill="#E3F2FB"/>
    </g>
    <g class="__CB__" fill="#FFFFFF" opacity="0.95">
      <rect x="858" y="42" width="112" height="16"/>
      <rect x="876" y="30" width="66" height="14"/>
      <rect x="896" y="20" width="32" height="12"/>
      <rect x="858" y="57" width="112" height="6" fill="#E3F2FB"/>
    </g>

    <path d="M0,214 C 100,196 220,232 340,214 C 460,196 580,230 700,212 C 820,194 940,230 1060,214 C 1120,206 1160,210 1200,206 L1200,300 L0,300 Z" fill="#96D470"/>
    <path d="M0,240 C 130,224 250,254 380,240 C 510,226 640,252 770,238 C 900,224 1030,252 1160,238 C 1180,236 1190,238 1200,236 L1200,300 L0,300 Z" fill="#6FBF3E"/>
    <rect x="0" y="266" width="1200" height="34" fill="#56A62B"/>

    <use href="#tree" x="95"/>
    <use href="#tree" x="1105"/>

    <rect x="514" y="150" width="18" height="150" fill="#6B4220"/>
    <rect x="528" y="150" width="4" height="150" fill="#4A2C17"/>
    <rect x="668" y="150" width="18" height="150" fill="#6B4220"/>
    <rect x="682" y="150" width="4" height="150" fill="#4A2C17"/>

    <rect x="320" y="55" width="560" height="145" rx="10" fill="url(#panel)" stroke="#4A2C17" stroke-width="7"/>
    <rect x="332" y="67" width="536" height="121" rx="6" fill="none" stroke="#8B5E34" stroke-width="3"/>
    <rect x="336" y="71" width="528" height="9" rx="4" fill="#FFF7E2" opacity="0.75"/>
    <circle cx="344" cy="79" r="4" fill="#8B5E34"/>
    <circle cx="856" cy="79" r="4" fill="#8B5E34"/>
    <circle cx="344" cy="176" r="4" fill="#8B5E34"/>
    <circle cx="856" cy="176" r="4" fill="#8B5E34"/>

    <text class="t" x="602" y="148" font-size="46" letter-spacing="4" text-anchor="middle" fill="#D9C69C">ZetvD</text>
    <text class="t" x="600" y="145" font-size="46" letter-spacing="4" text-anchor="middle" fill="#4A2C17">ZetvD</text>
    __CARET__
    <rect x="556" y="158" width="88" height="3" fill="#C9A86F"/>
    <text class="t" x="600" y="180" font-size="12" letter-spacing="2" text-anchor="middle" fill="#8B5E34">FULLSTACK DEV // COZY FARMER</text>

    <g class="__GRASS__">
      <use href="#tuft" x="140" y="290"/>
      <use href="#tuft" x="250" y="278"/>
      <use href="#tuft" x="470" y="292"/>
      <use href="#tuft" x="720" y="284"/>
      <use href="#tuft" x="900" y="292"/>
      <use href="#tuft" x="1030" y="280"/>
      <use href="#tuft" x="60" y="285"/>
      <use href="#tuft" x="800" y="272"/>
      <g fill="#F2C14E">
        <rect x="330" y="284" width="7" height="7"/>
        <rect x="626" y="290" width="7" height="7"/>
        <rect x="960" y="285" width="7" height="7"/>
      </g>
    </g>
  </g>
</svg>
"""


def build_banner(animated: bool) -> str:
    caret = (
        '<rect class="caret" x="742" y="112" width="8" height="38" fill="#8B5E34"/>'
        if animated
        else ""
    )
    return (
        BANNER.replace("__FONT__", font_b64)
        .replace("__ANIM_CSS__", ANIM_CSS if animated else "")
        .replace("__CA__", "cloud-a" if animated else "")
        .replace("__CB__", "cloud-b" if animated else "")
        .replace("__SUN__", "sun" if animated else "")
        .replace("__GRASS__", "grass" if animated else "")
        .replace("__CARET__", caret)
    )


# --------------------------------------------------------------- divider ----
def build_divider() -> str:
    dashes = []
    for x in range(70, 400, 42):
        dashes.append(f'<rect x="{x}" y="13" width="26" height="4"/>')
    for x in range(500, 830, 42):
        dashes.append(f'<rect x="{x}" y="13" width="26" height="4"/>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="30" viewBox="0 0 900 30" role="img" aria-label="divider">
  <g fill="#C9A86F">{"".join(dashes)}</g>
  <rect x="424" y="9" width="10" height="10" fill="#46A02E"/>
  <rect x="466" y="9" width="10" height="10" fill="#46A02E"/>
  <circle cx="450" cy="15" r="10" fill="#F2C14E"/>
  <circle cx="450" cy="15" r="5" fill="#FBE38A"/>
</svg>
"""


# ---------------------------------------------------------------- skills ----
SKILLS_ROWS = [
    ("FRONTEND", "#F2C14E", 9),
    ("BACKEND", "#C0562E", 8),
    ("DEVOPS", "#46A02E", 7),
    ("DATABASES", "#4FA8D8", 7),
    ("NETWORKING", "#8B5E34", 6),
]


def build_skills() -> str:
    y0, step = 104, 58
    parts = []
    for i, (name, color, lvl) in enumerate(SKILLS_ROWS):
        y = y0 + i * step
        parts.append(
            f'<rect x="56" y="{y - 16}" width="32" height="32" rx="7" fill="{color}" stroke="#4A2C17" stroke-width="3"/>'
        )
        parts.append(
            f'<rect x="66" y="{y - 6}" width="12" height="12" rx="3" fill="#FFF7E2" opacity="0.9"/>'
        )
        parts.append(
            f'<text class="t" x="108" y="{y + 6}" font-size="15" letter-spacing="1" fill="#4A2C17">{name}</text>'
        )
        for s in range(10):
            x = 470 + s * 35
            fill = color if s < lvl else "#E4D2AB"
            parts.append(
                f'<rect x="{x}" y="{y - 12}" width="30" height="24" rx="4" fill="{fill}" stroke="#A98A5F" stroke-width="1.5"/>'
            )
        parts.append(
            f'<text class="t" x="882" y="{y + 7}" font-size="18" fill="{color}">{lvl}</text>'
        )
        parts.append(
            f'<text class="t" x="908" y="{y + 6}" font-size="11" fill="#9A7B5A">/10</text>'
        )
    body = "".join(parts)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="400" viewBox="0 0 1000 400" role="img" aria-label="Skills panel">
  <defs>
    <style>
      @font-face {{
        font-family: 'PS2P';
        src: url(data:font/woff2;base64,{font_b64}) format('woff2');
        font-weight: normal;
        font-style: normal;
      }}
      .t {{ font-family: 'PS2P', ui-monospace, 'Courier New', monospace; }}
    </style>
    <linearGradient id="p2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FCF2DA"/>
      <stop offset="1" stop-color="#EEDAC0"/>
    </linearGradient>
  </defs>
  <rect x="20" y="26" width="960" height="352" rx="12" fill="url(#p2)" stroke="#4A2C17" stroke-width="7"/>
  <rect x="32" y="38" width="936" height="328" rx="8" fill="none" stroke="#8B5E34" stroke-width="3"/>
  <rect x="388" y="6" width="224" height="48" rx="10" fill="#4A2C17" stroke="#2E1B0E" stroke-width="4"/>
  <text class="t" x="500" y="39" font-size="20" letter-spacing="3" text-anchor="middle" fill="#F2C14E">SKILLS</text>
  {body}
</svg>
"""


# ---------------------------------------------------------------- avatar ----
def build_avatar() -> str:
    tufts = "".join(
        f'<use href="#tuft" x="{x}" y="{y}"/>'
        for x, y in [(70, 480), (170, 468), (330, 486), (430, 474), (250, 496)]
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img" aria-label="ZetvD avatar">
  <defs>
    <style>
      @font-face {{
        font-family: 'PS2P';
        src: url(data:font/woff2;base64,{font_b64}) format('woff2');
        font-weight: normal;
        font-style: normal;
      }}
      .t {{ font-family: 'PS2P', ui-monospace, 'Courier New', monospace; }}
    </style>
    <linearGradient id="asky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#8FD6F2"/>
      <stop offset="1" stop-color="#D3EEF9"/>
    </linearGradient>
    <linearGradient id="apanel" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FCF2DA"/>
      <stop offset="1" stop-color="#EEDAC0"/>
    </linearGradient>
    <clipPath id="aclip"><rect x="0" y="0" width="512" height="512" rx="72"/></clipPath>
    <g id="tuft">
      <path d="M-7,0 L-4,-13 L-1,0 Z" fill="#3E7B27"/>
      <path d="M-2,0 L2,-16 L6,0 Z" fill="#46A02E"/>
      <path d="M4,0 L8,-11 L11,0 Z" fill="#3E7B27"/>
    </g>
  </defs>
  <g clip-path="url(#aclip)">
    <rect x="0" y="0" width="512" height="512" fill="url(#asky)"/>
    <circle cx="410" cy="90" r="40" fill="#F7D046"/>
    <circle cx="410" cy="90" r="25" fill="#FBE38A"/>
    <g fill="#FFFFFF">
      <rect x="60" y="96" width="120" height="18"/>
      <rect x="80" y="82" width="70" height="16"/>
      <rect x="100" y="70" width="36" height="14"/>
    </g>
    <path d="M0,378 C 90,362 180,392 270,376 C 360,360 450,390 512,374 L512,512 L0,512 Z" fill="#96D470"/>
    <rect x="0" y="420" width="512" height="92" fill="#6FBF3E"/>
    <rect x="0" y="470" width="512" height="42" fill="#56A62B"/>
    <rect x="96" y="150" width="320" height="180" rx="16" fill="url(#apanel)" stroke="#4A2C17" stroke-width="10"/>
    <rect x="112" y="166" width="288" height="148" rx="10" fill="none" stroke="#8B5E34" stroke-width="4"/>
    <circle cx="126" cy="180" r="5" fill="#8B5E34"/>
    <circle cx="386" cy="180" r="5" fill="#8B5E34"/>
    <circle cx="126" cy="300" r="5" fill="#8B5E34"/>
    <circle cx="386" cy="300" r="5" fill="#8B5E34"/>
    <text class="t" x="257" y="252" font-size="56" letter-spacing="2" text-anchor="middle" fill="#4A2C17">ZetvD</text>
    <rect x="196" y="266" width="122" height="3" fill="#C9A86F"/>
    <text class="t" x="257" y="292" font-size="12" letter-spacing="2" text-anchor="middle" fill="#8B5E34">DEV // FARMER</text>
    {tufts}
  </g>
</svg>
"""


def main() -> None:
    files = {
        "stardew-banner.svg": build_banner(animated=False),
        "stardew-banner-anim.svg": build_banner(animated=True),
        "stardew-divider.svg": build_divider(),
        "stardew-skills.svg": build_skills(),
        "stardew-avatar.svg": build_avatar(),
    }
    for name, svg in files.items():
        (ASSETS / name).write_text(svg, encoding="utf-8")
    for name in files:
        p = ASSETS / name
        print(f"wrote {p.relative_to(ROOT)} ({p.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
