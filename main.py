txt = "**********"

while "*" in txt:
    print(txt)
    txt = txt.removesuffix("*")
