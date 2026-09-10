class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def decode(s,i, result) :
            if i == n :
                result[i] = 1
                return result[i]
            if s[i] == '0' :
                result[i]=0
                return result[i]
            if i in result :
                return result[i]
            one_digit = decode(s,i+1,result)
            two_digit = 0
            if i+1<n and 10<=int(s[i:i+2])<=26 :
                two_digit = decode(s,i+2, result)
            result[i] = one_digit + two_digit
            return result[i]
            
        return decode(s,0, {})
