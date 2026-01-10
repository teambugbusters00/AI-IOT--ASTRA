import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from typing import Optional

# Model configuration
MODEL_NAME = "microsoft/phi-2"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Global variables for model and tokenizer
model: Optional[AutoModelForCausalLM] = None
tokenizer: Optional[AutoTokenizer] = None

def load_model():
    """Load the Phi-2 model with optimizations"""
    global model, tokenizer

    if model is not None and tokenizer is not None:
        return  # Already loaded

    try:
        print(f"Loading Phi-2 model on {DEVICE}...")

        # Configure quantization for memory efficiency (optional)
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        ) if DEVICE == "cuda" else None

        # Load tokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        # Add padding token if missing
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # Load model with optimizations
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
            device_map="auto" if DEVICE == "cuda" else None,
            quantization_config=quantization_config,
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )

        print("Phi-2 model loaded successfully!")

    except Exception as e:
        print(f"Error loading model: {e}")
        raise RuntimeError(f"Failed to load Phi-2 model: {e}")

def run_model(prompt: str, max_tokens: int = 200) -> str:
    """
    Generate IoT code using Phi-2 model

    Args:
        prompt: Input prompt for code generation
        max_tokens: Maximum tokens to generate

    Returns:
        Generated code/text
    """
    global model, tokenizer

    # Ensure model is loaded
    if model is None or tokenizer is None:
        load_model()

    try:
        # Prepare input
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        ).to(DEVICE)

        # Generate with optimized parameters for code
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.3,  # Lower temperature for more focused code
                top_p=0.9,
                top_k=50,
                do_sample=True,
                num_beams=1,  # Greedy for speed
                repetition_penalty=1.1,
                length_penalty=1.0,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id
            )

        # Decode output
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Remove the input prompt from output
        if generated_text.startswith(prompt):
            generated_text = generated_text[len(prompt):].strip()

        return generated_text

    except Exception as e:
        error_msg = f"Error generating code: {e}"
        print(error_msg)
        return f"// Error: {error_msg}\n// Please try again or check your prompt."

def unload_model():
    """Unload model from memory (useful for memory management)"""
    global model, tokenizer
    if model is not None:
        del model
        model = None
    if tokenizer is not None:
        del tokenizer
        tokenizer = None
    torch.cuda.empty_cache() if torch.cuda.is_available() else None

# Initialize model on import (lazy loading)
def initialize_model():
    """Initialize model in background"""
    try:
        load_model()
    except Exception as e:
        print(f"Model initialization failed: {e}")
        print("Model will be loaded on first use")

# Optional: Initialize on import
# initialize_model()