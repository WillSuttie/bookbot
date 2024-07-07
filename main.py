def main():
    
    input_file = "books/frankenstein.txt"
    file_contents = get_book_text(input_file)
    word_list = word_counter(file_contents)
    character_dictionary = character_counter(file_contents)
    character_reporter(character_dictionary, word_list, input_file)
    



def character_reporter(character_dictionary, word_list, input_file ):
    
    ordered_dictionary = {}

    while character_dictionary:
        highest = (None, float('-inf'))
        for char, count in character_dictionary.items():
            if count > highest[1]:
                highest = (char, count)
        
        
        ordered_dictionary[highest[0]] = highest[1]
        
        
        del character_dictionary[highest[0]]

    print(f"--- Begin report of {input_file} ---")
    print(f"{len(word_list)} words found in the document")
    print(" ")
    for char in ordered_dictionary:
        print(f"{char} appeared {ordered_dictionary[char]} times.")
    print("--- End Report ---")


def get_book_text(input_file):
    with open(input_file) as f:
        file_contents = f.read()
        return file_contents

def word_counter(input_string):
    words = input_string.split()
    return words

def character_counter(input_string):
    character_count = {}
    
    for char in input_string:
        char = char.lower()
        
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else: character_count[char] = 1
    
    return character_count

main()