def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_list = list(chars_dict.items())
    sorted_chars = sorted(chars_list, key=sort_on, reverse=True)
    print(f"---Begin Report of {book_path}---")
    print(f"{num_words} words found in the document")
    print("")
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")
    print("---End Report---")


def sort_on(list):
    return list[1]


def get_num_chars(text):
    words = text.split()
    chars_dict = {}
    for word in words:
        chars = list(word)
        for char in chars:
            lower_char = char.lower()
            if lower_char not in chars_dict:
                chars_dict[lower_char] = 1
            elif lower_char in chars_dict:
                chars_dict[lower_char] += 1

    return chars_dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
