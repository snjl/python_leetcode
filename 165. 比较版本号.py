class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        cursor = 0

        while cursor < len(v1) and cursor < len(v2):
            if int(v1[cursor])> int(v2[cursor]):
                return 1
            elif int(v1[cursor]) < int(v2[cursor]):
                return -1
            else:
                cursor += 1
        # 到这里表示前面的号码都相同

        if len(v1) > cursor:
            while cursor < len(v1):
                if int(v1[cursor]) > 0:
                    return 1
                cursor += 1
        if len(v2) > cursor:
            while cursor < len(v2):
                if int(v2[cursor]) > 0:
                    return -1
                cursor += 1

        return 0




if __name__ == '__main__':
    x = Solution()

    version1 = "7.5.3.0"
    version2 = "7.5.3"

    print(x.compareVersion(version1,version2))

