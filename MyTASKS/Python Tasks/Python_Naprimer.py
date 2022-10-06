word= input("Vvdedite slovo: ")
word_lower = [word.lower()]
if word_lower[0][0] == "а" or word_lower[0] == "о" or word_lower[0] == "у" or word_lower[0] == "е" or word_lower[0] == "я":
    word_lower.append("way")
else:
    word_lower.append(word_lower[0][0])
    word_lower.pop(0)
    word_lower.append("ay")
print("".join(word_lower))
