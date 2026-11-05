from collections import Counter

class DifferenceFinder:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]

if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    print(DifferenceFinder().findTheDifference(s, t))