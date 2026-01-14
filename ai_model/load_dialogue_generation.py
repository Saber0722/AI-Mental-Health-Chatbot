import sys
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

# Path to your saved fine-tuned model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "dialogue_generation", "models", "fine_tuned_distilbart_empathetic")

# Load tokenizer and model
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
    
    # ✅ Force override the broken config value
    model.config.early_stopping = True

except Exception as e:
    print(f"Error loading model: {e}", file=sys.stderr)
    sys.exit(1)

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_response(prompt: str) -> str:
    try:
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=128)
        input_ids = inputs["input_ids"].to(device)
        attention_mask = inputs["attention_mask"].to(device)

        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=128,
            min_length=5,
            num_beams=4,
            do_sample=True,
            top_k=50,
            top_p=0.9,
            early_stopping=True   # ✅ Needed due to broken config
        )

        return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    except Exception as e:
        print(f"Error during generation: {e}", file=sys.stderr)
        return "I'm here to help. Could you share more?"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python load_dialogue_generation.py \"Your input text here\"")
        sys.exit(1)

    user_input = sys.argv[1]
    print(generate_response(user_input))
