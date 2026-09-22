from typing import List


class Solution:
    def DeleteTillDub(self, temp, s2, dub, st, s1_c) -> tuple[int,int]:
        while s2[st] != dub:
            temp[s2[st]] -= 1
            st += 1
            s1_c -= 1
        st += 1

        return st, s1_c

    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        ls1 = len(s1)
        for i in range(0, ls1):
            if dic.get(s1[i]) is None:
                dic[s1[i]] = 1
            else:
                dic[s1[i]] += 1

        temp = {}
        s1_c = 0
        ls2 = len(s2)
        st = 0
        for i in range(0, ls2):
            if s1_c >= ls1:
                return True
            if dic.get(s2[i]) is not None:
                if temp.get(s2[i]) is None or temp[s2[i]] == 0:
                    temp[s2[i]] = 1
                    s1_c += 1
                elif temp[s2[i]] >= dic[s2[i]]:
                    st, s1_c = self.DeleteTillDub(temp,s2, s2[i], st, s1_c)
                else:
                    temp[s2[i]] += 1
                    s1_c += 1
            else:
                while st < i:
                    temp[s2[st]] -= 1
                    st += 1
                    s1_c -= 1
                st += 1

        if s1_c >= ls1:
            return True
        return False




sol = Solution()
s1 = "ab"
s2 = "aab"
print(sol.checkInclusion(s1,s2))