import os

WORKSPACE = r"c:\Users\TRB\modified mindspace sdg\CrediAI\GIT-PROFILE"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
TRB_DIR = os.path.join(WORKSPACE, "trb-89", "assets")

def generate_snake_preview():
    # An aesthetic monochrome contribution grid preview with an animated silver snake
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 140" width="100%" height="140" fill="none">
  <style>
    .cell { shape-rendering: geometricPrecision; rx: 2px; }
    .bg { fill: #000000; }
    .grid-border { stroke: #262626; stroke-width: 1; }
    .text-mono { font-family: 'Consolas', 'Courier New', monospace; font-size: 11px; fill: #888888; }
    .snake-head { fill: #FFFFFF; }
    .snake-body { fill: #C0C0C0; }
    @keyframes crawl {
      0% { transform: translateX(0px); }
      50% { transform: translateX(45px); }
      100% { transform: translateX(0px); }
    }
    .snake-group { animation: crawl 5s ease-in-out infinite; }
  </style>

  <rect width="840" height="140" class="bg"/>
  <rect x="0.5" y="0.5" width="839" height="139" fill="none" class="grid-border"/>

  <!-- Header line -->
  <text x="25" y="24" class="text-mono">[ TELEMETRY // CONTRIBUTION GRAPH &amp; RUNTIME TRACE ]</text>
  <text x="710" y="24" class="text-mono">STATUS: SYNCED</text>
  <line x1="25" y1="34" x2="815" y2="34" stroke="#1c1c1c" stroke-width="1"/>

  <!-- Matrix of cells: 52 columns x 5 rows -->
  <g transform="translate(25, 48)">
'''
    import random
    random.seed(89)
    colors = ["#121212", "#121212", "#1f1f1f", "#333333", "#555555", "#888888", "#C0C0C0"]
    weights = [40, 25, 15, 10, 5, 3, 2]
    
    for col in range(52):
        x = col * 15
        for row in range(5):
            y = row * 15
            c = random.choices(colors, weights=weights)[0]
            svg += f'    <rect x="{x}" y="{y}" width="11" height="11" fill="{c}" class="cell"/>\n'

    # Animated snake crawling over a segment
    svg += '''
    <!-- Silver Monochrome Snake Entity -->
    <g class="snake-group">
      <rect x="360" y="30" width="11" height="11" class="cell snake-head"/>
      <rect x="345" y="30" width="11" height="11" class="cell snake-body"/>
      <rect x="330" y="30" width="11" height="11" class="cell snake-body" fill="#888888"/>
      <rect x="315" y="30" width="11" height="11" class="cell snake-body" fill="#555555"/>
      <rect x="315" y="15" width="11" height="11" class="cell snake-body" fill="#333333"/>
    </g>
  </g>
</svg>'''

    for p in [os.path.join(ASSETS_DIR, "snake-preview.svg"), os.path.join(TRB_DIR, "snake-preview.svg")]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(svg)
    print("Saved snake-preview.svg")

if __name__ == "__main__":
    generate_snake_preview()
