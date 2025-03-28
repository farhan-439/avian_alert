import numpy as np
from app.models.audio_detection import AudioDetection, db
from app.utils.audio_utils import process_audio_file, load_audio_model

model = load_audio_model()

def analyze_audio(file, flock_id):
    features = process_audio_file(file)
    pred = model.predict(np.array([features]))[0]
    
    classes = ['Healthy', 'Unhealthy', 'Noise']
    prediction_idx = np.argmax(pred)
    confidence = float(pred[prediction_idx])

    detection = AudioDetection(
        flock_id=flock_id,
        prediction=classes[prediction_idx],
        confidence=confidence
    )
    db.session.add(detection)
    db.session.commit()
    return detection
