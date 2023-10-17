# Characters supported by isdecimal() and isdigit()
unicode_chars = "123 1/4 ½¾०१२३০১২৩੦੧੨੩౦౧౨౩൦൧൨൩"

for char in unicode_chars:
    print(f"{char}: isdecimal: {char.isdecimal()}, isdigit: {char.isdigit()}")
