#Time Complexity: O(n*m)
#Space Complexity: O(n)
#Approach: Lists
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        output = []
        for word in sentence:
            current = word
            for i in dictionary:
                if word.startswith(i):
                    if len(current) > len(i):
                        current = i
            output.append(current)
        return " ".join(output)
