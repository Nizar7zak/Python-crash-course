message = input('>')

words = message.split(' ')

emojies = {
    "happy": ":)",
    "sad": ":("
}

output = ""
for word in words:
    output += emojies.get(word, word) + " "

print(output)
