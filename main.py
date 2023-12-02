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

        #print(f"The {book_path} has {num_words} word(s).")
        
        alpha_count, non_alpha_count = character_count(text)



        alpha_count_ordered, non_alpha_count_ordered = character_sorter(alpha_count, non_alpha_count)


        #print(f"The {book_path} has the following letter counts:\n{alpha_count}\nand the following character counts:\n{non_alpha_count}")
        text_report(book_path, num_words, alpha_count_ordered,non_alpha_count_ordered)


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
    # Initialize two lists to store alphabetic and non-alphabetic characters
    alpha_chars = []
    non_alpha_chars = []

    # Convert the input text to lowercase
    lower_text = text.lower()

    # Iterate over each character in the lowercased text
    for char in lower_text:
        # If the character is alphabetic, add to the alpha_chars list
        if char.isalpha():
            alpha_chars.append(char)
        # If the character is not alphabetic, add to the non_alpha_chars list
        else:
            non_alpha_chars.append(char)

    # Initialize a dictionary to store the count of each alphabetic character
    alpha_count = {}
    # Iterate over each character in the alpha_chars list
    for letter in alpha_chars:
        # If the character is already in the dictionary, increment its count
        if letter in alpha_count:
            alpha_count[letter] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            alpha_count[letter] = 1

    # Initialize a dictionary to store the count of each non-alphabetic character
    non_alpha_count = {}
    # Iterate over each character in the non_alpha_chars list
    for char in non_alpha_chars:
        # If the character is already in the dictionary, increment its count
        if char in non_alpha_count:
            non_alpha_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            non_alpha_count[char] = 1

    # Return the two dictionaries, one for alphabetic character counts and one for non-alphabetic character counts
    return alpha_count, non_alpha_count

def character_sorter(alpha_count, non_alpha_count):
    alpha_count_ordered = []
    non_alpha_count_ordered = []
    #print(alpha_count)

    for char, count in alpha_count.items():
        alpha_count_ordered.append((char, count))

    alpha_count_ordered.sort()
    for char, count in non_alpha_count.items():
        non_alpha_count_ordered.append((char, count))
    
    non_alpha_count_ordered.sort()
    #print(alpha_count_ordered)
    return alpha_count_ordered, non_alpha_count_ordered


def text_report(text_path, num_words, alpha_count_ordered, non_alpha_count_ordered):
    print(f"--- Begin report of {text_path} ---")
    print(f"{num_words} words found\n\n")    
    for char, count in alpha_count_ordered:
        print(f"The '{char}' character was found '{count}'times")
    for char, count in non_alpha_count_ordered:
        print(f"The '{char}' character was found '{count}'times")
    print(f"--- End report ---")

# Call the main function to execute the program
main()



