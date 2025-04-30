# 🖼️ Simple Image Editor

A quick and easy Python script to batch-edit images with a touch of style!

## ✨ What It Does

This script:
- Sharpens the image
- Rotates it 90° counterclockwise
- Converts it to **black & white (grayscale)**
- Enhances the contrast
- Saves the edited image with a new name in a separate folder

Perfect for batch processing images for a specific aesthetic or project!

## 🛠 How to Use

1. **Install Pillow (if not already):**
```bash
pip install pillow
```

2. **Set Your Paths:**
- `path`: Folder with your original images
- `pathOut`: Folder where edited images will be saved

3. **Run the Script:**
```bash
python image_editor.py
```

Your edited images will appear in the `editedImgs/` folder with `_edited` added to their names.

## 🖼 Example Output

Original ➡️ `myphoto.jpg`  
Edited ➡️ `myphoto_edited.jpg`

## 📁 Folder Structure

```
Image_Editor/
├── imgs/         # original images
├── editedImgs/   # output images
└── image_editor.py
```

---

🎉 That’s it! Clean, contrasty, grayscale images with one script.
