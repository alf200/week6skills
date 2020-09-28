word_one = input("Enter a word:").casefold().strip() 
word_two = input("Enter another word").casefold().strip() 

word_one_list = list(word_one) 


anagram = f"{word_one} and {word_two} are anagrams!"
not_anagram = f"{word_one} and {word_two} are not anagrams!"

check_anagram = True
