import pyfiglet
from termcolor import colored


text = "congratulations CA206"
fonts = ["slant"]

for i, word in enumerate(text.split()):
    font = pyfiglet.Figlet(font = fonts[i% len(fonts)]) 
    color = ["red","blue","white"][i % 3]
    ascii_art = font.renderText(word)
    print(colored(ascii_art,color))
