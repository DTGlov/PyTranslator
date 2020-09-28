from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open("text file to be tranlated",mode="r",encoding="utf8") as myfile:
        text = myfile.read()
        translation = translator.translate(text)
        with open("new text file to save", mode="w",encoding="utf8") as myfile2:
           myfile2.write(translation)
except  FileNotFoundError as e:
    print("Please check file path")

