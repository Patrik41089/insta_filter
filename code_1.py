from PIL import Image
from PIL import ImageFilter

def apply_filter(image, filter_type):
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))

            if filter_type == "Filter 1":
                g = min(255, max(0, g + 50))
            elif filter_type == "Filter 2":
                r = min(255, max(0, r + 50))
            elif filter_type == "Filter 3":
                b = min(255, max(0, b + 50))
            elif filter_type == "Filter 4":
                image = image.filter(ImageFilter.BLUR)

            image.putpixel((x, y), (r, g, b))

    return image

def main():
    image = Image.open("hunter.jpg")
    filter_type = input("Vyberte filtr (1, 2, 3, 4): ")

    if filter_type in ["1", "2", "3", "4"]:
        image_filtered = apply_filter(image, "Filter " + filter_type)
        image_filtered.show()
    else:
        print("Neplatný vstup.")

if __name__ == "__main__":
    main()



