class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter_obj = Counter(nums)

        items_list = list(counter_obj.items())

        sorted_d = sorted(items_list, key = lambda x : x[-1],reverse=True)

        top_frequent = [i[0] for i in sorted_d]

        if k <= len(top_frequent):
            return top_frequent[:k]
        return False
    