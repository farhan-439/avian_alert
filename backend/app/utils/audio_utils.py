import numpy as np
import librosa
import tensorflow as tf

def process_audio_file(file):
    # Load and preprocess audio file
    audio, sr = librosa.load(file, sr=22050)
    # Extract features (mel spectrogram)
    mel_spec = librosa.feature.melspectrogram(y=audio, sr=sr)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    # Reshape to match model input
    features = np.resize(mel_spec_db, (128, 128))
    return features

def load_audio_model():
    # Load the trained model
    model = tf.keras.models.load_model('models/audio_model.h5')
    return model 