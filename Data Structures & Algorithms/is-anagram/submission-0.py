class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        char_counts = {}

        for char_s , char_t in zip(s,t) :
            char_counts[char_s] = char_counts.get(char_s , 0) + 1
            char_counts[char_t] = char_counts.get(char_t , 0) - 1  

        return all(char_iter == 0 for char_iter in  char_counts.values())              