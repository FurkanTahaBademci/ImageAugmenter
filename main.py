import argparse
import Automold as am
import glob
import cv2 
from tqdm import tqdm
import os
import time
import shutil

parser = argparse.ArgumentParser(description='Image Augmentation Script')
parser.add_argument('--input_path', type=str, help='Path to input images directory', required=True)
parser.add_argument('--output_path', type=str, help='Path to output directory', required=True)
parser.add_argument('--image_type', type=str, help='Image type (e.g., jpeg, png)', default='jpeg')

args = parser.parse_args()

path = args.input_path
output = args.output_path
type = args.image_type

image_paths= glob.glob(path+"*."+type)
time_path = time.time()

os.mkdir(output+f"bright_{time_path}/")
os.mkdir(output+f"dark_{time_path}/")
os.mkdir(output+f"shadowy_{time_path}/")
os.mkdir(output+f"snowy_{time_path}/")
os.mkdir(output+f"rainy_{time_path}/")
os.mkdir(output+f"speedy_{time_path}/")

for img in tqdm(image_paths):
    
    image = cv2.imread(img)
    bright_image = am.brighten(image)
    dark_image = am.darken(image, darkness_coeff=0.3)
    shadowy_images= am.add_shadow(image,no_of_shadows=2, shadow_dimension=8)
   
    speedy_images= am.add_speed(image)
    
    snowy_images= am.add_snow(image, snow_coeff=0.3)
    image_name = f"data_augmente_{time.time()}.jpeg"
    txt_name = image_name.replace(".jpeg",".txt")
    txt_path_new = output+f"snowy_{time_path}/{txt_name}"
    txt_path_before = img.replace(".jpeg",".txt") 
    shutil.copy(txt_path_before,txt_path_new)
    cv2.imwrite(output+f"snowy_{time_path}/{image_name}",snowy_images)
    
    rainy_images= am.add_rain(image, rain_type='heavy', slant=20)
    image_name = f"data_augmente_{time.time()}.jpeg"
    txt_name = image_name.replace(".jpeg",".txt")
    txt_path_new = output+f"rainy_{time_path}/{txt_name}"
    txt_path_before = img.replace(".jpeg",".txt") 
    shutil.copy(txt_path_before,txt_path_new)
    cv2.imwrite(output+f"rainy_{time_path}/{image_name}",rainy_images)
    
    cv2.imwrite(output+f"bright_{time_path}/{image_name}",bright_image);image_name = f"data_augmente_{time.time()}.jpg"
    cv2.imwrite(output+f"dark_{time_path}/{image_name}",dark_image);image_name = f"data_augmente_{time.time()}.jpg"
    cv2.imwrite(output+f"shadowy_{time_path}/{image_name}",shadowy_images);image_name = f"data_augmente_{time.time()}.jpg"
    cv2.imwrite(output+f"speedy_{time_path}/{image_name}",speedy_images);image_name = f"data_augmente_{time.time()}.jpg"

    
    
     