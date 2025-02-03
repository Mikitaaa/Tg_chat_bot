from huggingface_hub import InferenceClient
from Config_handler import load_config

config = load_config('config.txt')

client = InferenceClient(
    provider="hf-inference",
    api_key = config['api_key']
)

def getTextResponse(user_message: str) -> str:
    prompt_message = config['prompt_message'].format(user_message=user_message)
    messages = [{"role": "user", "content": prompt_message}]

    try:
        completion = client.chat.completions.create(
            model="mistralai/Mistral-Nemo-Instruct-2407",
            messages=messages,
            max_tokens=300,
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        print(f"Ошибка при запросе к модели: {e}")
        return "Хз что сказать"
