#  in this question we need to find the longest prefix a word can have compared to the other two 

def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        
        return prefix