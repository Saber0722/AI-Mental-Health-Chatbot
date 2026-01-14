# AI Model (ai_model)

This folder contains code and data for model training and inference used by the chatbot. It includes Jupyter notebooks, training scripts, and pre-trained/fine-tuned model artifacts stored under `ai_model/models/`.

---

# Directory Structure
```
├── dialogue_generation
│   ├── cache
│   │   ├── downloads
│   │   └── empathetic_dialogues
│   ├── data
│   │   └── emotion-emotion_69k.csv
│   ├── EDA.ipynb
│   ├── infer.ipynb
│   ├── models
│   │   ├── fine_tuned_distilbart_empathetic
│   │   ├── fine_tuned_t5_empathetic
│   │   └── fine_tuned_t5_empathetic_base
│   └── train_model.ipynb
├── load_dialogue_generation.py
├── load_sentimental_analysis.py
├── README.md
├── requirements.txt
└── sentiment_analysis
    ├── data
    │   ├── cached_data
    │   └── training_history.csv
    ├── explore.ipynb
    ├── infer.ipynb
    ├── models
    │   ├── checkpoints
    │   ├── sentiment_model
    │   └── sentiment_tokenizer
    └── train.ipynb

```
---

# Quick start

1. Install Python dependencies listed in `ai_model/requirements.txt` (use a virtual env).

2. Training AI Models:
- Run the `Dialogue Generation` model training under [dialogue_generation/train_model.ipynb](dialogue_generation/train_model.ipynb).
- Run the `Sentiment Analysis` model training under [sentiment_analysis/train.ipynb](sentiment_analysis/train.ipynb)

3. The other notebookes under each `AI Model` are used either for `EDA` or `inference`.

4. After training or downloading a model, ensure model files are available in `ai_model/models/<model_name>/` so the backend can load them.

---
# Notes

- Training large models requires GPU and may be time-consuming.
- Remove or anonymize any personal/sensitive data before using it for training.
