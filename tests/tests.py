import easygpt
import os
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

print("Testing EasyGPT class version: ", easygpt.__version__)

model_class = easygpt.GPTModel()

for model in model_class.availabe_models():
    gpt = easygpt.EasyGPT(openai="openai", model_name=model)
    print(f"Model: {model} Real Name: {gpt.model.get_real_name()}")
    result = gpt.ask("What is the meaning of life?")
    print("What is the meaning of life? \n", result)
