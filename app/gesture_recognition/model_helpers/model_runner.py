import tensorflow
# import os

# current_dir = os.path.dirname(__file__)
# model_filename = current_dir + '/model.h5'
model = tensorflow.keras.models.load_model('./model.h5')