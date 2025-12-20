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

igbo = {
    "Thank You": "Ekele",
    "Please": "Biko",
    "Hello": "Ndewo",
    "Person": "Onye",
    "Child": "Nwa",
    "House": "Ezi",
    "Water": "Mmiri",
    "Food": "Nri",
    "Clean": "Ocha",
    "Justice": "Ọfọ",
    "Don't Kill": "Egbuna",
    "Head": "Aka",
    "Sun": "Anyanwu",
    "Fire": "Ọkụ",
    "Wealth": "Akụ",
    "Friend": "Enyi",
    "Mother": "Nne",
    "Father": "Nna",
    "Gold": "Ọla",
    "Mind": "Uche",
    "Home": "Ụlọ",
}


edo = {
    "hello": "koyo",
    "water": "ami",
    "food": "ikhian",
    "house": "owa",
    "come": "ya",
    "go": "gha",
    "man": "okpia",
    "woman": "okhuo",
    "child": "omo",
    "good": "noghie",
    "bad": "khi",
    "sun": "owia",
    "moon": "okhuo-owia",
    "fire": "urhie",
    "name": "erhan",
    "money": "owo",
    "school": "ikpoba",
    "book": "ebo",
    "run": "khiagbe",
    "eat": "ya"
}


languages = {
    "hausa": hausa,
    "yoruba": yoruba,
    "igbo": igbo,
    "edo": edo,
}

print("Language Translator")
print("Choose a Language: hausa,yoruba,igbo,edo, ")

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