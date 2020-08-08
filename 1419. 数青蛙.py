class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        num = 0
        while "croak" in croakOfFrogs:
            croakOfFrogs = croakOfFrogs.replace("croak","")
            num += 1
        if num == 0:
            return -1
        else:
            return num



if __name__ == '__main__':
    x = Solution()

    print(x.minNumberOfFrogs("crcoakroak"))