# Program to sort alphabetically the words form a string provided by the user

# Define sentence
word = "Hello this Is an Example With cased letters"

# Split string by space, then sort the splitted string, and then put the string back together
word = ' '.join( sorted( word.split() ) )


# word.split()    - Splits string by space
# sorted()        - Sorts array of string
# ' '.join()      - Joins the string array together with a space
print(word)
