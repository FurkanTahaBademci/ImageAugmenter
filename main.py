import argparse
import Automold as am
import glob
import cv2
from tqdm import tqdm
import os
import time
import shutil

def main():
    parser = argparse.ArgumentParser(description='Image Augmentation Script')
    parser.add_argument('--input', type=str, help='Path to input images directory', required=True)
    parser.add_argument('--output', type=str, help='Path to output directory', required=True)
    parser.add_argument('--type', type=str, help='Image type (e.g., jpeg, png)', required=True)
    parser.add_argument('--copy_txt', action='store_true', help='Copy txt files if True, otherwise do not copy')

    args = parser.parse_args()

    path = args.input
    output = args.output
    image_type = args.type
    copy_txt = args.copy_txt

    image_paths = glob.glob(os.path.join(path, f'*.{image_type}'))
    time_path = time.time()

    create_directories(output, "bright", "dark", "shadowy", "snowy", "rainy", "speedy")

    for img in tqdm(image_paths):
        image = cv2.imread(img)
        bright_image = am.brighten(image)
        dark_image = am.darken(image, darkness_coeff=0.3)
        shadowy_images= am.add_shadow(image,no_of_shadows=2, shadow_dimension=8)
        speedy_images= am.add_speed(image)
        snowy_images= am.add_snow(image, snow_coeff=0.3)
        rainy_images= am.add_rain(image, rain_type='heavy', slant=20)

        process_image(output, img, copy_txt, "snowy", snowy_images, image_type)
        process_image(output, img, copy_txt, "rainy", rainy_images, image_type)
        process_image(output, img, False, "bright", bright_image, image_type)
        process_image(output, img, False, "dark", dark_image, image_type)
        process_image(output, img, False, "shadowy", shadowy_images, image_type)
        process_image(output, img, False, "speedy", speedy_images, image_type)


def create_directories(output_path, *directories):
    for directory in directories:
        os.makedirs(os.path.join(output_path, directory), exist_ok=True)

def process_image(output, img, copy, folder, processed_image, image_type):
    file_name = os.path.basename(img)
    file_name_without_extension = os.path.splitext(file_name)[0]
    image_name = f"{file_name_without_extension}_{folder}.{image_type}"
    if copy:
        txt_name = file_name.replace(f".{image_type}", ".txt")
        txt_path_new = os.path.join(output, folder, txt_name)
        txt_path_before = img.replace(f".{image_type}", ".txt")
        shutil.copy(txt_path_before, txt_path_new)
    cv2.imwrite(os.path.join(output, folder, image_name), processed_image)

    
if __name__ == "__main__":
    main()
