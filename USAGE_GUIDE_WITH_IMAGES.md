# How to Run Product Creative Generator with Your Product Images

## 🎯 Quick Start with Product Images

The **enhanced version** of Product Creative Generator now supports **image-to-image generation**, allowing you to use your actual Kashmiri Gold Black Pearl Supari product images as input to generate 100 creative variations!

## 📋 Step-by-Step Instructions

### **Step 1: Prepare Your Product Images**

1. Create a folder named `product_images` in your project directory
2. Download or copy your Kashmiri Gold Black Pearl Supari product images to this folder
3. Supported formats: **JPG** or **PNG**
4. Recommended image size: **1080x1080px** (optimal for Instagram)

**Folder structure:**
```
product-creative-generator/
├── product_images/              # Create this folder
│   ├── supari_image_1.jpg       # Your product images
│   ├── supari_image_2.png
│   └── supari_image_3.jpg
├── generate_creatives.py
├── config.json
├── requirements.txt
└── README.md
```

### **Step 2: Set Up Environment**

```bash
# Clone the repository (if not done)
git clone https://github.com/pranaynaresh2007-web/product-creative-generator.git
cd product-creative-generator

# Install dependencies
pip install requests pillow
```

### **Step 3: Start Stable Diffusion WebUI**

Open a terminal and start Stable Diffusion with API enabled:
```bash
# Navigate to your Stable Diffusion WebUI directory
cd path/to/stable-diffusion-webui

# Start with API
python launch.py --api
```

You should see: `Uvicorn running on http://127.0.0.1:7860`

### **Step 4: Run the Generator with Product Images**

In a **new terminal window**, navigate to the project directory and run:

```bash
python generate_creatives.py
```

**The script will:**
- ✓ Automatically detect product images in `product_images/` folder
- ✓ Use **image-to-image mode** (if images found)
- ✓ Generate 100 creative variations using your product images as reference
- ✓ Apply different styles to each variation
- ✓ Save all images to `output_creatives/` folder

### **Step 5: Access Your Generated Images**

All 100 creative images will be in `output_creatives/`:
```
output_creatives/
├── creative_001.png   # Luxury style
├── creative_002.png   # Minimal style
├── creative_003.png   # Cinematic style
├── creative_004.png   # Neon/Gen Z style
├── creative_005.png   # Lifestyle style
├── creative_006.png   # Macro style
├── creative_007.png   # Floating style
└── ... (100 images total)
```

---

## 🎨 How Image-to-Image Works

The enhanced script uses **two modes**:

### **Mode 1: Image-to-Image (When Product Images Exist)**
- Takes your Kashmiri Gold Black Pearl Supari product image
- Uses AI to apply creative styles while preserving product structure
- Cycles through your product images if multiple ones exist
- **More consistent** product appearance across all variations
- **Better quality** results with your specific product

### **Mode 2: Text-to-Image (Fallback)**
- If no product images found, uses pure text-to-image generation
- Based on descriptive prompts about the product
- Still produces excellent quality 100 images

---

## 📊 Generation Styles Applied

The generator applies **7 different aesthetic styles**:

1. **Luxury & Premium** - Black & gold accents, dark sophisticated backgrounds
2. **Minimal & Clean** - White backgrounds, minimalist composition
3. **Dark Cinematic** - Dramatic lighting, moody atmosphere
4. **Neon & Gen Z** - Vibrant gradients, trendy modern style
5. **Lifestyle** - Social gathering scenarios, real-world usage
6. **Macro** - Extreme close-ups showing product detail
7. **Floating** - Levitating product, suspended shots

**Total Variations:** 15 images per style × 6-7 styles = **100 unique images**

---

## ⚙️ Customization Options

### **Adjust Denoising Strength (Image-to-Image)**
The denoising strength controls how much the AI changes your image (0-1):
- **0.5**: Keep more of original image
- **0.7**: Balanced (default)
- **0.9**: More creative transformations

