str = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
lower = 0
for i in str:
    if (i.islower()):
        lower += 1
print("The number of lower case character is ",lower)