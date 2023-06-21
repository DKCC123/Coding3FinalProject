from PIL import Image
import os

folder_path = 'D:/Programming/Projects/Python/DKC ImageResize/Symbolism'
folder_path_resized = 'D:/Programming/Projects/Python/DKC ImageResize/Symbolism_Resized'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_name = os.path.basename(file_path)
        image = Image.open(file_path)
        img = image.resize((256,256))
        img.save(folder_path_resized + '/' + file_name)
    print('All graphs have been resized successfully.')