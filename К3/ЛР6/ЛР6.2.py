def max_digits_substring(s, k):
    max_count=0
    result=""
    for i in range(len(s)-k+1):
        substring=s[i:i+k]
        count_digits=sum(ch.isdigit()for ch in substring)
        if count_digits>max_count:
            max_count=count_digits
            result=substring
    return result
s="ab12c345d"
k=4
print(max_digits_substring(s, k))
