from .celery_app import celery_app
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


# Cargar el modelo y el tokenizador
model_name = "codellama/CodeLlama-13b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
)


# Definir la tarea de generación de código
@celery_app.task
def generate_code(prompt: str, max_length: int = 700) -> str:
    """Genera código a partir de un prompt."""

    # Preparar la entrada
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=max_length,
        return_attention_mask=True,
    ).to("cuda" if torch.cuda.is_available() else "cpu")

    # Generar la respuesta con parámetros ajustados
    outputs = model.generate(
        inputs.inputs_ids,
        max_length=5000,
        temperature=0.9,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id,
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
