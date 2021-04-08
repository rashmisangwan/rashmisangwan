import tensorflow
import os

current_dir = os.path.dirname(__file__)
model_filename = current_dir + '/model.h5'
model = tensorflow.keras.models.load_model(model_filename)

def run(img_path):
    from PIL import Image, ImageOps
    from tensorflow.keras.preprocessing import image

    img = image.load_img(img_path, target_size=(28, 28, 1))
    img = ImageOps.grayscale(img)

    img_array = image.img_to_array(img)
    img_array = img_array.reshape(-1,28,28,1)
    img_array = img_array/255.

    return model.predict_classes(img_array)

# model.predict_classes(your_image('./ges.png'))