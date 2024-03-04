# https://leetcode.com/problems/restore-ip-addresses/
# 12 min 14 sec

from typing import List

class Solution:
    def validate_ip(self, ip: List[str]) -> bool:
        if len(ip) != 4:
            return False
        try:
            for i in ip:
                if len(i) > 1 and i[0] == "0":
                    return False
                integer = int(i)
                if integer < 0 or integer > 255:
                    return False
        except ValueError:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        for x in range(1,len(s)):
            for y in range(x+1,len(s)):
                for z in range(y+1,len(s)):
                    ip = [s[0:x], s[x:y], s[y:z], s[z:len(s)]]
                    if self.validate_ip(ip):
                        output.append('.'.join(ip))
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreIpAddresses("0000"))
    print(solution.restoreIpAddresses("25525511135"))