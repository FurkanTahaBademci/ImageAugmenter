import argparse
import Automold as am
import glob
import cv2 
from tqdm import tqdm
import os
import time
import shutil

parser = argparse.ArgumentParser(description='Image Augmentation Script')
parser.add_argument('--input', type=str, help='Path to input images directory', required=True)
parser.add_argument('--output', type=str, help='Path to output directory', required=True)
parser.add_argument('--type', type=str, help='Image type (e.g., jpeg, png)', required=True)
parser.add_argument('--copy_txt', action='store_true', help='Copy txt files if True, otherwise do not copy')

args = parser.parse_args()

path = args.input
output = args.output
type = args.type
copy_txt = args.copy_txt

image_paths= glob.glob(path+"*."+type)
time_path = time.time()

os.mkdir(output+f"bright/")
os.mkdir(output+f"dark/")
os.mkdir(output+f"shadowy/")
os.mkdir(output+f"snowy/")
os.mkdir(output+f"rainy/")
os.mkdir(output+f"speedy/")

for img in tqdm(image_paths):

    image = cv2.imread(img)
    bright_image = am.brighten(image)
    dark_image = am.darken(image, darkness_coeff=0.3)
    shadowy_images= am.add_shadow(image,no_of_shadows=2, shadow_dimension=8)

    speedy_images= am.add_speed(image)

    snowy_images= am.add_snow(image, snow_coeff=0.3)
    image_name = f"data_augmente_{time.time()}.{type}"
    if copy_txt:
        txt_name = os.path.basename(img).replace(f".{type}",".txt")
        txt_path_new = os.path.join(output, "snowy", txt_name)
        txt_path_before = img.replace(f".{type}",".txt")
        shutil.copy(txt_path_before,txt_path_new)
    cv2.imwrite(os.path.join(output, "snowy", image_name), snowy_images)

    rainy_images= am.add_rain(image, rain_type='heavy', slant=20)
    image_name = f"data_augmente_{time.time()}.{type}"
    if copy_txt:
        txt_name = os.path.basename(img).replace(f".{type}",".txt")
        txt_path_new = os.path.join(output, "rainy", txt_name)
        txt_path_before = img.replace(f".{type}",".txt")
        shutil.copy(txt_path_before,txt_path_new)
    cv2.imwrite(os.path.join(output, "rainy", image_name), rainy_images)

    cv2.imwrite(os.path.join(output, "bright", image_name), bright_image)
    cv2.imwrite(os.path.join(output, "dark", image_name), dark_image)
    cv2.imwrite(os.path.join(output, "shadowy", image_name), shadowy_images)
    cv2.imwrite(os.path.join(output, "speedy", image_name), speedy_images)
