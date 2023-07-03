
class Solution(object):
    def isAnagram(self, s, t):    
        

        a = list(s)
        b = list(t)

        count_a = Counter(a)
        count_b = Counter(b)

        
        if count_a.items() == count_b.items():
            return True
        return False