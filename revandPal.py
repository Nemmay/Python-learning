def reverse(word):
    reverseText = word[::-1]
    return reverseText
def palindrome(word):
    if word == reverse(word):
        return True
    else:
        return False
word = input("Enter word: ")
print("The word {} is a palindrome. This statement is {}.".format(word,palindrome(word)))
print("{} reversed is {}.".format(word, reverse(word)))