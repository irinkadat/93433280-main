import sys
from pyfiglet import Figlet


if sys.argv[1] != '-f' and sys.argv[1] != '-font':
    sys.exit('Invalid usage')

txt = input("enter text:")



figlet = Figlet()
fonts = figlet.getFonts()


figlet.setFont(font=sys.argv[2])

print(figlet.renderText(txt))
