#Time Complexity: O(n^2)
#Space Complexity: O(n^2)
#Approach: Dijskra's 
#Time Limit Exceeded
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        word_set = set()
        max_word_len = 0

        for word in words:
            max_word_len = max(max_word_len, len(word))
            for i in range(1, min(len(word), len(target)) + 1):
                word_set.add(word[:i])
        
        heap = []
        heapq.heappush(heap, (0, "")) 
        
        visited = set()
        
        while heap:
            curr_dist, curr_word = heapq.heappop(heap)
            
            if curr_word in visited:
                continue
            visited.add(curr_word)
            
            if curr_word == target:
                return curr_dist
            
            next_start = len(curr_word)
            for end in range(next_start + 1, min(len(target), next_start + max_word_len) + 1):
                next_part = target[next_start:end]
                
                if next_part in word_set:
                    next_word = curr_word + next_part
                    
                    if next_word not in visited:
                        heapq.heappush(heap, (curr_dist + 1, next_word))
        
        return -1
