class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0

        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x) + 1:]
                print("str= ", str_list)

            str_list.append(x)
            max_length = max(max_length, len(str_list))

        return max_length


sub = Solution()
p = sub.lengthOfLongestSubstring("abcabcbb")
print(p)