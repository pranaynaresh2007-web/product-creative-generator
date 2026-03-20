#!/usr/bin/env python3
# Product Creative Generator - 100 Automated Images
# Generates unique product advertisements using Stable Diffusion WebUI API
# For KASHMIRI GOLD Black Pearl Supari

import requests
import json
import time
import os
import base64
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO

class ProductCreativeGenerator:
    """Generate 100 unique product creatives using Stable Diffusion WebUI"""
    
    def __init__(self, api_url="http://127.0.0.1:7860", output_dir="output_creatives"):
        self.api_url = api_url
        self.output_dir = output_dir
        self.txt2img_endpoint = f"{api_url}/api/txt2img"
        Path(self.output_dir).mkdir(exist_ok=True)
        
    prompts = [
        # LUXURY & PREMIUM (15 images)
        "Ultra premium black pearl supari on dark luxury background, gold accents, professional product photography, 4K, studio lighting",
        "Kashmiri Black Pearl supari mouth freshener, black packaging, luxury aesthetic, black and gold gradient background, Instagram ad",
        "Black pearl supari premium product shot, soft golden bokeh background, cinematic lighting, commercial photography, 4K",
        "Luxury black pearl supari pouch displayed on black marble surface, gold leaf accents, dramatic studio lighting",
        "Premium Kashmiri supari, dark moody background, luxury minimalist composition, soft rim lighting, professional product shoot",
        "Black pearl supari with gold foil packaging, dark backdrop, luxury premium feel, studio photography, sharp focus",
        "High-end black pearl supari advertisement, black velvet background, golden highlights, luxury branding, Instagram aesthetic",
        "Black pearl supari luxury shot, product centered, dark sophisticated background, professional lighting setup",
        "Premium mouth freshener supari, black packaging, elegant composition, gold accents, luxury lifestyle photography",
        "Kashmiri supari black pearl variant, dark luxury setting, premium product display, dramatic shadows",
        "Ultra luxury black pearl supari, dark monochromatic background, gold leaf details, premium aesthetic, studio quality",
        "Black pearl supari premium presentation, luxury dark background, professional photography, commercial ad quality",
        "Luxury supari product shot, dark background with gold particles, premium feel, Instagram ad ready",
        "Black pearl supari deluxe packaging, luxury dark setting, professional lighting, premium product photography",
        "Premium black pearl supari, dark luxury backdrop, gold accents, commercial photography quality",
        
        # MINIMAL & CLEAN (15 images)
        "Black pearl supari on clean white background, minimal composition, soft natural lighting, product focused",
        "Supari black pearl, pure white background, minimalist flat lay, professional product shot, sharp focus",
        "Clean minimal product photography of black pearl supari, white background, product centered, soft lighting",
        "Black pearl supari minimalist style, white studio background, simple composition, professional product photo",
        "Minimal black pearl supari shot, bright white background, clean aesthetic, professional product photography",
        "Supari black pearl flat lay, clean white background, minimalist design, product photography style",
        "Clean product shot black pearl supari, white background, minimal elements, professional photography",
        "Minimalist black pearl supari, bright white backdrop, product focused, studio photography, sharp focus",
        "Simple elegant black pearl supari shot, white background, minimal composition, professional product photo",
        "Black pearl supari minimal presentation, clean white background, professional photography, commercial quality",
        "Ultra clean black pearl supari product shot, white background, minimalist style, professional lighting",
        "Minimal black pearl supari on white, flat lay style, product photography, clean aesthetic",
        "Clean minimal black pearl supari advertisement, white background, professional product shot",
        "Supari black pearl minimalist presentation, white studio background, product focused, professional shot",
        "Clean aesthetic black pearl supari, white background, simple elegant composition, product photography",
        
        # NEON & GEN Z (15 images)
        "Black pearl supari neon aesthetic, vibrant neon pink and blue gradient background, Gen Z style, trendy product shot",
        "Supari black pearl with neon glow effect, electric blue and pink background, trendy Instagram ad, bold colors",
        "Black pearl supari neon advertisement, vibrant gradient background neon colors, Gen Z aesthetic",
        "Supari product shot with neon lights, colorful holographic background, trendy vibrant style, Instagram ready",
        "Black pearl supari Gen Z trendy shot, neon gradient background, bold vibrant colors, modern product ad",
        "Neon aesthetic black pearl supari, electric pink blue purple gradient, trendy product photography, Instagram style",
        "Vibrant neon black pearl supari ad, colorful glowing background, Gen Z style, trendy modern product shot",
        "Black pearl supari with neon glow, vibrant trendy background, bold colors, Instagram ad style",
        "Gen Z trendy black pearl supari, neon lights effect, vibrant gradient background, modern product photography",
        "Neon black pearl supari product shot, electric colorful background, trendy vibrant aesthetic, Instagram ready",
        "Vibrant neon supari black pearl, bold gradient neon colors, Gen Z style ad, trendy product photo",
        "Black pearl supari glowing neon effect, vibrant pink blue gradient, trendy product ad, Instagram aesthetic",
        "Trendy neon black pearl supari shot, vibrant colorful background, Gen Z modern style, product advertisement",
        "Supari black pearl with neon lights, electric vibrant gradient, trendy Instagram ad, bold colors",
        "Gen Z neon aesthetic black pearl supari, vibrant glowing background, trendy product shot, modern ad style",
        
        # DARK CINEMATIC (15 images)
        "Black pearl supari dark cinematic shot, moody dramatic lighting, dark background, professional cinema photography",
        "Supari black pearl cinematic lighting, dramatic shadows, dark atmospheric background, professional product shot",
        "Black pearl supari dark moody aesthetic, cinematic dramatic shadows, professional photography, dark background",
        "Cinematic dark black pearl supari, dramatic rim lighting, dark atmospheric setting, professional product photo",
        "Dark cinematic black pearl supari shot, moody lighting, dramatic shadows, professional product photography",
        "Supari black pearl cinematic style, dark atmospheric background, dramatic professional lighting",
        "Black pearl supari dark drama aesthetic, cinematic lighting setup, dramatic shadows, professional shot",
        "Cinematic black pearl supari, moody dark background, professional dramatic lighting, product advertisement",
        "Dark moody black pearl supari shot, cinematic lighting effect, dramatic shadows, professional photography",
        "Black pearl supari cinematic presentation, dark atmospheric background, professional dramatic lighting",
        "Dramatic dark cinematic supari shot, professional lighting setup, moody atmosphere, product focused",
        "Black pearl supari dark cinema aesthetic, dramatic lighting, professional photography, cinematic quality",
        "Cinematic dark black pearl supari ad, moody atmospheric lighting, professional product shot",
        "Dark supari black pearl cinematic style, dramatic professional lighting, moody background",
        "Black pearl supari dramatic dark shot, cinematic lighting effect, professional product photography",
        
        # LIFESTYLE & USAGE (15 images)
        "Black pearl supari in elegant bowl, lifestyle photography, person enjoying mouth freshener, warm natural lighting",
        "Supari black pearl lifestyle shot, social gathering setting, festive mood, warm lighting, product in use",
        "Black pearl supari lifestyle photography, elegant serving, social occasion setting, warm natural lighting",
        "Lifestyle image black pearl supari, being enjoyed at party gathering, warm ambient lighting",
        "Supari black pearl in elegant presentation, lifestyle setting, social gathering context, warm lighting",
        "Black pearl supari lifestyle advertisement, person enjoying, festive setting, warm natural lighting",
        "Lifestyle black pearl supari shot, elegant serving style, social occasion, warm professional lighting",
        "Supari black pearl lifestyle photography, celebration setting, warm ambient lighting, product in context",
        "Black pearl supari being enjoyed, lifestyle moment, social gathering, warm natural lighting, product photo",
        "Lifestyle advertisement black pearl supari, elegant presentation, celebration setting, warm lighting",
        "Supari black pearl lifestyle image, being used at gathering, warm ambient setting, professional shot",
        "Black pearl supari lifestyle photography, festive occasion, people enjoying, warm lighting",
        "Lifestyle black pearl supari shot, elegant serving, social moment, warm professional lighting",
        "Supari black pearl being enjoyed, lifestyle advertisement, celebration setting, warm lighting",
        "Black pearl supari lifestyle context, elegant presentation, social gathering, warm natural lighting",
        
        # CLOSE-UP MACRO (10 images)
        "Extreme close-up black pearl supari, macro photography, detailed texture, professional lighting",
        "Black pearl supari macro shot, extreme close-up detail, professional macro photography, high resolution",
        "Macro close-up black pearl supari, detailed texture photography, professional macro lighting",
        "Black pearl supari extreme macro shot, detailed close-up photography, professional setup",
        "Close-up macro black pearl supari, extreme detail photography, professional macro shot",
        "Supari black pearl macro photography, extreme close-up, detailed texture, professional macro setup",
        "Macro black pearl supari shot, extreme close-up detail, professional photography",
        "Black pearl supari detailed macro, extreme close-up photography, professional macro lighting",
        "Extreme macro supari black pearl, detailed close-up shot, professional macro photography",
        "Black pearl supari macro detail shot, extreme close-up, professional macro photography",
        
        # FLOATING PRODUCT SHOT (15 images)
        "Black pearl supari floating product shot, levitating mid-air, professional product photography",
        "Supari black pearl floating advertisement, suspended in air, professional product shot",
        "Black pearl supari levitating product photo, floating mid-air, professional product advertisement",
        "Floating black pearl supari shot, suspension product photography, professional product ad",
        "Supari black pearl floating levitating, professional product shot, suspended in air",
        "Black pearl supari suspended floating, levitating product photography, professional shot",
        "Levitating black pearl supari product shot, floating mid-air, professional product photo",
        "Black pearl supari floating suspension, professional product advertisement, suspended shot",
        "Supari black pearl levitating, floating product shot, professional product photography",
        "Black pearl supari floating mid-air, suspended levitating shot, professional product ad",
        "Floating levitating black pearl supari, professional product photography, suspended mid-air",
        "Supari black pearl suspension product shot, floating mid-air, professional product photo",
        "Black pearl supari levitating advertisement, floating product shot, professional photography",
        "Floating black pearl supari suspended, professional product shot, levitating mid-air",
        "Supari black pearl floating professional, levitating product shot, suspended in air",
    ]
    
    def generate_images(self, num_images=100, steps=25, cfg_scale=7.5):
        """Generate images using Stable Diffusion API"""
        
        print(f"\n{'='*70}")
        print(f"STARTING 100 PRODUCT CREATIVE GENERATION")
        print(f"{'='*70}\n")
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        for idx, prompt in enumerate(self.prompts[:num_images], 1):
            try:
                print(f"[{idx}/100] Generating: {prompt[:50]}...")
                
                payload = {
                    "prompt": prompt,
                    "negative_prompt": "blurry, low quality, distorted product, watermark, bad anatomy, extra objects",
                    "steps": steps,
                    "cfg_scale": cfg_scale,
                    "width": 1080,
                    "height": 1080,
                    "sampler_name": "DPM++ 2M Karras",
                    "seed": -1,
                }
                
                response = requests.post(self.txt2img_endpoint, json=payload, timeout=300)
                
                if response.status_code == 200:
                    result = response.json()
                    images = result.get('images', [])
                    
                    if images:
                        image_data = base64.b64decode(images[0])
                        image = Image.open(BytesIO(image_data))
                        filename = f"{self.output_dir}/creative_{idx:03d}.png"
                        image.save(filename)
                        successful += 1
                        print(f"   OK: {filename}")
                    else:
                        failed += 1
                        print(f"   ERROR: No image returned")
                else:
                    failed += 1
                    print(f"   ERROR: API returned {response.status_code}")
                    
            except Exception as e:
                failed += 1
                print(f"   ERROR: {str(e)}")
            
            if idx % 25 == 0:
                elapsed = time.time() - start_time
                rate = idx / elapsed if elapsed > 0 else 0
                remaining = (100 - idx) / rate if rate > 0 else 0
                print(f"\n[PROGRESS] {idx}/100 | Success: {successful} | ETA: {remaining:.0f}s\n")
        
        elapsed_time = time.time() - start_time
        print(f"\n{'='*70}")
        print(f"GENERATION COMPLETE")
        print(f"{'='*70}")
        print(f"Total: {successful}/100 generated successfully")
        print(f"Failed: {failed}")
        print(f"Time: {elapsed_time:.1f}s ({elapsed_time/60:.1f} minutes)")
        print(f"Output: {os.path.abspath(self.output_dir)}")
        print(f"{'='*70}\n")

if __name__ == "__main__":
    generator = ProductCreativeGenerator()
    generator.generate_images(num_images=100, steps=25, cfg_scale=7.5)
