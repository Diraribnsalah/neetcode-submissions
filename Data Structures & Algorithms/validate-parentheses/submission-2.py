class Solution:
    def isValid(self, s: str) -> bool:
        refrence = {
            "]" : "[", "}" : "{", ")" : "("
        }
        symbols = []
        if len(s) == 0 :
            return False
        for i in range(len(s)) : 
            if s[i] == "[" or s[i] == "{" or s[i] == "(" : 
                symbols.append(s[i]) 
            elif s[i] == "]" or s[i] == "}" or s[i] == ")" :
                if len(symbols) == 0 or symbols.pop() != refrence[s[i]] :
                    return False
        return len(symbols) == 0 