def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_counts = {}


    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_characters(char_dict):
     # Liste bauen aus Dictionaries
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():   # nur Buchstaben erlauben
            sorted_list.append({
                "char": char,
                "num": count
            })

 # sortieren – von groß nach klein
    def sort_key(item):
        return item["num"]

    # Sortieren von groß nach klein
    sorted_list.sort(key=sort_key, reverse=True)

    return sorted_list
