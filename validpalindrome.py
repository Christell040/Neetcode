class Solution(object):
    def isPalindrome(self, s):
       
        s = s.lower()       

        def remove_non_alnum_from_string(string):
            return ''.join(x for x in string if x.isalnum())
        
        s =  remove_non_alnum_from_string(s)
        

        def ispalindrome(string):
            if string == string[::-1]:
                return True
            return False      
        
        
        return ispalindrome(s)
    