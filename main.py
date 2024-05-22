def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars_dict(chars_dict)
    print("--- Begin report of {} ---".format(book_path))
    print(f"{num_words} words found in the document\n")
    
    for char in sorted_chars:
        print(f"The '{char['name']}' character was found{char['num']} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def sort_chars_dict(chars):
    char_list = [{"name": k, "num": v} for k, v in chars.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)

def get_book_text(path):
    with open(path) as f:
        return f.read()   


main()
