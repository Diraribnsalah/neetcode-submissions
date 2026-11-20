class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string 

        s = s.replace(" " , "")
        valid_chars = set(string.ascii_lowercase + string.digits)
         

        right = len(s) - 1 
        left = 0
        
        while left < right :
            if s[left].lower() not in valid_chars  :
                left +=  1
            elif s[right].lower() not in  valid_chars :
                right -=  1   
            elif s[left].lower() != s[right].lower() :
                return False

            else :
                right -= 1
                left += 1    
        return True
 
