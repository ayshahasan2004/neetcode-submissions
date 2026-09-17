class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set ()
        r , l=0  ,0
        maxL=0
        while r < len(s):
            if s[r] not in seen :
                seen.add(s[r])
                maxL=max (len(seen) , maxL)
                r+=1
            else:
                seen.remove(s[l])
                l+=1
        return maxL

        