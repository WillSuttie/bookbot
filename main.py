def main():
    
    input_file = "books/frankenstein.txt"
    file_contents = get_book_text(input_file)
    word_list = word_counter(file_contents)
    print (len(word_list))
    


def get_book_text(input_file):
    with open(input_file) as f:
        file_contents = f.read()
        return file_contents

def word_counter(string):
    words = string.split()
    return words

main()