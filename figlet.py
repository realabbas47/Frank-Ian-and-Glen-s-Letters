from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

# Taking font from cmd line if exists and setting font#
fnt = "a"
arg = sys.argv
if len(arg) == 3:
    if arg[1] != "-f":
        print("Invalid usage")
        sys.exit(1)
    else:
        try:
            index = fonts.index(arg[2])
            fnt = figlet.setFont(font=arg[2])
        except ValueError:
            print("Invalid usage")
            sys.exit(1)
elif len(arg) == 1:
    fnt = figlet.setFont(font=random.choice(fonts))
else:
    print("Invalid usage")
    sys.exit(1)


#Printing text#
text = input("Input: ")
print(figlet.renderText(text))
