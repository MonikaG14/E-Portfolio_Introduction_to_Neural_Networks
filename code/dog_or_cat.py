from tensorflow import keras
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from PIL import ImageDraw, ImageFont
import numpy as np

IMG_SIZE = 160  # All images will be resized to 160x160

model = keras.models.load_model('dogs_vs_cats.h5')

# load the image
picture = 'cat_vs_dog/dog2.jpg'

# once in full size for display
img = load_img(picture)

# reshape for use with the model
img_conv = load_img(picture, target_size=(IMG_SIZE, IMG_SIZE))
# convert to numpy array
img_array = img_to_array(img_conv)
# normalize from 0:255 to -1:1
img_array = (img_array / 127.5) - 1
# reshape again for model input (additional dimension)
img_array = img_array.reshape(1, IMG_SIZE, IMG_SIZE, 3)
# use model to get prediction if cat or dog
prediction = model(img_array)
class_names = ['Cat', 'Dog']
print(prediction)
# extract integer value between 0 and +inf from prediction
cat_or_dog = int(prediction[0][0])
print(cat_or_dog)
index = np.sign(cat_or_dog)   # returns -1 if negative, 0 if 0, +1 if positive
print(index)
# cats are 0, dogs are 1
answer = (class_names[index])
print("It is a " + answer + "!")

# draw image with title
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30, encoding="unic")
draw.text((0, 0), answer, (0, 0, 0), font)
# show image
img.show()
