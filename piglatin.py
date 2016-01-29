# 1. get word
# 2. make sure it's only letters; if it isn't, send "Sorry, that's not a word!" -> quit
# 3. is front letter a vowel
    # 3a. add a w to the back
# 4. else
    # 4a. take off front letter
    # 4b. shove it on the back
    # 4c. if front letter is not a vowel
        # 4ca. take off front letter
        # 4cb. shove it on the back
# 6. add "ay" to the end
# 7. print your new string! :)

print("Malachi's pig latin translator")

text=raw_input("Type in a word to translate to Pig Latin: ")
if text.isalpha():
    v = ["a","e","i","o","u"]
    if text[0] in v:
        text+="w"
    else:
        f = text[0]
        text=text[1:]
        text+=f
        if text[0] not in v:
            f=text[0]
            text=text[1:]
            text+=f 
    text+="ay"
    print(text)

else :
    print("sorry that is not a word")
