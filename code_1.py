from PIL import Image, ImageFilter
from colorama import Fore, Style  # Importujte Fore pro barvy textu, Style pro reset barvy
#pip install pillow
#pip install colorama

def program():
    obrazek = Image.open("hunter.jpg")
    sirka, vyska = obrazek.size

    while True:
        volba = input("Zadejte filtr: (1, 2, 3, 4): ")
        if volba == "1":
            print(Fore.GREEN + "Zelený" + Style.RESET_ALL + " filtr")
            souhlas = input("Chcete použít ZELENÝ filtr? (pouze ano/ne): ").lower()
            if souhlas == "ano":
                for x in range(sirka):
                    for y in range(vyska):
                        r, g, b = obrazek.getpixel((x, y))
                        g = min(255, max(0, g + 100))
                        obrazek.putpixel((x, y), (r, g, b))
                break
            elif souhlas == "ne":
                print("Znovu vyberte filtr.")
            else:
                print("Neplatný vstup")
                print("Znovu vyberte filtr.")
        elif volba == "2":
            print(Fore.RED + "Červený" + Style.RESET_ALL + " filtr")
            souhlas = input("Chcete použít ČERVENÝ filtr? (pouze ano/ne): ").lower()
            if souhlas == "ano":
                for x in range(sirka):
                    for y in range(vyska):
                        r, g, b = obrazek.getpixel((x, y))
                        r = min(255, max(0, r + 100))
                        obrazek.putpixel((x, y), (r, g, b))
                break
            elif souhlas == "ne":
                print("Znovu vyberte filtr.")
            else:
                print("Neplatný vstup")
                print("Znovu vyberte filtr.")
        elif volba == "3":
            print(Fore.BLUE + "Modrý" + Style.RESET_ALL + " filtr")
            souhlas = input("Chcete použít MODRÝ filtr? (pouze ano/ne): ").lower()
            if souhlas == "ano":
                for x in range(sirka):
                    for y in range(vyska):
                        r, g, b = obrazek.getpixel((x, y))
                        b = min(255, max(0, b + 100))
                        obrazek.putpixel((x, y), (r, g, b))
                        break
            elif souhlas == "ne":
                print("Znovu vyberte filtr.")
            else:
                print("Neplatný vstup")
                print("Znovu vyberte filtr.")
        elif volba == "4":
            print(Fore.YELLOW + "Rozmazávací" + Style.RESET_ALL + " filtr")
            souhlas = input("Chcete použít filtr ROZMAZÁVACÍ? (pouze ano/ne): ").lower()
            if souhlas == "ano":
                obrazek = obrazek.filter(ImageFilter.BLUR)
                break
            elif souhlas == "ne":
                print("Znovu vyberte filtr.")
            else:
                print("Neplatný vstup")
                print("Znovu vyberte filtr.")

    obrazek.show()

program()

         

         








