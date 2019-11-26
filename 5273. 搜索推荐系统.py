class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        search_result = list()
        for i in range(1, len(searchWord) + 1):
            # print(searchWord[:i])
            l = list()
            for product in products:
                if product[:i] == searchWord[:i]:
                    l.append(product)
                if len(l) == 3:
                    break
            search_result.append(l)
            # print(l)

        # print(search_result)
        return search_result

if __name__ == '__main__':

    x= Solution()



    # products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    # searchWord = "mouse"

    products = ["havana"]
    searchWord = "sdfs"

    products.sort()
    search_result = list()
    for i in range(1,len(searchWord) + 1):
        print(searchWord[:i])
        l = list()
        for product in products:
            if product[:i] == searchWord[:i]:
                l.append(product)
            if len(l) == 3:
                break
        search_result.append(l)
        print(l)

    print(search_result)


    # print(x.suggestedProducts(products,searchWord))

