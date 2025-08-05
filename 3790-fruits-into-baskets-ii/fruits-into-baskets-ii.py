class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for i in fruits:
            for j in range(len(baskets)):
                if i <=baskets[j]:
                    c+=1
                    baskets[j]=-1
                    break
        return len(fruits)-c