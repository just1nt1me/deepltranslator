import deepl
import docx
from deep_key import key

# authenticate with your API key
translator =deepl.Translator(key)

# open the docx file
input_path=input("What document do you want to translate? ")
output_path="en"+input_path
translator.translate_document_from_filepath(input_path, output_path, target_lang="EN-US")
