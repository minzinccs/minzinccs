"""Generate self-contained SVG assets for the profile README.

Outputs (into ./assets):
  - stardew-banner.svg   : Stardew Valley style header banner
  - stardew-divider.svg  : pixel divider strip

Both embed the 'Press Start 2P' pixel font as base64 where text is used,
so they render identically on GitHub (no external requests).
"""

import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONT = ASSETS / "pressstart2p.woff2"

font_b64 = base64.b64encode(FONT.read_bytes()).decode("ascii")

# ---------------------------------------------------------------- banner ----
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

    <circle cx="1062" cy="64" r="34" fill="#F7D046"/>
    <circle cx="1062" cy="64" r="22" fill="#FBE38A"/>

    <g fill="#FFFFFF">
      <rect x="150" y="74" width="140" height="20"/>
      <rect x="172" y="58" width="84" height="18"/>
      <rect x="196" y="44" width="44" height="16"/>
      <rect x="150" y="92" width="140" height="7" fill="#E3F2FB"/>
    </g>
    <g fill="#FFFFFF" opacity="0.95">
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
    <rect x="556" y="158" width="88" height="3" fill="#C9A86F"/>
    <text class="t" x="600" y="180" font-size="12" letter-spacing="2" text-anchor="middle" fill="#8B5E34">FULLSTACK DEV // COZY FARMER</text>

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
</svg>
"""


# --------------------------------------------------------------- divider ----
def build_divider() -> str:
    dashes = []
    for x in range(70, 400, 42):
        dashes.append(f'<rect x="{x}" y="13" width="26" height="4"/>')
    for x in range(500, 830, 42):
        dashes.append(f'<rect x="{x}" y="13" width="26" height="4"/>')
    dash_svg = "".join(dashes)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="900" height="30" viewBox="0 0 900 30" role="img" aria-label="divider">
  <g fill="#C9A86F">{dash_svg}</g>
  <rect x="424" y="9" width="10" height="10" fill="#46A02E"/>
  <rect x="466" y="9" width="10" height="10" fill="#46A02E"/>
  <circle cx="450" cy="15" r="10" fill="#F2C14E"/>
  <circle cx="450" cy="15" r="5" fill="#FBE38A"/>
</svg>
"""


def main() -> None:
    (ASSETS / "stardew-banner.svg").write_text(
        BANNER.replace("__FONT__", font_b64), encoding="utf-8"
    )
    (ASSETS / "stardew-divider.svg").write_text(build_divider(), encoding="utf-8")
    for name in ("stardew-banner.svg", "stardew-divider.svg"):
        p = ASSETS / name
        print(f"wrote {p.relative_to(ROOT)} ({p.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
