import os

WORKSPACE = r"c:\Users\TRB\modified mindspace sdg\CrediAI\GIT-PROFILE"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
TRB_DIR = os.path.join(WORKSPACE, "trb-89", "assets")

PROJECTS = [
    {
        "id": "agent-os",
        "num": "01",
        "title": "A G E N T . O S",
        "category": "AUTONOMOUS AGENT RUNTIME",
        "status": "EXPERIMENTAL",
        "desc": "Operating framework for autonomous AI agents with task orchestration,",
        "desc2": "persistent memory architecture, dynamic tool execution & multi-agent mesh.",
        "stack": "PYTHON  //  LANGCHAIN  //  AGENTIC AI  //  VECTOR MEMORY",
        "repo": "https://github.com/trb-89/agent-os",
        "graphic": "mesh"
    },
    {
        "id": "sentinel-ai",
        "num": "02",
        "title": "S E N T I N E L   A I",
        "category": "DEFENSIVE THREAT INTELLIGENCE",
        "status": "IN DEVELOPMENT",
        "desc": "Autonomous security intelligence engine focused on predictive threat",
        "desc2": "pattern detection, automated defense workflows, and audit stream triage.",
        "stack": "PYTHON  //  GEMINI API  //  SECURITY WORKFLOWS  //  REST",
        "repo": "https://github.com/trb-89/sentinel-ai",
        "graphic": "radar"
    },
    {
        "id": "aura",
        "num": "03",
        "title": "A U R A",
        "category": "MULTIMODAL EMOTIONAL COMPANION",
        "status": "IN DEVELOPMENT",
        "desc": "Conversational AI companion designed for emotional reflection,",
        "desc2": "expressive voice support, and empathetic context-aware adaptation.",
        "stack": "REACT  //  NODE.JS  //  LLM INTEGRATION  //  VOICE AI",
        "repo": "https://github.com/trb-89/aura",
        "graphic": "wave"
    },
    {
        "id": "gfg",
        "num": "04",
        "title": "G A P   F O R   G O O D",
        "category": "AI CAREER ACCELERATOR",
        "status": "DEPLOYED",
        "desc": "AI-enabled platform empowering women to rebuild engineering competencies",
        "desc2": "and return smoothly to high-impact technical roles post career break.",
        "stack": "SPRING BOOT  //  REACT  //  POSTGRESQL  //  GEMINI API",
        "repo": "https://github.com/trb-89/gap-for-good",
        "graphic": "lattice"
    },
    {
        "id": "one-planet",
        "num": "05",
        "title": "O N E   P L A N E T",
        "category": "SUSTAINABILITY ACTION PLATFORM",
        "status": "DEPLOYED",
        "desc": "Open platform supporting all 17 UN Sustainable Development Goals via",
        "desc2": "distributed problem intake, verification telemetry, and action hubs.",
        "stack": "VITE  //  REACT  //  SUPABASE  //  OPEN APIS",
        "repo": "https://github.com/trb-89/one-planet",
        "graphic": "globe"
    }
]

def render_graphic(kind):
    if kind == "mesh":
        return '''
        <!-- Mesh Wireframe -->
        <g stroke="#555555" stroke-width="1" fill="none">
          <circle cx="730" cy="50" r="16" stroke="#C0C0C0" stroke-width="1.2"/>
          <circle cx="680" cy="115" r="12"/>
          <circle cx="780" cy="115" r="12"/>
          <circle cx="730" cy="140" r="8" fill="#FFFFFF"/>
          <line x1="730" y1="66" x2="680" y2="103"/>
          <line x1="730" y1="66" x2="780" y2="103"/>
          <line x1="680" y1="127" x2="730" y2="132"/>
          <line x1="780" y1="127" x2="730" y2="132"/>
          <circle cx="730" cy="50" r="4" fill="#C0C0C0"/>
        </g>
        '''
    elif kind == "radar":
        return '''
        <!-- Radar Wireframe -->
        <g stroke="#444444" stroke-width="1" fill="none">
          <circle cx="730" cy="95" r="45" stroke="#333333"/>
          <circle cx="730" cy="95" r="30" stroke="#555555"/>
          <circle cx="730" cy="95" r="15" stroke="#C0C0C0"/>
          <line x1="730" y1="50" x2="730" y2="140" stroke="#333333"/>
          <line x1="685" y1="95" x2="775" y2="95" stroke="#333333"/>
          <line x1="730" y1="95" x2="760" y2="65" stroke="#FFFFFF" stroke-width="1.5"/>
          <circle cx="750" cy="75" r="2.5" fill="#FFFFFF"/>
        </g>
        '''
    elif kind == "wave":
        return '''
        <!-- Resonance Frequency Wave -->
        <g stroke="#666666" stroke-width="1" fill="none">
          <path d="M 670,95 Q 685,60 700,95 T 730,95 T 760,95 T 790,95" stroke="#888888"/>
          <path d="M 670,95 Q 685,45 700,95 T 730,95 T 760,95 T 790,95" stroke="#C0C0C0" stroke-width="1.2"/>
          <path d="M 670,95 Q 685,75 700,95 T 730,95 T 760,95 T 790,95" stroke="#444444"/>
          <circle cx="730" cy="95" r="3" fill="#FFFFFF"/>
        </g>
        '''
    elif kind == "lattice":
        return '''
        <!-- Geometric Diamond Lattice -->
        <g stroke="#555555" stroke-width="1" fill="none">
          <polygon points="730,55 765,95 730,135 695,95" stroke="#C0C0C0" stroke-width="1.2"/>
          <polygon points="730,70 750,95 730,120 710,95" stroke="#666666"/>
          <circle cx="730" cy="95" r="3" fill="#FFFFFF"/>
          <line x1="695" y1="95" x2="765" y2="95" stroke="#333333"/>
        </g>
        '''
    elif kind == "globe":
        return '''
        <!-- Minimal Isometric Globe Sphere -->
        <g stroke="#444444" stroke-width="1" fill="none">
          <circle cx="730" cy="95" r="40" stroke="#C0C0C0" stroke-width="1.2"/>
          <ellipse cx="730" cy="95" rx="40" ry="16" stroke="#666666"/>
          <ellipse cx="730" cy="95" rx="16" ry="40" stroke="#666666"/>
          <circle cx="730" cy="95" r="3" fill="#FFFFFF"/>
        </g>
        '''

