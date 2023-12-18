# In this Madlibs Generator, we have a story that contains some replaceble words
# The user chooses whatever word he wants to replace with, according to the type of word

with open("project2.txt", "r") as f: # used the open function that allows me to open the file; the mode "r" is the way which we gona read it (read mode)
    story = f.read() # gives me all the text inside the file   

# 1) We need to look for all the words in my story
    
words = set() # by using a set instead of a list, we get a single type of <word>, iontead of duplicated <words>'s
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story): # enumerate gives us access to the position as well as the element at that position
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1: # if we found the target_end bracket AND we had a starting bracket
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# 2) Now, we ask the user to give a value for each of the words

answers = {} # we gona use the dictionary 

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer


# 3) Now, we can take every single instance of these words and replace them 
    
for word in words:
    story = story.replace(word, answers[word]) # .replace method replaces every single instance of a string with another

print(story)

