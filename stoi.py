class Solution:
    # @return an integer
    def atoi(self, str):
        sig = 1
        if len(str) != 0:
            for i in range(len(str)):
                if str[i] == ' ' or str[i].isdigit() or str[i] == '-' or str[i] == '+':
                    if str[i].isdigit() or str[i] == '-' or str[i] == '+':
                        if str[i] == '-':
                            sig = -1
                            result = 0
                        elif str[i] == '+':
                            sig = 1
                            result = 0
                        else:
                            result = int(str[i])
                        i += 1
                        while i < len(str) and str[i].isdigit():
                            result = result * 10 + int(str[i])
                            i += 1
                        # handle when input  = "2147483648", expected output is "2147483647"
                        if result * sig >= 2 ** 31:
                            return 2 ** 31 - 1
                        elif result * sig < -1 * 2 ** 31:
                            return  -1 * 2 ** 31
                        else:
                            return result * sig
                else:
                    return 0
            else:
                return 0
        else:
            return 0
