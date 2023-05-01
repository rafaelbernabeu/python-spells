import keras_cv
from tensorflow import keras
from PIL import Image

query = "photograph of an astronaut riding a horse"

keras.mixed_precision.set_global_policy("float32")
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)
images = model.text_to_image(query, batch_size=2)

i=0
for image in images:
    Image.fromarray(image).save(f"{query}-{i}.png")
    i+=1
