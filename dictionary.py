words = {}
n = int(input("Enter the number of words in your dictionary: "))

for i in range(n):
    key = input(f"Enter word {i+1}: ")
    value = input(f"Enter meaning of '{key}': ")
    words[key] = value   # ✅ INSIDE the loop

print(words)

word = input("Enter the word: ")
print(words.get(word, "Word not found"))
