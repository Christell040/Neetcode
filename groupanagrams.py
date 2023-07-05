
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))

            anagrams[sorted_word].append(word)

            result = list(anagrams.values())

        return result   
