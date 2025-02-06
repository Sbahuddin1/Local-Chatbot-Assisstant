# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")

def generate_response(prompt: str) -> str:
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Generate a response
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    
    # Decode the generated tokens to a string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response