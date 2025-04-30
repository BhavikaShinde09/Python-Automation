# 📂 Auto File Organizer

Automatically organize your Downloads folder by sorting files into categorized subfolders in real time! 🧹✨

## 🔍 What It Does

This Python script watches your `Downloads` folder and **moves files** into categorized folders based on their file types:

| File Type       | Folder       |
|-----------------|--------------|
| Images          | `Images/`    |
| Videos          | `Videos/`    |
| Audio & SFX     | `Music/` & `SFX/` |
| PDFs            | `PDF/`       |
| Word Documents  | `Word/`      |
| PowerPoint Files| `PPT/`       |

🎵 Small audio files (under 10MB or containing "SFX" in the name) are treated as sound effects and moved to the `SFX` folder.

## 🛠 How It Works

- Uses **Watchdog** to monitor your `Downloads` folder.
- On file **creation** or **modification**, it checks the extension and moves the file to the appropriate folder.
- Ensures no files are overwritten by making filenames unique.

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install watchdog
```

### 2. Set Up
- Edit the `source_dir` and `base_dest_dir` paths in the script to your system's Downloads path.
- Run the script:
```bash
python file_organizer.py
```

### 3. Done!
The script when executed runs in the background and keeps your downloads organized automatically.

## 📁 Folder Structure

Example result after running:

```
Downloads/
├── Images/
├── Music/
├── SFX/
├── Videos/
├── Word/
├── PDF/
└── PPT/
```

## 💡 Features

- Real-time file monitoring
- Folder creation after script running
- Duplicate name protection
- Minimal configuration needed

---


