frase = input("Digite uma frase: ")

print(f"Na frase: '{frase}' tem:\n",
    f"a ou A: {frase.count("a") + frase.count("A")}\n",
    f"e ou E: {frase.count("e") + frase.count("E")}\n",
    f"i ou I: {frase.count("i") + frase.count("I")}\n",
    f"o ou O: {frase.count("o") + frase.count("O")}\n",
    f"u ou U: {frase.count("u") + frase.count("U")}\n")