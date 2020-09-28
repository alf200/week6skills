word_one = input("Enter a word:").casefold().strip() 
word_two = input("Enter another word").casefold().strip() 

word_one_list = list(word_one) 


anagram = f"{word_one} and {word_two} are anagrams!"
not_anagram = f"{word_one} and {word_two} are not anagrams!"

check_anagram = True

if len(word_one) != len(word_two):
    check_anagram = False
else:
    for x in word_one_list:
        if word_one.count(x) != word_two.count(x):
            check_anagram = False

if check_anagram:
    print(anagram)
else:
    print(not_anagram)