"""
def main():
    book_path = "books/test-file.txt"
    text = get_book_text(book_path)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
"""

def main():
    # Set the path to the book file
    book_path = "books/frankenstein.txt"

    try:
        # Attempt to get the text from the book file
        text = get_book_text(book_path)
        # Print the text obtained from the book file
        # print("Main function text:", text)
        num_words = text_count(text)

        print(f"The {book_path} has {num_words} word(s).")
        
        num_character = character_count(text)

        print(f"The {book_path} has {num_character} letter(s).")


    except Exception as e:
        # Handle any exceptions that might occur during the process
        print(f"Error in main function: {e}")



def get_book_text(path):
    try:
        # Attempt to open and read the content of the specified file
        with open(path) as f:
            # Read the content of the file
            content = f.read()
        # Print the content obtained from the file
        # print("File content:", content)
        # Return the content of the file
        return content
    except Exception as e:
        # Handle any exceptions that might occur during the process
        print(f"Error reading the file: {e}")
        # Raising the exception again for further debugging or propagation
        raise

def text_count(text):
    #convert text to string
    #split string
    words = text.split()
    #count the words in the list
    return len(words)

def character_count(text):
    letter_count = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


# Call the main function to execute the program
main()



