import openai
import os

os.environ['OPENAI_API_KEY'] = "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"

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def return_doc(text):
    prompt = f"""
    Se baseando no texto entre parenteses triplos como um modelo de petição, transforme o texto delimitado por aspas triplas em uma petição, pórem sumarize a parte dos requerimentos finais.

    Os dados que você não conseguir preencher deixe entre colchetes e em negrito para o advogado inserir depois.
    Vale lembrar que o linguajar deve ser o mais formal possível porque é uma petição, ou seja, um documento jurídico.
    Gere tudo isso em um formato HTML.
    ```{text}```
    (((O documento começa com o endereço do juiz, seguido de um espaço de aproximadamente 10 cm. Em seguida, é apresentado o nome do autor, sua nacionalidade, estado civil, profissão, documento de identidade e CPF. O documento continua com o endereço do advogado para recebimento de intimações. O documento então apresenta os fatos relevantes para o julgamento da lide.)))
    """

    return get_completion(prompt)
