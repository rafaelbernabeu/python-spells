import keras_cv
from tensorflow import keras
from PIL import Image
import argparse
from os import path

parser = argparse.ArgumentParser(
    description="Generate images from prompt",
    usage="$ python3 stable-duffusion.py prompt [...]"
)

parser.add_argument('-p', '--path', type=str, help="Path to save generated images. Defaults to current folder", default=".")
parser.add_argument('-b', '--batch-size', type=int, help="Num of images generated for each prompt", default=1)
parser.add_argument('prompt', nargs="+", type=str, help='A list of prompts seppared by spaces. Use "" to group words.') 

args = parser.parse_args()

keras.mixed_precision.set_global_policy("float32")
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

for p in args.prompt:
    images = model.text_to_image(p, batch_size=args.batch_size)

    for i, image in enumerate(images):
        Image.fromarray(image).save(path.join(args.path, f"{p}-{i}.png"))

