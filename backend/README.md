avian-alert-backend/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── audio.py
│   │   ├── image.py
│   │   ├── simulate.py
│   │   └── notifications.py
│   ├── utils/
│   │   ├── audio_processing.py
│   │   ├── image_model.py
│   │   └── burn_layer.py
│   ├── ml_models/
│   │   ├── audio_model.h5
│   │   └── image_model.h5
│   └── config.py
│
├── instance/
│   └── config.py  # (secret keys, DB URI, etc.)
│
├── requirements.txt
├── run.py
└── README.md
