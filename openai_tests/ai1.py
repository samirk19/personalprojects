import pathlib
import textwrap
import google.generativeai as genai
import os
#from IPython.display import display
from IPython.display import Markdown

key = os.getenv('GOOGLE_API_KEY')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



if __name__ == "__main__":
    genai.configure(api_key=key)
    
    """for x in genai.list_models():
        if 'generateContent' in x.supported_generation_methods:
            print(x.name)"""

    model1 = genai.GenerativeModel('gemini-pro')
    question = input("What do you want to ask Gemini Pro? ")
    response = model1.generate_content(question, stream=False)

    print(response.text)
    
    """for chunk in response:
        print(chunk.text)
        print("_"*80)"""