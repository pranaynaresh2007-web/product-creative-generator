#!/usr/bin/env python3
# Product Creative Generator - 100 Automated Images (Enhanced with Image-to-Image)
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
import glob

class ProductCreativeGenerator:
    """Generate 100 unique product creatives using Stable Diffusion WebUI"""
    
    def __init__(self, api_url="http://127.0.0.1:7860", output_dir="output_creatives", input_image_dir="product_images"):
        self.api_url = api_url
        self.output_dir = output_dir
        self.input_image_dir = input_image_dir
        self.txt2img_endpoint = f"{api_url}/api/txt2img"
        self.img2img_endpoint = f"{api_url}/api/img2img"
        Path(self.output_dir).mkdir(exist_ok=True)
        
        # Style prompts for creative variations
        self.style_modifiers = [
            "luxury professional photography, gold accents, dark background",
            "minimalist clean product shot, white background, sharp focus",
            "dark cinematic lighting, dramatic shadows, moody atmosphere",
            "neon aesthetic, vibrant gradient background, Gen Z style",
            "lifestyle photography, social gathering, warm lighting",
            "extreme macro close-up, detailed texture, professional macro",
            "floating levitating product, suspended mid-air, professional shot",
        ]
        
        self.prompts = self._generate_prompts()
    
    def _generate_prompts(self):
        """Generate 100 unique prompts across different styles"""
        prompts = []
        base_descriptions = [
            "black pearl supari mouth freshener product",
            "kashmiri gold supari premium product",
            "black current supari gourmet food",
            "mouth freshener supari elegant packaging",
            "premium black pearl supari luxury product",
            "kashmiri supari black pearl variant authentic",
            "gourmet mouth freshener supari premium quality",
            "black pearl supari product display photography",
            "luxury supari mouth freshener black pearls",
            "premium kashmiri gold supari black pearl",
            "artisanal mouth freshener black pearl supari",
            "gourmet black pearl supari fresh product",
            "luxury mouth freshener supari black pearl",
            "premium kashmiri black pearl supari authentic",
            "professional product shot black pearl supari"
        ]
        
        for base_desc in base_descriptions:
            for style in self.style_modifiers:
                prompt = f"{base_desc}, {style}, professional photography, 4K, high quality"
                prompts.append(prompt)
                if len(prompts) >= 100:
                    return prompts[:100]
        
        return prompts[:100]
    
    def load_product_images(self):
        """Load product images from input directory"""
        image_files = glob.glob(f"{self.input_image_dir}/*.jpg") + glob.glob(f"{self.input_image_dir}/*.png")
        if not image_files:
            print(f"Warning: No product images found in {self.input_image_dir}/")
            print("Proceeding with text-to-image generation only...")
            return []
        return image_files
    
    def image_to_base64(self, image_path):
        """Convert image file to base64 encoding"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def generate_images(self, num_images=100, steps=25, cfg_scale=7.5, use_product_images=True):
        """Generate images using Stable Diffusion API"""
        
        print(f"\n{'='*70}")
        print(f"STARTING 100 PRODUCT CREATIVE GENERATION")
        print(f"{'='*70}\n")
        
        # Load product images if available
        product_images = []
        if use_product_images:
            product_images = self.load_product_images()
        
        successful = 0
        failed = 0
        start_time = time.time()
        
        for idx, prompt in enumerate(self.prompts[:num_images], 1):
            try:
                print(f"[{idx}/100] Generating: {prompt[:60]}...")
                
                # Decide whether to use img2img or txt2img
                # Cycle through product images if available
                use_img2img = use_product_images and len(product_images) > 0
                
                if use_img2img:
                    # Use image-to-image mode with product image as input
                    product_image = product_images[(idx - 1) % len(product_images)]
                    response = self._generate_img2img(prompt, product_image, steps, cfg_scale)
                else:
                    # Use text-to-image mode
                    response = self._generate_txt2img(prompt, steps, cfg_scale)
                
                if response and response.status_code == 200:
                    result = response.json()
                    images = result.get('images', [])
                    
                    if images:
                        image_data = base64.b64decode(images[0])
                        image = Image.open(BytesIO(image_data))
                        filename = f"{self.output_dir}/creative_{idx:03d}.png"
                        image.save(filename)
                        successful += 1
                        print(f" ✓ Saved: {filename}")
                    else:
                        failed += 1
                        print(f" ✗ No image returned")
                else:
                    failed += 1
                    status_code = response.status_code if response else "No response"
                    print(f" ✗ API Error: {status_code}")
                
                # Progress update every 25 images
                if idx % 25 == 0:
                    elapsed = time.time() - start_time
                    rate = idx / elapsed if elapsed > 0 else 0
                    remaining = (100 - idx) / rate if rate > 0 else 0
                    print(f"\n[PROGRESS] {idx}/100 | Success: {successful} | ETA: {remaining:.0f}s\n")
            
            except Exception as e:
                failed += 1
                print(f" ✗ Error: {str(e)}")
        
        elapsed_time = time.time() - start_time
        print(f"\n{'='*70}")
        print(f"GENERATION COMPLETE")
        print(f"{'='*70}")
        print(f"Total: {successful}/100 generated successfully")
        print(f"Failed: {failed}")
        print(f"Time: {elapsed_time:.1f}s ({elapsed_time/60:.1f} minutes)")
        print(f"Output: {os.path.abspath(self.output_dir)}")
        print(f"{'='*70}\n")
    
    def _generate_txt2img(self, prompt, steps, cfg_scale):
        """Generate image from text prompt"""
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
        
        try:
            return requests.post(self.txt2img_endpoint, json=payload, timeout=300)
        except Exception as e:
            print(f" ✗ Request error: {str(e)}")
            return None
    
    def _generate_img2img(self, prompt, input_image_path, steps, cfg_scale, denoising_strength=0.7):
        """Generate image from text prompt and input image (image-to-image)"""
        try:
            image_base64 = self.image_to_base64(input_image_path)
            
            payload = {
                "init_images": [image_base64],
                "prompt": prompt,
                "negative_prompt": "blurry, low quality, distorted, watermark, extra objects",
                "steps": steps,
                "cfg_scale": cfg_scale,
                "denoising_strength": denoising_strength,
                "width": 1080,
                "height": 1080,
                "sampler_name": "DPM++ 2M Karras",
                "seed": -1,
            }
            
            return requests.post(self.img2img_endpoint, json=payload, timeout=300)
        except Exception as e:
            print(f" ✗ Image-to-image error: {str(e)}")
            return None

if __name__ == "__main__":
    generator = ProductCreativeGenerator()
    
    # Check if product images are available
    product_images = generator.load_product_images()
    use_img2img = len(product_images) > 0
    
    if use_img2img:
        print(f"\n✓ Found {len(product_images)} product image(s)")
        print(f"Using image-to-image generation mode...\n")
    else:
        print(f"\n✓ Product images not found")
        print(f"Using text-to-image generation mode...\n")
    
    generator.generate_images(num_images=100, steps=25, cfg_scale=7.5, use_product_images=use_img2img)
