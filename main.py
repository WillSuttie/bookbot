def main():
    
    input_file = "books/frankenstein.txt"
    file_contents = get_book_text(input_file)
    word_list = word_counter(file_contents)
    print (len(word_list))
    


def get_book_text(input_file):
    with open(input_file) as f:
        file_contents = f.read()
        return file_contents

def word_counter(input_string):
    words = input_string.split()
    return words

def charcter_counter(input_string):
    character_count = {}
    
    for char in input_string:
        char = char.lower()
        
        if char in character_count:
            character_count[char] += 1
        else: character_count[char] = 1
    
    return character_count

main()