import os
import cloudinary
import cloudinary.uploader
from pathlib import Path
from environs import Env

# Load environment variables
env = Env()
env.read_env()

# Configure Cloudinary
cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)

MEDIA_DIR = Path("media/images")

# Image extensions we want to upload
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".avif",
}

files = [
    file for file in MEDIA_DIR.iterdir()
    if file.is_file() and file.suffix.lower() in IMAGE_EXTENSIONS
]

print(f"Found {len(files)} image files.")
print("-" * 50)

for file in files:
    try:
        print(f"Uploading: {file.name}")

        result = cloudinary.uploader.upload(
            str(file),
            folder="media/images",
            use_filename=True,
            unique_filename=False,
            overwrite=True,
        )

        print(f"SUCCESS: {result['secure_url']}")
        print()

    except Exception as e:
        print(f"FAILED: {file.name}")
        print(f"ERROR: {e}")
        print()

print("-" * 50)
print("Upload process completed.")