class Solution(object):
    def licenseKeyFormatting(self, S, K):
        key = S.replace("-", "")
        list_key = list(key)

        #count how many "-" added to list
        count = 1
        #how many places into list from the end to insert
        k = K

        #will fail if string is --- as list becomes empty, exception prevents
        try:
            while list_key[0] != "-":
                list_key.insert(-k, "-")
                count += 1
                k = ((K * count) + (count - 1))
        except:
            pass
        try:    
            list_key.pop(0)
        except:
            pass
        new_key = ''.join(list_key)
        new_key = new_key.upper()
        return new_key



x = Solution().licenseKeyFormatting("---", 3)
print(x)
