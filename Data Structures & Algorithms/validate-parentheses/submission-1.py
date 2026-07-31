class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for bracket in s:
            b = bracket_map.get(bracket, None)
            print(f"bracket = {bracket}, b={b}", end=",")
            if b and b in stack:
                popped = stack.pop()
                if popped != b:
                    return False
            else:
                stack.append(bracket)
                print(f" stack= {stack} - append")

        return len(stack) == 0
        