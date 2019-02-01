with open("image.ppm","w") as img:
    img.write("P3 500 500 500 ")
    for x in range(500):
        for y in range(500):
            nl = ""
            for x in range(3):
                nl += str(int((x/(y+1)**2) % 500 + (y/(x+1)**2) % 500))
                nl += " "
            if y > (x**2):
                for x in range(3):
                    nl += str(int((y / (x + 1) ** 2) % 500 + (x / (y + 1) ** 2) % 500))
                    nl += " "
            if y > (x**3):
                for x in range(3):
                    nl += str(int((y % (x + 1) ** 2) % 500 + (x % (y + 1) ** 2) % 500))
                    nl += " "
            img.write(nl)