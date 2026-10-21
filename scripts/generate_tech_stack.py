import os

WORKSPACE = r"c:\Users\TRB\modified mindspace sdg\CrediAI\GIT-PROFILE"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
TRB_DIR = os.path.join(WORKSPACE, "trb-89", "assets")

def generate_tech_stack_svg():
    print("Generating tech-stack.svg...")
    
    categories = [
        ("01", "LANGUAGES", ["PYTHON", "JAVA", "C", "JAVASCRIPT", "SQL"]),
        ("02", "FRONTEND", ["REACT", "HTML5", "CSS3", "VITE"]),
        ("03", "BACKEND", ["SPRING BOOT", "NODE.JS", "REST APIS"]),
        ("04", "DATABASE & INFRA", ["MYSQL", "POSTGRESQL", "SUPABASE", "GIT", "GITHUB"]),
        ("05", "ARTIFICIAL INTELLIGENCE", ["GEMINI API", "LLM INTEGRATION", "AGENT ORCHESTRATION", "AI APPLICATION DEV"])
    ]
    
    WIDTH = 840
    HEIGHT = 380
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="100%" height="{HEIGHT}" fill="none">
  <defs>
    <linearGradient id="gridBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#333333"/>
      <stop offset="50%" stop-color="#1a1a1a"/>
      <stop offset="100%" stop-color="#333333"/>
    </linearGradient>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" fill="#090909"/>
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" fill="none" stroke="url(#gridBorder)" stroke-width="1"/>

  <!-- Top System Header -->
  <path d="M 12 18 L 18 18 M 18 12 L 18 18" stroke="#888888" stroke-width="1"/>
  <path d="M {WIDTH - 12} 18 L {WIDTH - 18} 18 M {WIDTH - 18} 12 L {WIDTH - 18} 18" stroke="#888888" stroke-width="1"/>
  <text x="28" y="28" font-family="'Consolas', 'Courier New', monospace" font-size="11" fill="#777777" letter-spacing="1.5">SYS // CAPABILITIES MATRIX  —  CLASSIFIED STACK ARCHITECTURE</text>
  <text x="{WIDTH - 28}" y="28" font-family="'Consolas', 'Courier New', monospace" font-size="11" fill="#555555" text-anchor="end">STATUS: DEPLOYABLE</text>
  <line x1="28" y1="38" x2="{WIDTH - 28}" y2="38" stroke="#1c1c1c" stroke-width="1"/>
'''
    
    # 5 categories laid out cleanly
    # Row 1: Languages, Frontend (x=28, x=430)
    # Row 2: Backend, Database & Infra
    # Row 3: AI (full width)
    
    cards = [
        (28, 52, 380, 85, categories[0]),
        (432, 52, 380, 85, categories[1]),
        (28, 150, 380, 85, categories[2]),
        (432, 150, 380, 85, categories[3]),
        (28, 248, 784, 105, categories[4]),
    ]
    
    for cx, cy, cw, ch, (num, cat_title, items) in cards:
        svg += f'''
  <!-- Card: {cat_title} -->
  <g transform="translate({cx}, {cy})">
    <rect width="{cw}" height="{ch}" fill="#000000" stroke="#222222" stroke-width="0.8"/>
    <text x="14" y="20" font-family="'Consolas', 'Courier New', monospace" font-size="10" fill="#666666" letter-spacing="1">[{num}] // {cat_title}</text>
    <g transform="translate(14, 34)">
'''
        # Render item tags
        tag_x = 0
        tag_y = 0
        for item in items:
            tag_w = len(item) * 7.5 + 20
            if tag_x + tag_w > cw - 28 and cx == 28 and ch > 90:
                # Wrap for AI section if needed
                tag_x = 0
                tag_y += 28
                
            svg += f'''      <g transform="translate({tag_x}, {tag_y})">
        <rect width="{tag_w}" height="22" fill="#0d0d0d" stroke="#333333" stroke-width="0.8" rx="0"/>
        <text x="{tag_w / 2}" y="15" font-family="'Consolas', 'Courier New', monospace" font-size="10" fill="#E5E5E5" text-anchor="middle" letter-spacing="0.8">{item}</text>
      </g>
'''
            tag_x += tag_w + 8

        svg += '''    </g>
  </g>
'''

    # Bottom footer tag
    svg += f'''
  <line x1="28" y1="{HEIGHT - 20}" x2="{WIDTH - 28}" y2="{HEIGHT - 20}" stroke="#141414" stroke-width="1"/>
  <text x="28" y="{HEIGHT - 8}" font-family="'Consolas', 'Courier New', monospace" font-size="9" fill="#444444">RUNTIME ENVIRONMENT: LINUX / DARWIN / WINDOWS  —  COMPILER: GCC / OPENJDK / NODE</text>
  <text x="{WIDTH - 28}" y="{HEIGHT - 8}" font-family="'Consolas', 'Courier New', monospace" font-size="9" fill="#444444" text-anchor="end">SYS.AUTH // VERIFIED</text>
</svg>'''

    for folder in [ASSETS_DIR, TRB_DIR]:
        with open(os.path.join(folder, "tech-stack.svg"), "w", encoding="utf-8") as f:
            f.write(svg)
    print("Saved tech-stack.svg")

if __name__ == "__main__":
    generate_tech_stack_svg()
