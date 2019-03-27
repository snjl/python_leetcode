class Solution1:
    def findContentChildren(self, children: list, cookies: list) -> int:
        children.sort()
        cookies.sort()
        num = 0
        for child in children:
            for cookie in cookies:
                if child <= cookie:
                    cookies.remove(cookie)
                    num += 1
                    break
        return num

class Solution:
    def findContentChildren(self, children: list, cookies: list) -> int:
        children.sort()
        cookies.sort()
        num = 0
        child_index = 0
        cookie_index = 0
        while child_index < len(children) and cookie_index < len(cookies):
            if children[child_index] <= cookies[cookie_index]:
                num += 1
                child_index += 1
                cookie_index += 1
            else:
                cookie_index += 1
        return num


if __name__ == '__main__':
    children = [10, 9, 8, 7]
    cookies = [5, 6, 7, 8]


    children.sort()
    cookies.sort()
    num = 0
    child_index = 0
    cookie_index = 0
    while child_index < len(children) and cookie_index < len(cookies):
        if children[child_index] <= cookies[cookie_index]:
            num += 1
            child_index += 1
            cookie_index += 1
        else:
            cookie_index += 1
    print(num)