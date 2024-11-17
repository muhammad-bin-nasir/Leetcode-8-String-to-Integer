class Solution:
    def myAtoi(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] != " ":
                s = s[i:]
                break
        if len(s)==0:
            return 0
        if s[0]=='+' or s[0]=='-':
            x=s[0]
            s = s[1:]
        else:
            x=''
        for i in range(len(s)):
            if s[i].isdigit():
                x = x+s[i]
            else:
                break
        if x=="" or x=="+" or x=="-":
            return 0
        x = int(x)
        if x < -2**31:
            return -2**31
        elif x > 2**31 -1:
            return 2**31 -1
        return x

        
