# Implementación de API para generación de código

## Modelo
Modelo LLM (Large Language Model) de Instructor 13b de Hugging Fase para la generación de código en diferenes lenguajes de programación.

**Modelo:** `codellama/CodeLlama-13b-Instruct-hf`

Disponible en: [_Hugging Face_](https://huggingface.co/codellama)

## Notebooks
Aloja los Notebooks de Jupyter con los ejemplos de uso del modelo para la generación de código en diferentes lenguajes de programación.

## API

### Ejecución en local
Ejecute el siguiente comando para iniciar la API en local:

```
flask --app "app:create_app('sqlite:///db.sqlite')" run
```
