from os import scandir, rename, makedirs
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folders
source_dir = "C://Users/91998/Downloads"
base_dest_dir = "C://Users/91998/Downloads"

dest_dir_sfx = join(base_dest_dir, "SFX")
dest_dir_music = join(base_dest_dir, "Music")
dest_dir_video = join(base_dest_dir, "Videos")
dest_dir_image = join(base_dest_dir, "Images")
dest_dir_pdf = join(base_dest_dir, "PDF")
dest_dir_ppt = join(base_dest_dir, "PPT")
dest_dir_doc = join(base_dest_dir, "Word")
dest_dir_zip = join(base_dest_dir, "ZIP")
dest_dir_cdr = join(base_dest_dir, "CDR")

# Supported file extensions
image_extensions = [".jpg", ".jpeg", ".png",
                    ".gif", ".webp", ".bmp", ".svg", ".ico"]
video_extensions = [".mp4", ".avi", ".mov", ".flv", ".wmv"]
audio_extensions = [".mp3", ".wav", ".m4a", ".flac"]
document_extensions = [".doc", ".docx", ".odt", ".xls", ".xlsx"]
ppt_extensions = [".ppt", ".pptx"]
pdf_extensions = [".pdf"]
zip_extensions = [".zip"]
cdr_extensions = [".cdr"]

# Create necessary folders if they don't exist


def create_folders():
    for folder in [dest_dir_sfx, dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_pdf, dest_dir_ppt, dest_dir_doc, dest_dir_zip, dest_dir_cdr]:
        makedirs(folder, exist_ok=True)

# Make filename unique


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

# Move file


def move_file(dest, entry, name):
    if exists(join(dest, name)):
        name = make_unique(dest, name)
    move(entry.path, join(dest, name))

# Event Handler


class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.organize_files()

    def on_created(self, event):
        self.organize_files()

    def organize_files(self):
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    self.check_and_move(entry, name)

    def check_and_move(self, entry, name):
        if any(name.lower().endswith(ext) for ext in audio_extensions):
            dest = dest_dir_sfx if entry.stat(
            ).st_size < 10_000_000 or "SFX" in name else dest_dir_music
            move_file(dest, entry, name)
            logging.info(f"Moved audio file: {name}")

        elif any(name.lower().endswith(ext) for ext in video_extensions):
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

        elif any(name.lower().endswith(ext) for ext in image_extensions):
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

        elif any(name.lower().endswith(ext) for ext in document_extensions):
            move_file(dest_dir_doc, entry, name)
            logging.info(f"Moved document file: {name}")

        elif any(name.lower().endswith(ext) for ext in pdf_extensions):
            move_file(dest_dir_pdf, entry, name)
            logging.info(f"Moved pdf file: {name}")

        elif any(name.lower().endswith(ext) for ext in ppt_extensions):
            move_file(dest_dir_ppt, entry, name)
            logging.info(f"Moved PowerPoint file: {name}")

        elif any(name.lower().endswith(ext) for ext in zip_extensions):
            move_file(dest_dir_zip, entry, name)
            logging.info(f"Moved zip file: {name}")

        elif any(name.lower().endswith(ext) for ext in cdr_extensions):
            move_file(dest_dir_cdr, entry, name)
            logging.info(f"Moved cdr file: {name}")

        else:
            logging.info(f"Skipped file (no matching extension): {name}")


# Run
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    create_folders()

    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=False)
    observer.start()

    # Initial sorting when script runs
    event_handler.organize_files()

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def organize_files(self):
    with scandir(source_dir) as entries:
        for entry in entries:
            if entry.is_file():
                print(f"Found file: {entry.name}")   # <-- Add this
                name = entry.name
                self.check_and_move(entry, name)
