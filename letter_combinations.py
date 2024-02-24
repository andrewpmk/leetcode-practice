# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Time to solve: 19 min 30 sec
# Time complexity O(4^n)
# Space complexity O(4^n + n)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        mapping = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        first = digits[0]
        if first not in mapping.keys():
            raise ValueError
        second = digits[1:]
        combos1 = mapping[first]
        if second == "":
            return combos1
        combos2 = self.letterCombinations(second)
        # Combine all combinations of first and second
        output = []
        for i in range(len(combos1)):
            for j in range(len(combos2)):
                output.append(combos1[i] + combos2[j])
        return output

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations(""))
    print(s.letterCombinations("2"))
    print(s.letterCombinations("23"))
    print(s.letterCombinations("234"))