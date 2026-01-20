hausa = {
    "hello": "Sannu",
    "come": "Zo",
    "go": "Tafi",
    "name": "Suna",
    "money": "Kudi",
    "school": "Makaranta",
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "good": "nagari",
    "bad": "mara kyau",
    "sun": "rana",
    "moon": "wata",
    "fire": "wuta",
    "book": "littafi",
    "run": "gudu",
    "eat": "ci"
}

languages = {
    "hausa": hausa,
}

print("Language Translator")
print("Choose a Language: hausa, ")

language = input("Enter Language: ")

if language not in languages:
    print("Language not found. Pick Again ")
else:
    english_word = input("Enter a English word to translate: ")

    if english_word in languages[language]:
        print("Translation is; ",
 languages[language][english_word])
    else:
        print("Word not found in the Dictionary")