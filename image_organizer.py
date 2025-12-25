import os
import shutil

# Paths
downloads_folder = 'C:/Users/dell/Downloads'
pictures_folder = 'C:/Users/dell/Pictures'

# Create destination folder if not exists
os.makedirs(pictures_folder, exist_ok=True)

# Move image files
for filename in os.listdir(downloads_folder):
    if filename.endswith(('.jpg', '.png')):
        source = os.path.join(downloads_folder, filename)
        destination = os.path.join(pictures_folder, filename)
        shutil.move(source, destination)
        print(f"Moved: {filename}")
