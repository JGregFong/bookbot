def get_num_words(text):
    number = 0
    for word in text.split():
        number+=1

    return number

def get_num_letters(text):
    letters = {
        
    }
    for word in text.split():
        string = word.lower()
        for char in string:
            letters.setdefault(char,0)
            letters[char] +=1  
    return letters
def sort_on(items):
    return items["num"]
def sorted_dictionary(original_list):
    dictionary_list = []
        
    for item in original_list:
        info = {
            "char" : item,
            "num" : original_list[item]
        }
        dictionary_list.append(info)

    dictionary_list.sort(reverse=True, key=sort_on)    
    return dictionary_list

