string = "label"
flg = ""

for c in string:
    flg += chr(ord(c)^13)

    print(f"crypto{{{flg}}}")