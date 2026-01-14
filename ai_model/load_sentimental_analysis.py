import sys
import tensorflow as tf
from transformers import TFDistilBertForSequenceClassification, DistilBertTokenizer
import os

# Get base path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths
MODEL_DIR = os.path.join(BASE_DIR, 'sentiment_analysis', 'models', 'sentiment_model')
TOKENIZER_DIR = os.path.join(BASE_DIR, 'sentiment_analysis', 'models', 'sentiment_tokenizer')

# Load the model and tokenizer
try:
    model = TFDistilBertForSequenceClassification.from_pretrained(MODEL_DIR)
    tokenizer = DistilBertTokenizer.from_pretrained(TOKENIZER_DIR)
except Exception as e:
    print(f"Error loading model or tokenizer: {e}", file=sys.stderr)
    sys.exit(1)

# Mapping go_emotions labels (0-27) to sentiment
SENTIMENT_MAP = {
    # Positive emotions
    0: "positive",  # admiration
    1: "positive",  # amusement
    2: "positive",  # approval
    7: "positive",  # excitement
    9: "positive",  # gratitude
    12: "positive", # joy
    14: "positive", # love
    16: "positive", # optimism
    19: "positive", # pride
    21: "positive", # relief
    # Negative emotions
    3: "negative",  # anger
    4: "negative",  # annoyance
    6: "negative",  # disappointment
    8: "negative",  # fear
    13: "negative", # disgust
    15: "negative", # nervousness
    17: "negative", # pain
    22: "negative", # sadness
    25: "negative", # embarrassment
    26: "negative", # nervousness
    27: "negative", # remorse
    # Neutral emotions
    5: "neutral",   # confusion
    10: "neutral",  # curiosity
    11: "neutral",  # desire
    18: "neutral",  # realization
    20: "neutral",  # surprise
    23: "neutral",  # sympathy
    24: "neutral"   # neutral
}

def analyze_sentiment(text):
    try:
        # Tokenize input (match training settings)
        inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True, max_length=128)
        
        # Run inference
        outputs = model(inputs)
        logits = outputs.logits
        
        # Get predicted class
        predicted_class = tf.argmax(logits, axis=1).numpy()[0]
        
        # Map to sentiment
        return SENTIMENT_MAP.get(predicted_class, "neutral")
    except Exception as e:
        print(f"Error during inference: {e}", file=sys.stderr)
        return "neutral"

if __name__ == '__main__':
    # Get user input from command-line argument
    user_input = sys.argv[1] if len(sys.argv) > 1 else ''
    sentiment = analyze_sentiment(user_input)
    print(sentiment)  # Output to be captured by Node.js