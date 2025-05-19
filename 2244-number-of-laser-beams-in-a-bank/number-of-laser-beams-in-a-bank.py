class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        c=0
        i = 0
        while i < len(bank):
            if bank[i].count('1') == 0:
                bank.pop(i)
            else:
                i += 1
        for i in range(len(bank)-1):
            l1=bank[i].count('1')
            l2=bank[i+1].count('1')
            c+=l1*l2
        return c