import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Directories
WORKSPACE = r"c:\Users\TRB\modified mindspace sdg\CrediAI\GIT-PROFILE"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")
TRB_DIR = os.path.join(WORKSPACE, "trb-89", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(TRB_DIR, exist_ok=True)

SPADE_SOURCE = r"C:\Users\TRB\.gemini\antigravity-ide\brain\80a2ef88-3eba-4f87-91e1-5a7807cf0593\chrome_spade_base_1792587952022.jpg"

def create_chrome_spade_banner():
    print("Generating chrome-spade.gif (3:1 cinematic banner)...")
    base_img = Image.open(SPADE_SOURCE).convert("RGBA")
    
    # 3:1 banner: 840 x 280
    WIDTH, HEIGHT = 840, 280
    SPADE_SIZE = 224
    
    # Resize base spade to fit height
    spade_resized = base_img.resize((SPADE_SIZE, SPADE_SIZE), Image.Resampling.LANCZOS)
    
    # We will generate 36 frames for a smooth 4.0 second seamless loop (duration=110ms)
    NUM_FRAMES = 36
    frames = []
    
    for i in range(NUM_FRAMES):
        t = i / NUM_FRAMES
        # Banner canvas: pure black
        banner = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
        
        # 1. 3D Yaw Rotation Simulation:
        # Smooth sinusoidal yaw rotation: max yaw +/- 18 degrees
        yaw_rad = math.sin(2 * math.pi * t) * math.radians(18)
        scale_x = math.cos(yaw_rad)
        
        cur_w = max(int(SPADE_SIZE * abs(scale_x)), 10)
        cur_h = SPADE_SIZE
        
        # Scale horizontally to simulate 3D rotation
        cur_spade = spade_resized.resize((cur_w, cur_h), Image.Resampling.LANCZOS)
        
        # 2. Chrome Specular Light Sweep:
        # A moving metallic specular highlight moving across the spade in sync
        sweep_x = (math.sin(2 * math.pi * t) + 1.0) / 2.0  # 0 to 1
        
        # Create specular overlay on cur_spade
        spade_np = np.array(cur_spade, dtype=np.float32)
        
        # Generate light gradient for this frame
        xx = np.linspace(0, 1, cur_w)
        band_center = sweep_x
        light_band = np.exp(-((xx - band_center) ** 2) / (2 * (0.10 ** 2)))
        light_band = light_band.reshape(1, cur_w, 1)
        
        # Enhance RGB where light band is active
        for c in range(3):
            boost = light_band[:, :, 0] * 75.0
            spade_np[:, :, c] = np.clip(spade_np[:, :, c] + boost * (spade_np[:, :, c] / 255.0), 0, 255)
            
        cur_spade_lighted = Image.fromarray(spade_np.astype(np.uint8), mode="RGBA")
        
        # 3. Position centered with subtle vertical hover
        hover_y = int(4.0 * math.sin(2 * math.pi * t))
        pos_x = (WIDTH - cur_w) // 2
        pos_y = (HEIGHT - cur_h) // 2 + hover_y
        
        # Subtle horizontal laser / chrome reflection line behind spade
        draw = ImageDraw.Draw(banner)
        # Background subtle ambient obsidian grid lines
        for gx in range(0, WIDTH, 70):
            draw.line([(gx, 0), (gx, HEIGHT)], fill=(12, 12, 12, 255), width=1)
        for gy in range(0, HEIGHT, 70):
            draw.line([(0, gy), (WIDTH, gy)], fill=(12, 12, 12, 255), width=1)
            
        # Subtle central horizontal silver flare
        flare_w = 400
        flare_x1 = (WIDTH - flare_w) // 2
        flare_x2 = (WIDTH + flare_w) // 2
        draw.line([(flare_x1, HEIGHT // 2), (flare_x2, HEIGHT // 2)], fill=(28, 28, 28, 255), width=1)
        
        # Minimal brutalist corner brackets
        bracket_color = (60, 60, 60, 255)
        # Top-left
        draw.line([(20, 20), (50, 20)], fill=bracket_color, width=1)
        draw.line([(20, 20), (20, 50)], fill=bracket_color, width=1)
        # Top-right
        draw.line([(WIDTH - 50, 20), (WIDTH - 20, 20)], fill=bracket_color, width=1)
        draw.line([(WIDTH - 20, 20), (WIDTH - 20, 50)], fill=bracket_color, width=1)
        # Bottom-left
        draw.line([(20, HEIGHT - 20), (50, HEIGHT - 20)], fill=bracket_color, width=1)
        draw.line([(20, HEIGHT - 50), (20, HEIGHT - 20)], fill=bracket_color, width=1)
        # Bottom-right
        draw.line([(WIDTH - 50, HEIGHT - 20), (WIDTH - 20, HEIGHT - 20)], fill=bracket_color, width=1)
        draw.line([(WIDTH - 20, HEIGHT - 50), (WIDTH - 20, HEIGHT - 20)], fill=bracket_color, width=1)
        
        # Paste spade with blend
        banner.paste(cur_spade_lighted, (pos_x, pos_y), cur_spade_lighted)
        
        # Convert to RGB
        rgb_banner = banner.convert("RGB")
        # Quantize with adaptive palette for crisp GIF rendering
        frames.append(rgb_banner.quantize(colors=128, method=Image.Resampling.LANCZOS))
        
    out_path = os.path.join(ASSETS_DIR, "chrome-spade.gif")
    out_path_trb = os.path.join(TRB_DIR, "chrome-spade.gif")
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=110,
        loop=0,
        optimize=True
    )
    frames[0].save(
        out_path_trb,
        save_all=True,
        append_images=frames[1:],
        duration=110,
        loop=0,
        optimize=True
    )
    print(f"Saved {out_path} ({os.path.getsize(out_path) / 1024:.1f} KB)")

if __name__ == "__main__":
    create_chrome_spade_banner()
