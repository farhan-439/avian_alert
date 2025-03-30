import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras import layers

# Define any custom layer classes needed for your image model
# If your image model also uses BurnLayer
class BurnLayer(layers.Layer):
    def __init__(self, burn_intensity=0.2, **kwargs):
        super(BurnLayer, self).__init__(**kwargs)
        self.burn_intensity = burn_intensity
    
    def call(self, inputs, training=None):
        if training:
            return inputs + self.burn_intensity * tf.random.normal(shape=tf.shape(inputs))
        else:
            return inputs
    
    def get_config(self):
        config = super(BurnLayer, self).get_config()
        config.update({"burn_intensity": self.burn_intensity})
        return config

def process_image(filepath, target_size=(224, 224)):
    # Load and preprocess image
    img = Image.open(filepath)
    img = img.resize(target_size)  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def load_image_model():
    # Load the trained model with any custom objects
    custom_objects = {"BurnLayer": BurnLayer}  # Add if your image model uses BurnLayer
    model = tf.keras.models.load_model('models/image_model.h5', custom_objects=custom_objects)
    return model