text = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(text[89:])
text1 = "giveqcctsicslyqlenycn"
lower = 0
for i in text1:
    if (i.islower()):
        lower += 1
print("The number of lower case character is ",lower)