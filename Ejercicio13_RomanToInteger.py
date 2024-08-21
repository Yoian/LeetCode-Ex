class Solution:
    def romanToInt(self, s: str) -> int:
        NumRom = [x for x in s]
        NumInt=0

        for i in range(len(NumRom)-1):
            if NumRom[i]+NumRom[i+1] == 'IV':
                NumInt=NumInt+4
                NumRom[i]=""
                NumRom[i+1]=""
            elif NumRom[i]+NumRom[i+1] == 'IX':
                NumInt=NumInt+9
                NumRom[i]=""
                NumRom[i+1]=""
            elif NumRom[i]+NumRom[i+1] == 'XL':
                NumInt=NumInt+40
                NumRom[i]=""
                NumRom[i+1]=""
            elif NumRom[i]+NumRom[i+1] == 'XC':
                NumInt=NumInt+90
                NumRom[i]=""
                NumRom[i+1]=""
            elif NumRom[i]+NumRom[i+1] == 'CD':
                NumInt=NumInt+400
                NumRom[i]=""
                NumRom[i+1]=""
            elif NumRom[i]+NumRom[i+1] == 'CM':
                NumInt=NumInt+900
                NumRom[i]=""
                NumRom[i+1]=""

        for i in NumRom:
            if i == 'I':
                NumInt=NumInt+1
            elif i == 'V':
                NumInt=NumInt+5
            elif i == 'X':
                NumInt=NumInt+10
            elif i == 'L':
                NumInt=NumInt+50
            elif i == 'C':
                NumInt=NumInt+100
            elif i == 'D':
                NumInt=NumInt+500
            elif i == 'M':
                NumInt=NumInt+1000

        return NumInt