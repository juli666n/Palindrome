word = input("write a word to check if is palindrome or not\n")
wordinv = word[::-1]
if word==wordinv:
    print("palindrome")
else:
    print("not palindrome")
