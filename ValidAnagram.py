class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = False
        sorted_t = ''.join(sorted(t))
        sorted_s =''.join(sorted(s))
        if sorted_t == sorted_s:
            anagram = True
        return anagram


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(ValidAnagram().isAnagram(s, t))