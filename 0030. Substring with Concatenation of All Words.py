#Time Complexity: O(n*m)
#Space Complexity: O(n*m)
#Approach: Freq Map, Set, Sliding Window, Dynamic Programming 
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = {}
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        length = len(words[0])
        res = []
        perm = set()
        for i in range(len(s) - len(words) * length + 1):
            if(s[i:i+length*len(words)] in perm):
                res.append(i)
                continue
            j = i
            _dic = dic.copy()
            while s[j:j+length] in _dic and _dic[s[j:j+length]] > 0:
                _dic[s[j:j+length]] -= 1
                j += length
            if (j - i) // length == len(words):
                res.append(i)
                perm.add(s[i:i+length*len(words)])
        return res
