import re
from PIL import Image

# 1. Create cool, vibrant reel thumbnail from reels-5 (Spiti Valley, stunning cinematic landscape 1920x1080)
im_reel = Image.open('/tmp/reels-5.mp4.png')
im_reel.save('work-section/slider_img_1.webp', 'WEBP', quality=95)
print("✅ Saved new Reels thumbnail from Spiti Valley 4K cinematic cut to work-section/slider_img_1.webp")

# 2. Update Image 2 thumbnail for Poster Collection (Taj Mahal / Neymar / Golden Temple)
im_posters = Image.open('projects/Itmatters/gallery/taj-mahal.webp')
# Make a 16:10 or 16:9 crop or high quality thumbnail for slide 2
w, h = im_posters.size
# Crop center to 16:10 for smooth slider display
target_h = int(w * 10 / 16)
if target_h < h:
    top = (h - target_h) // 2
    im_posters_cropped = im_posters.crop((0, top, w, top + target_h))
else:
    im_posters_cropped = im_posters
im_posters_cropped.save('work-section/slider_img_2.webp', 'WEBP', quality=95)
print("✅ Saved new Poster Collection thumbnail (Taj Mahal Marble Symphony) to work-section/slider_img_2.webp")

