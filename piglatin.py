"""
To Do:
 - split sentence (or essay) by spaces
 - check for a capital letter at the beginning
 - make a variable for whether or not letter is capitalized
 - if it is capitalized, make it lowercase
 - check last character for punctuation
 - if it is, remove it and store it in a variable
 - at the end, stick the punctuation back on the end
"""

def isnum(ch):
    """ This function will return True if the character is a number. """
    if ord(ch) >= 48 and ord(ch) <= 57:
        return True
    return False

def char_good(ch):
    """ This function will return True if the character is a letter, apostrophe, or number. """
    if ch.isalpha() or isnum(ch) or ch == "\'":
        return True
    else:
        return False

def word_good(word):
    """ This function will return True if the word contains only letters, apostrophes, or numbers. """
    for ch in word:
        if not char_good(ch):
            return False
    return True

print("Malachi's pig latin translator")
print "Please do not add single quotes, because the computer thinks they're apostrophes."

text=raw_input("Type in something to translate to Pig Latin: ")
text = text.split()
translation = ""

for word in text:
    if word_good(word):
        # if first character is a letter
        if word[0].isalpha():
            v = ["a","e","i","o","u"]
            # if the first letter is a vowel
            if word[0] in v:
                word+="w"
            # if the first letter is not a number
            else:
                f = word[0]
                isFirstLetterUpper = False
                if f.isupper():
                    isFirstLetterUpper = True
                    f = f.lower()
                word=word[1:]
                word+=f
                if word[0] not in v:
                    f=word[0]
                    word=word[1:]
                    word+=f
                if isFirstLetterUpper:
                    word = word[0].upper() + word[1:]
        word+="ay"
    translation += word + " "

print translation
