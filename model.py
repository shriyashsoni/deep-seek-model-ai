from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "deepseek-ai/deepseek-coder-6.7b"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

def generate_response(prompt):
    """Generate AI response using DeepSeek model."""
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=512, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[0], skip_special_tokens=True).split("AI:")[-1].strip()
    return response
