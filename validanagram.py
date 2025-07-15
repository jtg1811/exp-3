class Solution:
    def validanagram(self,str1,str2) :
        counting1 = {}
        counting2 = {}

        for n in str1:
            if n in counting1 :
                counting1[n] += 1
            else:
                counting1[n] = 1
        for n in str2:
            if n in counting2 :
                counting2[n] += 1
            else:
                counting2[n] = 1
    
        if counting1 == counting2:
            return True
    
        return False

s = Solution()
print(s.validanagram("anagram", "nagaram")) 