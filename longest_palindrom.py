def longestPalindrome(s):
    # Create a string to store our resultant palindrome
    palindrome = ''
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            print(s[i:j])
            if len(palindrome) >= j-i:
                break

            elif s[i:j] == s[i:j][::-1]:
                palindrome = s[i:j]
                break
    
    return palindrome

s='abaaba'
result = longestPalindrome(s)
print(result)