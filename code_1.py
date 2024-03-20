from PIL import Image

obrazek = Image.open("hunter.jpg")
sirka, vyska = obrazek.size

for x in range(sirka):
    for y in range(vyska):
        r, g, b = obrazek.getpixel((x,y))
        
        g = min(255, max(0, g + 40))
        r = min(255, max(0, r + 40))
        b = min(255, max(0, b + 40))

        obrazek.putpixel((x,y), (r, g, b))

obrazek.show()

