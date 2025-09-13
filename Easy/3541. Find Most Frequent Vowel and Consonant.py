class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        max_vowel = 0
        max_consonant = 0

        for ch in s:
            count = s.count(ch)
            if ch in vowels:
                if count > max_vowel:
                    max_vowel = count
            else:
                if count > max_consonant:
                    max_consonant = count

        return max_vowel + max_consonant
