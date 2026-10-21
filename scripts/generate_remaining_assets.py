import os
import random
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WORKSPACE = r"c:\Users\TRB\modified mindspace sdg\CrediAI\GIT-PROFILE"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
TRB_DIR = os.path.join(WORKSPACE, "trb-89", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(TRB_DIR, exist_ok=True)

# Fonts
def get_font(name, size):
    try:
        if name == "mono_bold":
            return ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", size)
        elif name == "mono":
            return ImageFont.truetype("C:/Windows/Fonts/consola.ttf", size)
        elif name == "title":
            return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
        elif name == "impact":
            return ImageFont.truetype("C:/Windows/Fonts/impact.ttf", size)
    except:
        pass
    return ImageFont.load_default()

# -------------------------------------------------------------
# 1. GLITCH HEADING (TRB-89 / CREATE / DISRUPT / REPEAT)
# -------------------------------------------------------------
def create_glitch_heading():
    print("Generating glitch-heading.gif...")
    WIDTH, HEIGHT = 840, 150
    font_title = get_font("impact", 46)
    font_sub1 = get_font("mono_bold", 15)
    font_sub2 = get_font("mono", 12)
    
    # Base clean render
    base = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
    draw = ImageDraw.Draw(base)
    
    t1 = "T R B - 8 9"
    t2 = "CREATE  /  DISRUPT  /  REPEAT"
    t3 = "AI SYSTEMS   —   AUTONOMOUS AGENTS   —   FULL STACK ENGINEERING"
    
    # Measure text
    bbox1 = draw.textbbox((0, 0), t1, font=font_title)
    w1, h1 = bbox1[2] - bbox1[0], bbox1[3] - bbox1[1]
    x1 = (WIDTH - w1) // 2
    y1 = 15
    
    bbox2 = draw.textbbox((0, 0), t2, font=font_sub1)
    w2, h2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    x2 = (WIDTH - w2) // 2
    y2 = y1 + h1 + 18
    
    bbox3 = draw.textbbox((0, 0), t3, font=font_sub2)
    w3, h3 = bbox3[2] - bbox3[0], bbox3[3] - bbox3[1]
    x3 = (WIDTH - w3) // 2
    y3 = y2 + h2 + 14
    
    # Draw base
    draw.text((x1, y1), t1, font=font_title, fill=(255, 255, 255, 255))
    draw.text((x2, y2), t2, font=font_sub1, fill=(192, 192, 192, 255))
    draw.text((x3, y3), t3, font=font_sub2, fill=(140, 140, 140, 255))
    
    frames = []
    NUM_FRAMES = 32
    
    random.seed(42)
    for f in range(NUM_FRAMES):
        frame = base.copy()
        
        # Determine if this frame has glitch
        # Periodic glitch at frame 6-8 and 20-22
        is_glitch = (6 <= f <= 8) or (20 <= f <= 22) or (f == 14)
        
        if is_glitch:
            arr = np.array(frame)
            # 1. Horizontal slice shifts
            num_slices = random.randint(2, 5)
            for _ in range(num_slices):
                slice_y = random.randint(10, HEIGHT - 25)
                slice_h = random.randint(4, 16)
                shift = random.choice([-12, -8, 8, 14, -18, 20])
                arr[slice_y:slice_y+slice_h, :, :] = np.roll(arr[slice_y:slice_y+slice_h, :, :], shift, axis=1)
                
            # 2. Chrome channel jitter (displace silver/white channels)
            jitter_y = random.randint(15, 75)
            arr[jitter_y:jitter_y+20, :, 0] = np.roll(arr[jitter_y:jitter_y+20, :, 0], 4, axis=1)
            arr[jitter_y:jitter_y+20, :, 2] = np.roll(arr[jitter_y:jitter_y+20, :, 2], -4, axis=1)
            
            # 3. Interlace scanlines on glitch frame
            for y in range(0, HEIGHT, 3):
                arr[y, :, :3] = (arr[y, :, :3] * 0.4).astype(np.uint8)
                
            frame = Image.fromarray(arr)
        else:
            # Subtle silver specular sheen traveling across the title
            draw_frame = ImageDraw.Draw(frame)
            # Scanline subtle texture
            # Very faint scanlines
            arr = np.array(frame)
            # Subtle breathing luminance
            breath = 0.96 + 0.04 * math.sin(2 * math.pi * f / NUM_FRAMES)
            arr[:, :, :3] = np.clip(arr[:, :, :3] * breath, 0, 255).astype(np.uint8)
            frame = Image.fromarray(arr)
            
        rgb = frame.convert("RGB")
        frames.append(rgb.quantize(colors=64, method=Image.Resampling.LANCZOS))
        
    for p in [os.path.join(ASSETS_DIR, "glitch-heading.gif"), os.path.join(TRB_DIR, "glitch-heading.gif")]:
        frames[0].save(p, save_all=True, append_images=frames[1:], duration=100, loop=0, optimize=True)
    print(f"Saved glitch-heading.gif ({os.path.getsize(p) / 1024:.1f} KB)")

# -------------------------------------------------------------
# 2. ANIMATED TERMINAL (terminal.gif)
# -------------------------------------------------------------
def create_terminal_gif():
    print("Generating terminal.gif...")
    WIDTH, HEIGHT = 840, 360
    font_mono = get_font("mono", 14)
    font_bold = get_font("mono_bold", 14)
    font_header = get_font("mono", 12)
    
    # Terminal typing script
    # Each entry: (text, type: 'cmd' or 'resp' or 'active', is_instant: bool)
    script = [
        ("$ whoami", "cmd"),
        ("> trb-89", "resp"),
        ("", "blank"),
        ("$ initialize --profile", "cmd"),
        ("> AI SYSTEMS ENGINEER", "resp"),
        ("", "blank"),
        ("$ loading modules...", "cmd"),
        ("> AGENTIC AI             [ACTIVE]", "module_active"),
        ("> AUTONOMOUS SYSTEMS     [ACTIVE]", "module_active"),
        ("> FULL STACK ENGINEERING [ACTIVE]", "module_active"),
        ("> MACHINE LEARNING       [LEARNING]", "module_learn"),
        ("", "blank"),
        ("$ system.status", "cmd"),
        ("> ONLINE_", "status_online")
    ]
    
    # We will generate snapshots representing realistic typing
    # Total frames ~ 55-65 frames
    terminal_states = []
    
    # State builder:
    # We simulate line by line
    current_lines = []
    
    for item, kind in script:
        if kind == "blank":
            current_lines.append(("", "blank"))
            terminal_states.append((list(current_lines), False, 1))
        elif kind == "cmd":
            # Type character by character
            cmd_prefix = "$ "
            chars = item[2:]
            typed = "$ "
            # First show prompt
            current_lines.append((typed, "cmd"))
            terminal_states.append((list(current_lines), True, 2))
            # Type chunks
            step = 2 if len(chars) > 10 else 1
            for idx in range(0, len(chars), step):
                chunk = chars[:idx+step]
                current_lines[-1] = (cmd_prefix + chunk, "cmd")
                terminal_states.append((list(current_lines), True, 1))
            # Settle after typing command
            current_lines[-1] = (item, "cmd")
            terminal_states.append((list(current_lines), False, 3))
        elif kind == "resp":
            # Output appears
            current_lines.append((item, "resp"))
            terminal_states.append((list(current_lines), False, 4))
        elif kind.startswith("module"):
            current_lines.append((item, kind))
            terminal_states.append((list(current_lines), False, 2))
        elif kind == "status_online":
            current_lines.append((item, "status_online"))
            # Settle with blinking cursor on ONLINE_
            terminal_states.append((list(current_lines), True, 6))
            terminal_states.append((list(current_lines), False, 5))
            terminal_states.append((list(current_lines), True, 6))
            terminal_states.append((list(current_lines), False, 5))
            terminal_states.append((list(current_lines), True, 8))
            
    # Now render each state into an image
    frames = []
    durations = []
    
    LINE_HEIGHT = 20
    PAD_X = 28
    PAD_Y = 55
    
    for lines, cursor_visible, repeat_count in terminal_states:
        img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
        draw = ImageDraw.Draw(img)
        
        # 1. Window Frame
        # Outer thin border
        draw.rectangle([(0, 0), (WIDTH - 1, HEIGHT - 1)], outline=(40, 40, 40, 255), width=1)
        # Header bar
        draw.rectangle([(1, 1), (WIDTH - 2, 34)], fill=(12, 12, 12, 255))
        draw.line([(1, 35), (WIDTH - 2, 35)], fill=(34, 34, 34, 255), width=1)
        
        # Window buttons: monochrome minimalist
        draw.ellipse([(16, 12), (26, 22)], fill=(48, 48, 48, 255), outline=(70, 70, 70, 255))
        draw.ellipse([(34, 12), (44, 22)], fill=(48, 48, 48, 255), outline=(70, 70, 70, 255))
        draw.ellipse([(52, 12), (62, 22)], fill=(48, 48, 48, 255), outline=(70, 70, 70, 255))
        
        # Header text
        header_text = "trb-89@kernel: ~ / identity.sh   [STATUS: ACTIVE]"
        draw.text((80, 10), header_text, font=font_header, fill=(160, 160, 160, 255))
        
        # Brutalist right tag
        draw.text((WIDTH - 150, 10), "SYS//V4.09.X", font=font_header, fill=(80, 80, 80, 255))
        
        # 2. Render terminal lines
        y = PAD_Y
        for line_idx, (text, kind) in enumerate(lines):
            if kind == "cmd":
                # Silver / White
                draw.text((PAD_X, y), text, font=font_bold, fill=(240, 240, 240, 255))
                if cursor_visible and line_idx == len(lines) - 1:
                    bbox = draw.textbbox((PAD_X, y), text, font=font_bold)
                    cx = bbox[2] + 2
                    draw.rectangle([(cx, y + 2), (cx + 8, y + 15)], fill=(220, 220, 220, 255))
            elif kind == "resp":
                # Silver
                draw.text((PAD_X, y), text, font=font_mono, fill=(192, 192, 192, 255))
            elif kind == "module_active":
                # Split text: module name in light grey, [ACTIVE] in pure white
                parts = text.split("[ACTIVE]")
                draw.text((PAD_X, y), parts[0], font=font_mono, fill=(170, 170, 170, 255))
                bbox = draw.textbbox((PAD_X, y), parts[0], font=font_mono)
                draw.text((bbox[2], y), "[ACTIVE]", font=font_bold, fill=(255, 255, 255, 255))
            elif kind == "module_learn":
                parts = text.split("[LEARNING]")
                draw.text((PAD_X, y), parts[0], font=font_mono, fill=(170, 170, 170, 255))
                bbox = draw.textbbox((PAD_X, y), parts[0], font=font_mono)
                draw.text((bbox[2], y), "[LEARNING]", font=font_mono, fill=(130, 130, 130, 255))
            elif kind == "status_online":
                draw.text((PAD_X, y), text, font=font_bold, fill=(255, 255, 255, 255))
                if cursor_visible:
                    bbox = draw.textbbox((PAD_X, y), text, font=font_bold)
                    cx = bbox[2] + 2
                    draw.rectangle([(cx, y + 2), (cx + 8, y + 15)], fill=(255, 255, 255, 255))
            
            y += LINE_HEIGHT
            
        rgb = img.convert("RGB")
        frame_quantized = rgb.quantize(colors=64, method=Image.Resampling.LANCZOS)
        frames.append(frame_quantized)
        durations.append(repeat_count * 70)
        
    for p in [os.path.join(ASSETS_DIR, "terminal.gif"), os.path.join(TRB_DIR, "terminal.gif")]:
        frames[0].save(p, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True)
    print(f"Saved terminal.gif ({os.path.getsize(p) / 1024:.1f} KB, {len(frames)} frames)")

# -------------------------------------------------------------
# 3. FOOTER WAVE (footer-wave.gif)
# -------------------------------------------------------------
def create_footer_wave():
    print("Generating footer-wave.gif...")
    WIDTH, HEIGHT = 840, 160
    font_gothic = get_font("impact", 36)
    font_mono = get_font("mono_bold", 13)
    font_spade = get_font("title", 20)
    
    t1 = "NO SIGNAL. JUST CODE."
    t2 = "TRB-89  /  SYSTEM ONLINE"
    
    # 36 frames loop
    NUM_FRAMES = 36
    frames = []
    
    for f in range(NUM_FRAMES):
        img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
        draw = ImageDraw.Draw(img)
        
        # 1. Subtle animated waveform / interference oscilloscope line
        # Center y for waveform ~ 100
        wave_y = 118
        points = []
        for x in range(30, WIDTH - 30, 4):
            # Complex harmonic interference
            phase = 2 * math.pi * f / NUM_FRAMES
            # Wave modulation: localized packet around center
            center_dist = abs(x - WIDTH / 2) / (WIDTH / 2)
            envelope = math.exp(- (center_dist ** 2) / 0.18)
            
            # Interference of two frequencies
            y_offset = (math.sin(x * 0.045 + phase) * 8.0 + math.cos(x * 0.09 - 2 * phase) * 5.0) * envelope
            points.append((x, wave_y + y_offset))
            
        # Draw waveform
        for idx in range(len(points) - 1):
            p1 = points[idx]
            p2 = points[idx + 1]
            # Color intensity based on displacement
            draw.line([p1, p2], fill=(180, 180, 180, 255), width=1)
            
        # Subtle horizontal reference rail
        draw.line([(30, wave_y), (WIDTH - 30, wave_y)], fill=(30, 30, 30, 255), width=1)
        
        # 2. Main Gothic Text
        bbox1 = draw.textbbox((0, 0), t1, font=font_gothic)
        w1 = bbox1[2] - bbox1[0]
        x1 = (WIDTH - w1) // 2
        y1 = 18
        
        # Periodic interference flicker
        is_glitch = (f == 7 or f == 25)
        text_color = (255, 255, 255, 255)
        if is_glitch:
            draw.text((x1 + 3, y1), t1, font=font_gothic, fill=(120, 120, 120, 255))
            draw.text((x1 - 2, y1), t1, font=font_gothic, fill=(255, 255, 255, 255))
        else:
            draw.text((x1, y1), t1, font=font_gothic, fill=text_color)
            
        # 3. Subtext
        bbox2 = draw.textbbox((0, 0), t2, font=font_mono)
        w2 = bbox2[2] - bbox2[0]
        x2 = (WIDTH - w2) // 2
        y2 = y1 + 45
        draw.text((x2, y2), t2, font=font_mono, fill=(160, 160, 160, 255))
        
        # 4. Small monochrome spade symbol
        spade_sym = "♠"
        bbox_s = draw.textbbox((0, 0), spade_sym, font=font_spade)
        ws = bbox_s[2] - bbox_s[0]
        xs = (WIDTH - ws) // 2
        ys = y2 + 22
        draw.text((xs, ys), spade_sym, font=font_spade, fill=(220, 220, 220, 255))
        
        rgb = img.convert("RGB")
        frames.append(rgb.quantize(colors=64, method=Image.Resampling.LANCZOS))
        
    for p in [os.path.join(ASSETS_DIR, "footer-wave.gif"), os.path.join(TRB_DIR, "footer-wave.gif")]:
        frames[0].save(p, save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)
    print(f"Saved footer-wave.gif ({os.path.getsize(p) / 1024:.1f} KB)")

# -------------------------------------------------------------
# 4. CHROME DIVIDER (chrome-divider.svg)
# -------------------------------------------------------------
def create_chrome_divider():
    print("Generating chrome-divider.svg...")
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 32" width="100%" height="32" fill="none">
  <defs>
    <!-- Liquid Chrome Linear Gradient -->
    <linearGradient id="chromeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="20%" stop-color="#262626"/>
      <stop offset="40%" stop-color="#8a8a8a"/>
      <stop offset="50%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#8a8a8a"/>
      <stop offset="80%" stop-color="#262626"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </linearGradient>

    <!-- Animated Light Sheen Sweep -->
    <linearGradient id="sheenGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
      <animate attributeName="x1" from="-100%" to="200%" dur="4s" repeatCount="indefinite" />
      <animate attributeName="x2" from="0%" to="300%" dur="4s" repeatCount="indefinite" />
    </linearGradient>
  </defs>

  <!-- Background Base Hairline -->
  <line x1="40" y1="16" x2="860" y2="16" stroke="url(#chromeGrad)" stroke-width="1.2"/>
  
  <!-- Animated Sheen Overlay -->
  <line x1="40" y1="16" x2="860" y2="16" stroke="url(#sheenGrad)" stroke-width="1.5"/>

  <!-- Brutalist Centerpiece Accent -->
  <g transform="translate(450, 16)">
    <!-- Outer Diamond / Spade Rhombus -->
    <polygon points="0,-9 9,0 0,9 -9,0" fill="#090909" stroke="#C0C0C0" stroke-width="1.2"/>
    <!-- Inner Solid Chrome Core -->
    <polygon points="0,-4 4,0 0,4 -4,0" fill="#FFFFFF"/>
    <!-- Flanking Technical Marks -->
    <line x1="-22" y1="-3" x2="-22" y2="3" stroke="#888888" stroke-width="1"/>
    <line x1="22" y1="-3" x2="22" y2="3" stroke="#888888" stroke-width="1"/>
    <circle cx="-35" cy="0" r="1.5" fill="#444444"/>
    <circle cx="35" cy="0" r="1.5" fill="#444444"/>
  </g>
</svg>"""
    for p in [os.path.join(ASSETS_DIR, "chrome-divider.svg"), os.path.join(TRB_DIR, "chrome-divider.svg")]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(svg_content)
    print("Saved chrome-divider.svg")

if __name__ == "__main__":
    create_glitch_heading()
    create_terminal_gif()
    create_footer_wave()
    create_chrome_divider()
