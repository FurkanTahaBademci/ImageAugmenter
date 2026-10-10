# ImageAugmenter

A command-line tool that expands object-detection datasets with weather and lighting
conditions that are hard to capture in the field. Each input image produces 6 variants:

| Folder    | Effect                            |
| --------- | --------------------------------- |
| `bright`  | Brightened image                  |
| `dark`    | Darkened image                    |
| `shadowy` | Random shadows                    |
| `speedy`  | Motion blur (speed effect)        |
| `snowy`   | Snow                              |
| `rainy`   | Heavy, slanted rain               |

All effects are photometric (from [Automold](https://github.com/UjjwalSaxena/Automold--Road-Augmentation-Library)):
object positions do not change, so the original YOLO bounding boxes stay valid.
With `--copy_txt`, each image's YOLO `.txt` label is copied next to every variant
under the matching name (`image_snowy.png` → `image_snowy.txt`).

https://github.com/FurkanTahaBademci/ImageAugmenter/assets/95905794/a986148f-8b7b-499a-8435-aa52b817d109

## Installation

```
git clone https://github.com/FurkanTahaBademci/ImageAugmenter.git
cd ImageAugmenter
pip install -r requirements.txt
```

## Usage

```
python main.py --input <input-dir> --output <output-dir> --type <image-extension> [--copy_txt]
```

| Argument     | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| `--input`    | Folder with the source images (and YOLO `.txt` labels, if any)      |
| `--output`   | Folder where the 6 effect subfolders are created                    |
| `--type`     | Image extension to process, e.g. `jpg` or `png`                     |
| `--copy_txt` | Copy each image's YOLO label to every variant                       |

Example:

```
python main.py --input dataset/images --output dataset/augmented --type jpg --copy_txt
```

If an image has no label file, the image variants are still written and a warning is printed.

## Limitations

- No geometric transforms (rotation, flip, scale), so labels never need recalculating.
  Combine with a geometric augmentation step if your model needs that variety.
- Every input produces all 6 variants; there is no per-effect selection yet.

## Authors

- [@FurkanTahaBademci](https://github.com/FurkanTahaBademci)
- [@oguzaybilir](https://github.com/oguzaybilir)
- [@BusraKz](https://github.com/BusraKz)
