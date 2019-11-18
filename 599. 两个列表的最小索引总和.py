class Solution:
    def findRestaurant(self, list1, list2):
        map = dict()
        m = float('inf')
        map2 = dict()
        answers = list()
        for i in range(len(list1)):
            map[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in map.keys():
                # 计算索引总和
                map2[list2[i]] = i + map[list2[i]]

        for k in map2.keys():
            if map2[k] == min(map2.values()):
                answers.append(k)
        return answers


if __name__ == '__main__':
    x = Solution()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

