class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        strs[strs.index(min(strs,key=len))],strs[0]=strs[0],strs[strs.index(min(strs,key=len))]

        for i in strs[1:]:
            
            for j in range(len(strs[0])):
                if i[0:len(strs[0])] != strs[0]:
                    strs[0] = strs[0][:-1]
                else: break

                if strs[0]=="": return "No hay prefijo"

        return "El prefijo es"+strs[0]

Hola=Solution()
print(Hola.longestCommonPrefix(["flower","flow","arbolflo"]))

