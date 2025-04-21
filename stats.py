def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def get_num_chars(file_contents):
    result = {}
    for char in file_contents.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(char_dict):
    entries = []
    result = []

    for char in char_dict:
        if char.isalpha():
            entry = {"char": char, "num": char_dict[char]}
            entries.append(entry)

    entries.sort(reverse=True, key=sort_on)
    for entry in entries:
        result.append(f"{entry["char"]}: {entry["num"]}")

    return result

