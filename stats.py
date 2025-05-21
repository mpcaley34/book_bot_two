def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    new_text = str(text.split())
    char_dict = {}
    for char in new_text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sorted_list_of_dictionaries(char_dict):
    # Returns a sorted list of dictionaries

    for char, value in sorted(char_dict.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            value = char_dict[char]
            print(f"{char}: {value}")
