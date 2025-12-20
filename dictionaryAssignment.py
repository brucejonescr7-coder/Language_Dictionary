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

yoruba = {
    "iya": "mother",
    "bata": "shoes",
    "omi": "water",
    "rara": "no",
    "baba": "father",
    "ekaro": "good morning",
    "nibo": "where",
    "duro": "stand",
    "rin": "walk",
    "mu": "drink",
    "ibi": "place/here",
    "wa": "come",
    "lo": "go",
    "se": "a question marker(like 'is it')",
    "pele": "sorry",
    "oko": "car",
    "e nle o!": "hello",
    "ile": "house",
    "omo": "child",
    "ologbo": "cat",
}

languages = {
    "hausa": hausa,
    "yoruba": yoruba,
}

print("Language Translator")
print("Choose a Language: hausa,yoruba ")

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