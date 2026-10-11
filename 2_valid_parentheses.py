class Solution:
    def isValid(self, s: str):
        hash_map = {')':'(','}':'{',']': '['}
        stack = []
        for char in s:
            if char in hash_map:
                curr = stack.pop() if stack else '#'
                if hash_map[char] != curr:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0