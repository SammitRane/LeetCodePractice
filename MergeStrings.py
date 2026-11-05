from itertools import zip_longest

class MergeStrings:
    def mergeAlternately(self, word1, word2):
        final = ''
        for char1, char2 in zip_longest(word1, word2,fillvalue=""):
            final = final+char1
            final=final+char2

        return final
    
if __name__ == "__main__":
    word1 = "anagram"
    word2 = "nagaram"
    print(MergeStrings().mergeAlternately(word1,word2))     