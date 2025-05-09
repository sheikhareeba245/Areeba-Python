# Problem: Count Unique Words in a Sentence 
# Question:Write a Python program that takes a sentence as input and counts the number of unique words using a set.
# Ignore case sensitivity (e.g., "Apple" and "apple" should be treated as the same).
sentence=input("Enter your sentence: ")
words=sentence.lower().split()
unique_words=set(words)
print("Unique words: ",unique_words)
print("Total lenght of your unique words: ",len(unique_words))