Edit `generate_creatives.py`, line in `_generate_img2img()` method:
```python
denoising_strength = 0.7  # Adjust this value
```

### **Change Output Directory**
Edit the first parameter when initializing:
```python
generator = ProductCreativeGenerator(
    api_url="http://127.0.0.1:7860",
    output_dir="my_creatives",  # Change this
    input_image_dir="product_images"
)
```

### **Adjust Quality Settings**
```python
generator.generate_images(
    num_images=100,
    steps=25,         # Higher = better quality (25-50 recommended)
    cfg_scale=7.5,    # Prompt adherence (7-9 recommended)
    use_product_images=True  # Use image-to-image mode
)
```

---

## 📈 Expected Results

**Generation Time:**
- With GPU (RTX 3080): ~25-30 minutes for 100 images
- With GPU (RTX 2080): ~45-60 minutes
- With GPU (RTX 3060): ~60-90 minutes
- CPU only: Not recommended (very slow)

**Output Quality:**
- **Resolution:** 1080x1080px (Instagram ready)
- **Format:** PNG (transparent background support)
- **Size:** ~15-20MB per image
- **Total:** ~1.5-2GB for all 100 images

---

## ✅ Troubleshooting

### **"Product images not found" message**
- Make sure folder is named exactly `product_images/`
- Check images are .jpg or .png format
- Verify images exist in the correct location

### **"Connection refused" error**
- Ensure Stable Diffusion WebUI is running
- Check API is enabled: `python launch.py --api`
- Verify port 7860 is accessible

### **Out of memory error**
- Close other GPU applications
- Reduce `steps` parameter (20 instead of 25)
- Reduce image size (768 instead of 1080)

### **Low quality outputs**
- Increase `steps` (40 instead of 25)
- Adjust `cfg_scale` (8.5 instead of 7.5)
- Use better Stable Diffusion model (SDXL)

---

## 🎁 Benefits of Image-to-Image Mode

✓ **Product Consistency** - Your product always visible in creations
✓ **Style Variety** - 100 different creative treatments
✓ **Time Saving** - Automated 100 image generation
✓ **Ready to Use** - Instagram and e-commerce ready
✓ **Cost Effective** - No paid AI services needed
✓ **Scalable** - Easily generate more variations

---

## 🚀 Use Cases

- **Instagram Ads** - Test which creative style performs best
- **Amazon Listings** - Multiple product images for A/B testing
- **Email Marketing** - Different variations for campaigns
- **Social Media** - Pinterest, Facebook, TikTok content
- **Landing Pages** - Hero images with product focus
- **Product Catalog** - Professional product photography alternatives

---

## 📝 Example Command Output

```
======================================================================
STARTING 100 PRODUCT CREATIVE GENERATION
======================================================================

✓ Found 3 product image(s)
Using image-to-image generation mode...

[1/100] Generating: black pearl supari mouth freshener product, luxury...
 ✓ Saved: output_creatives/creative_001.png
[2/100] Generating: black pearl supari mouth freshener product, minimal...
 ✓ Saved: output_creatives/creative_002.png
...
[25/100] Generating: kashmiri gold supari premium product, neon aesthetic...
 ✓ Saved: output_creatives/creative_025.png

[PROGRESS] 25/100 | Success: 25 | ETA: 450s

[50/100] Generating: black current supari gourmet food, dark cinematic...
 ✓ Saved: output_creatives/creative_050.png

...
[100/100] Generating: premium kashmiri supari black pearl authentic...
 ✓ Saved: output_creatives/creative_100.png

======================================================================
GENERATION COMPLETE
======================================================================
Total: 100/100 generated successfully
Failed: 0
Time: 1320.5s (22.0 minutes)
Output: /path/to/output_creatives
======================================================================
```

---

## 📞 Support & Questions

- Check `README.md` for general information
- Review `config.json` for available settings
- See `generate_creatives.py` comments for technical details

**Happy generating! 🎉**
