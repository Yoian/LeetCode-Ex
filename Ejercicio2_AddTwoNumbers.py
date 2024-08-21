class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        l1.reverse()
        l2.reverse()
        n1=0
        n2=0
        lout=[]

        for i in range(len(l1)):
            n1=n1+l1[i]*(10**i)
        for i in range(len(l2)):
            n2=n2+l2[i]*(10**i)

        n3=str(n1+n2)
        for i in n3:
            lout.append(int(i))
        print(n3,lout)



Hola=Solution()
Hola.addTwoNumbers([1,4,5,6,2],[2,4,6,6,2])
            