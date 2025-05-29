class Solution:
    def countStudents(self, stu: List[int], sand: List[int]) -> int:
        c=0
        while stu and c<len(stu):  
            if stu[0]==sand[0]:
                stu.pop(0)
                sand.pop(0)
                c=0
            else:
                s=stu.pop(0)
                stu.append(s)
                c+=1
        return len(stu)