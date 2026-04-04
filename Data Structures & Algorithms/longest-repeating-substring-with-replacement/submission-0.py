class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_frequencies = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            max_frequencies = max(max_frequencies, count[s[right]])

            if (right - left +1) - max_frequencies > k:
                count[s[left]] = count.get(s[left]) - 1
                left += 1
        return right - left + 1