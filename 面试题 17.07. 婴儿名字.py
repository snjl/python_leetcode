
class Solution:
    def trulyMostPopular(self, names, synonyms):
        name_syn = dict()
        name_type = 0
        for syn in synonyms:
            syn = syn[1:-1].split(',')
            name1, name2 = syn

            # 两个名字都不在dict里
            if name1 not in name_syn.keys() and name2 not in name_syn.keys():
                name_syn[name1] = name_type
                name_syn[name2] = name_type
                name_type += 1
            elif name1 in name_syn.keys():
                name_syn[name2] = name_syn[name1]
            elif name2 in name_syn.keys():
                name_syn[name1] = name_syn[name2]

        name_alias = [list() for _ in range(name_type)]
        for k, v in name_syn.items():
            name_alias[v].append(k)

        name_alias_dict = dict()
        # 字典排序
        for alias in name_alias:
            alias.sort()
            name_alias_dict[alias[0]] = 0

        for name in names:
            n = name[:name.index('(')]
            num = int(name[name.index('(') + 1:-1])
            for index, alias in enumerate(name_alias):
                if n in alias:
                    name_alias_dict[alias[0]] += num
                    break

        name_alias_list = list()
        for k ,v in name_alias_dict.items():
            name_alias_list.append('{}({})'.format(k ,v))


        return name_alias_list

if __name__ == '__main__':
    x = Solution()
    names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    for name in names:
        n = name[:name.index('(')]
        num = int(name[name.index('(') + 1:-1])
        print(n, num)
    synonyms = ["(Jon,John)",
                "(Johnny,John)",
                "(Kris,Chris)",
                "(Chris,Christopher)"]

    x.trulyMostPopular(names, synonyms)
