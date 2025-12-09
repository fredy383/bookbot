def counting_words(text):

    words = text.split()

    return len(words)

def counting_characters(text):

    text = text.lower()

    counts = {}

    for character in text:

        if character in counts:
            counts[character] +=1
        else:
            counts[character] =1

    return counts

def sort_on(items):
    return items["num"]

def ranger(characters_dict):
    l = []
    for key, value in characters_dict.items():
        d = {}
        if key.isalpha() == True:
            d["char"] = key
            d["num"]= value
            l.append(d)

    l.sort(reverse=True, key=sort_on)
    return l
    