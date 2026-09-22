from typing import List


class Solution:
    def DeleteTillDub(self, temp, s2, dub, st, s1_c) -> tuple[int,int]:
        while s2[st] != dub:
            temp[s2[st]] -= 1
            st += 1
            s1_c -= 1
        st += 1

        return st, s1_c

    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        dic = {}
        lp = len(p)

        for i in range(0, lp):
            if dic.get(p[i]) is None:
                dic[p[i]] = 1
            else:
                dic[p[i]] += 1

        ls = len(s)
        temp = {}
        st = 0
        p_c = 0
        for i in range(0, ls):
            if p_c >= lp:
                res.append(st)
                temp[s[st]] -= 1
                st += 1
                p_c -= 1
            if dic.get(s[i]) is not None:
                if temp.get(s[i]) is None or temp[s[i]] == 0:
                    temp[s[i]] = 1
                    p_c += 1
                elif temp[s[i]] >= dic[s[i]]:
                    st, p_c = self.DeleteTillDub(temp,s, s[i], st, p_c)
                else:
                    temp[s[i]] += 1
                    p_c += 1
            else:
                while st < i:
                    temp[s[st]] -= 1
                    st += 1
                    p_c -= 1
                st += 1
        if p_c >= lp:
            res.append(st)
            temp[s[st]] -= 1
            st += 1
            p_c -= 1
        return res




sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s,p))