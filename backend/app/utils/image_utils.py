import numpy as np
import tensorflow as tf
from PIL import Image

def process_image(filepath):
    # Load and preprocess image
    img = Image.open(filepath)
    img = img.resize((224, 224))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize
    return img_array

def load_image_model():
    # Load the trained model
    model = tf.keras.models.load_model('models/image_model.h5')
    return model 