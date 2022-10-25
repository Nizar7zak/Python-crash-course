write your code that take an input as sentence form user and print the result

message = input('>')

words = message.split(' ')

emojis = {
    "happy": ":)",
    "sad": ":("
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)
