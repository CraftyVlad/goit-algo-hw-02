from collections import deque


def is_palindrome(text):
    text = text.replace(" ", "").lower()

    char_deque = deque(text)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


text = input("enter text: ")

if is_palindrome(text):
    print("the text is a palindrome")
else:
    print("the text is not a palindrome")