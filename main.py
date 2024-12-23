def main(path):
    with open(path) as file:
        text = file.read()
    return text

def count_words(text):
    words=text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    cahrs_dict = {}
    for char in text:
        if char.isalpha():
            if char in cahrs_dict:
                cahrs_dict[char] += 1
            else:
                cahrs_dict[char] = 1
    return cahrs_dict


def printout(bookpath):
    text = main(bookpath)
    wordcount = count_words(text)
    chars = count_chars(text)
    chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    print (f"--- Begin report of {bookpath} ---")
    print (f"{wordcount} words found in the document")
    print ("")
    for char in chars:
        print (f"The {char} character was found {chars[char]} times")
    print ("--- End report ---")
printout("books/frankenstein.txt")