def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="G"
            else:
                translation+="g"
        else:
            translation+=letter
    return translation

p=input("Enter word: ")
print(translate(p))