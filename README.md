# Product Creative Generator - 100 Automated Images

Automated generation of 100 unique, high-converting product advertisement creatives using Stable Diffusion WebUI. Optimized for Instagram ads, Amazon product listings, and e-commerce marketing.

## Features

✨ **100 Unique Designs** - Automatically generated across 6 aesthetic categories
🎯 **Ad-Ready Output** - 1080x1080px Instagram Post format
⚡ **Fast Generation** - Generates all 100 images in 30-45 minutes
🎨 **Diverse Styles** - Luxury, Minimal, Cinematic, Neon, Lifestyle, Macro
🔄 **Batch Processing** - Optimized for high-volume production
📊 **Product-Consistent** - Uses seed variation for unique layouts while maintaining product accuracy

## Products

- **KASHMIRI GOLD Black Pearl Supari** (Black Pearl/Black Current mouth freshener)
- Premium soft supari from Kashmir
- Ideal for product photography and marketing automation

## Prerequisites

### System Requirements
- Python 3.8+
- Stable Diffusion WebUI (running locally)
- 8GB+ VRAM (GPU recommended for fast generation)
- ~2GB disk space for 100 images

### Python Dependencies
```bash
pip install requests pillow
```

### Stable Diffusion Setup
1. Clone or download [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
2. Install dependencies and models
3. Start with API enabled:
   ```bash
   python launch.py --api
   ```
4. Default API runs on: `http://127.0.0.1:7860`

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/pranaynaresh2007-web/product-creative-generator.git
cd product-creative-generator
```

### 2. Ensure Stable Diffusion is Running
```bash
# In another terminal, start SD WebUI with API
python launch.py --api
```

### 3. Run Generation Script
```bash
python generate_creatives.py
```

### 4. Monitor Progress
The script will output:
- Real-time generation status
- Progress percentage
- Estimated time remaining
- Output file paths

### 5. Access Generated Images
```
output_creatives/
├── creative_001.png
├── creative_002.png
├── ...
└── creative_100.png
```

## Output Structure

**Directory:** `output_creatives/`
**Format:** PNG (1080x1080px)
**Naming:** `creative_[001-100].png`
**Total:** 100 images

### Categories Distribution
- **Luxury & Premium** (15 images) - Black & gold, premium aesthetics
- **Minimal & Clean** (15 images) - White backgrounds, modern design
- **Dark Cinematic** (15 images) - Dramatic lighting, moody atmosphere
- **Neon & Gen Z** (15 images) - Vibrant gradients, trendy styles
- **Lifestyle & Usage** (15 images) - Real-world scenarios
- **Macro & Floating** (25 images) - Close-ups and product shots

## Customization

### Adjust API Endpoint
Edit `generate_creatives.py`:
```python
api_url="http://YOUR_IP:7860"  # Change if SD WebUI on different IP
```

### Change Output Directory
```python
output_dir="your_custom_directory"
```

### Modify Prompt Categories
Edit the `prompts` dictionary in the script to customize descriptions.

### Adjust Image Quality
```python
steps=25  # Higher = better quality but slower (25-50 recommended)
cfg_scale=7.5  # Prompt adherence (7-9 recommended)
```

## Advanced Options

### API Parameters
- `steps`: 20-50 (default: 25)
- `cfg_scale`: 5-15 (default: 7.5)
- `sampler`: DPM++, Euler, Heun, etc.
- `seed`: -1 (random), or fixed value for reproducibility

### Batch Processing
To generate in multiple batches:
```python
generator = ProductCreativeGenerator()
generator.generate_images(num_images=50)  # First batch
generator.generate_images(num_images=50, starting_index=50)  # Second batch
```

## Troubleshooting

### "Connection refused" error
- Ensure Stable Diffusion WebUI is running
- Check API is enabled: `python launch.py --api`
- Verify port 7860 is accessible

### Out of memory errors
- Reduce batch size (already optimized to 1 image at a time)
- Lower `steps` parameter
- Close other GPU-intensive applications

### Low quality outputs
- Increase `steps` (25 → 40)
- Adjust `cfg_scale` (7.5 → 8.5)
- Use better model (e.g., SD 1.5, SDXL)

### Slow generation
- Use GPU instead of CPU
- Reduce image resolution (1080 → 768)
- Enable optimization flags in SD WebUI

## Performance Metrics

**Typical Generation Times** (with RTX 3080 / A100):
- 1 image: 8-15 seconds
- 10 images: 90-150 seconds
- 100 images: 15-30 minutes

**Storage Requirements**:
- ~15-20MB per image
- 100 images ≈ 1.5-2GB

## File Structure

```
product-creative-generator/
├── README.md                 # This file
├── generate_creatives.py     # Main generation script
├── requirements.txt          # Python dependencies
├── config.json              # Configuration (optional)
└── output_creatives/        # Generated images
    ├── creative_001.png
    ├── creative_002.png
    └── ...
```

## API Configuration

**Default Stable Diffusion WebUI API:**
- URL: `http://127.0.0.1:7860`
- Endpoint: `/api/txt2img`
- Method: POST
- Content-Type: application/json

## License

MIT License - Free for commercial and personal use

## Support

- **Issues**: GitHub Issues
- **Documentation**: See README.md
- **Examples**: Check output_creatives/ folder after first run

## Contributing

Contributions welcome! Feel free to:
- Improve prompt quality
- Optimize generation speed
- Add new aesthetic categories
- Enhance documentation

## Changelog

### v1.0 (Initial Release)
- 100 unique prompts across 6 categories
- Batch generation with progress tracking
- PNG export with sequential naming
- Error handling and logging

---

**Status:** Production Ready ✅
**Last Updated:** March 20, 2026
**Generator:** AI Creative Automation System
