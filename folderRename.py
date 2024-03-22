import os
from tkinter import Tk, filedialog
from PIL import Image, ImageDraw, ImageFont

def watermark_image(image_path, watermark_text):
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', 36)
        
        margin = 10
        x = img.width - 200
        y = img.height - 50
        
        # Draw semi-transparent rectangle
        draw.rectangle([x, y, img.width - margin, img.height - margin], fill=(0, 0, 0, 128))
        
        # Draw the watermark
        draw.text((x + margin, y), watermark_text, fill="white", font=font)
        
        # Save the watermarked image
        root, ext = os.path.splitext(image_path)
        watermarked_image_path = f"{root}_watermarked{ext}"
        img.save(watermarked_image_path)

def watermark_images_in_folder(folder_path):
    for item in os.listdir(folder_path):
        file_lower = item.lower()
        if file_lower.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, item)
            watermark_text = os.path.splitext(item)[0]
            watermark_image(image_path, watermark_text)
            print(f"Watermarked {image_path}")

def ask_folder():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


folder_path = ask_folder()
if folder_path:
    watermark_images_in_folder(folder_path)
    print("All images have been watermarked.")
else:
    print("No folder was selected.")
