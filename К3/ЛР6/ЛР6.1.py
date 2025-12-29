def is_palindrome(s):
    s=s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
text="А роза упала на лапу Азора"
print(is_palindrome(text))
