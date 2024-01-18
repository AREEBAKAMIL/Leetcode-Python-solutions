class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lgi = None
        for digit in range(9, -1, -1):
            if(s:= str(digit) * 3) in num:
                lgi = s
                return lgi
        if lgi is None:
            return str("")
        
    
if __name__ == "__main__": 
    sol = Solution()
    print(sol.largestGoodInteger("6777133339"))
    print(sol.largestGoodInteger("2300019"))
    print(sol.largestGoodInteger("42352338"))
