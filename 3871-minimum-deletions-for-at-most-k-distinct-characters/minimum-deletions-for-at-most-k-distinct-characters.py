class Solution(object):
    def minDeletion(self, s, k):
        k_freq = {}
        for i in s:
            if i in k_freq:
                k_freq[i] += 1
            else:
                k_freq[i] = 1
        
        if len(k_freq) <= k:
            return 0
        
        c = 0
        p = sorted(k_freq.values())
        for i in range(len(p) - k):
            c += p[i]
        
        return c
