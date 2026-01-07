import sys
from stats import get_num_words, get_num_letters, sorted_dictionary
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    print("Usage: python3 main.py <path_to_book>")
    #print(sys.argv)
 
    book_link= sys.argv[1]
    num_words = get_num_words(get_book_text(book_link))
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_link + "...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    dictionary = get_num_letters(get_book_text(book_link))
    updated_dictionary = sorted_dictionary(dictionary)
    print("--------- Character Count -------")
    for entry in updated_dictionary:
        print(entry["char"] + ": " + str(entry["num"]))
    
    print("============= END ===============")


    #sys.exit(1)


main()