def generate_project_svgs():
    print("Generating project SVG cards...")
    for p in PROJECTS:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 180" width="100%" height="180" fill="none">
  <defs>
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3a3a3a"/>
      <stop offset="50%" stop-color="#1f1f1f"/>
      <stop offset="100%" stop-color="#3a3a3a"/>
    </linearGradient>
  </defs>

  <!-- Background Base -->
  <rect width="840" height="180" fill="#090909" rx="0"/>
  <rect x="0.5" y="0.5" width="839" height="179" fill="none" stroke="url(#cardBorder)" stroke-width="1"/>

  <!-- Brutalist Corner Markers -->
  <path d="M 12 18 L 18 18 M 18 12 L 18 18" stroke="#888888" stroke-width="1"/>
  <path d="M 828 18 L 822 18 M 822 12 L 822 18" stroke="#888888" stroke-width="1"/>
  <path d="M 12 162 L 18 162 M 18 168 L 18 162" stroke="#888888" stroke-width="1"/>
  <path d="M 828 162 L 822 162 M 822 168 L 822 162" stroke="#888888" stroke-width="1"/>

  <!-- Classification Header -->
  <text x="32" y="34" font-family="'Consolas', 'Courier New', monospace" font-size="11" fill="#777777" letter-spacing="1.5">SYS // {p['num']}  —  {p['category']}</text>

  <!-- Status Pill Tag -->
  <g transform="translate(520, 22)">
    <rect x="0" y="0" width="115" height="18" fill="#121212" stroke="#444444" stroke-width="0.8"/>
    <text x="57" y="13" font-family="'Consolas', 'Courier New', monospace" font-size="9" fill="#E5E5E5" text-anchor="middle" letter-spacing="1">[{p['status']}]</text>
  </g>

  <!-- Main Title -->
  <text x="32" y="74" font-family="'Impact', 'Arial Black', sans-serif" font-size="24" fill="#FFFFFF" letter-spacing="2">{p['title']}</text>

  <!-- Description Lines -->
  <text x="32" y="104" font-family="'Consolas', 'Courier New', monospace" font-size="12" fill="#B0B0B0">{p['desc']}</text>
  <text x="32" y="122" font-family="'Consolas', 'Courier New', monospace" font-size="12" fill="#888888">{p['desc2']}</text>

  <!-- Divider Line -->
  <line x1="32" y1="142" x2="630" y2="142" stroke="#1c1c1c" stroke-width="1"/>

  <!-- Tech Stack -->
  <text x="32" y="159" font-family="'Consolas', 'Courier New', monospace" font-size="10" fill="#666666" letter-spacing="1">{p['stack']}</text>

  <!-- Right Geometric Artwork -->
  {render_graphic(p['graphic'])}

  <!-- Subtle Link Indicator -->
  <text x="618" y="159" font-family="'Consolas', 'Courier New', monospace" font-size="10" fill="#AAAAAA" text-anchor="end">VIEW REPO ↗</text>
</svg>'''

        filename = f"project-{p['id']}.svg"
        for folder in [ASSETS_DIR, TRB_DIR]:
            with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Saved {filename}")

if __name__ == "__main__":
    generate_project_svgs()
