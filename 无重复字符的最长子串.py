class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0
        fast = 0
        ret_ans = 0
        table = dict()

        while slow < len(s) and fast < len(s):
            # if find duplicated, slide window(slow+1)
            if s[fast] in table:
                del (table[s[slow]])
                slow += 1
            # if not duplicated, prolong the window（fast+1）
            else:
                table[s[fast]] = fast
                fast += 1
                ans = fast - slow
                ret_ans = max(ret_ans, ans)
        return ret_ans