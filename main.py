def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document /n")
    sorted_letter_list = sort_letter_list(text)
    for letter in sorted_letter_list:
        print(f"{letter[0]} and {letter[1]}")

def sort_number(d):
    return d[1]

def sort_letter_list(text):
    letter_list = get_letter_list(text)
    letter_list.sort(reverse=True, key=sort_number)
    return letter_list

def get_letter_list(text):
    letter_dict = count_letters(text)
    letter_list = []
    for letter in letter_dict:
        letter_list.append([letter,letter_dict[letter]])
    return letter_list

def count_letters(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    letter_count.items()
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()