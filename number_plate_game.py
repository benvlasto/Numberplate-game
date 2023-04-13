def number_plate_game():
    
    first_letter = input("First letter: ").upper()
    second_letter = input("Second letter: ").upper()
    third_letter = input("Third letter: ").upper()
    print()

    dictionary = open("unix_word_list.txt", "r")
    words = dictionary.readlines()
    
    for word in words:
        word = word.strip()
        
        if len(word) < 3:
            continue
        
        word = word.upper()
        first_char_pos = find_letter(word, first_letter)
        if first_char_pos == -1 or first_char_pos > len(word) - 3:
            continue
        
        sub_word = word[first_char_pos + 1:]
        second_char_pos = find_letter(sub_word, second_letter)
        if second_char_pos == -1 or second_char_pos > len(word) - 2:
            continue
        
        sub_sub_word = sub_word[second_char_pos + 1:]
        if third_letter in sub_sub_word:
            print(word)

    print()
    number_plate_game()

def find_letter(string, letter):
    if letter in string:
        return string.find(letter)
    else:
        return -1

number_plate_game()
