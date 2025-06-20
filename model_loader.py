import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Prevent TensorFlow usage

from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

def load_model(model_name="declare-lab/flan-alpaca-base"):
    print("[INFO] Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return generator
