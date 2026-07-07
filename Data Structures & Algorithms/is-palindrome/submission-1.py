class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0

        while i < len(s):

            if ord(s[i]) >= 65 and ord(s[i]) <= 90:

                s = s[:i] + s[i].lower() + s[i+1:len(s)]
            
            elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            
                pass
            
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:

                pass
            
            else:   

                s = s[:i] + s[i+1:]
                i-=1
            
            i += 1
            
        print(s)

        left = 0

        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:

                return False

            else:

                left += 1

                right -= 1
        
        return True
        