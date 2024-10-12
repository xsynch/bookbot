def countWords(book):
    wordCount = 0
    for line in book:
        wordCount = wordCount + len(line.split())
    return wordCount

def duplicateChars(book_text):
    char_dict = {}
    for line in book_text:
        text_new = "".join(line.split())
        for char in text_new:
            if char.isalpha():
                if char.lower() in char_dict.keys():
                    char_dict[char.lower()] += 1
                else:
                    char_dict[char.lower()] = 1
    return char_dict 

def print_report(book_dict):
    sortedBookChars = sorted(book_dict.items(), key=lambda item: item[1])
    sortedBookChars.reverse()    
    for i in sortedBookChars:
        print(f"The '{i[0]}' character was found {i[1]} times")

output = ""

with open("./books/frankenstein.txt","r") as f:
    output = f.readlines()

print("--- Begin report of books/frankenstein.txt ---")

print(f"{countWords(output)} found in the document\n\n\n")
duplicatCharsFound = duplicateChars(output)
# print(duplicatCharsFound)
print_report(duplicatCharsFound)
print("--- End report ---")


# for line in output:
#     print(line)
