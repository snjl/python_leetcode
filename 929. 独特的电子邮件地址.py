class Solution:
    def numUniqueEmails(self, emails) -> int:
        s = set()

        for email in emails:
            # 标志后面需要被忽略，一直到@
            flag = 0
            real_email = ''
            for i in range(len(email)):
                # 如果前面有+，且未到@，则一直忽略
                if flag == 1 and email[i] != '@':
                    continue
                elif email[i] == '@':
                    break
                if email[i] == '.':
                    continue
                elif email[i] == '@':
                    break
                elif email[i] == '+':
                    flag = 1
                else:
                    real_email += email[i]
            real_email += email[i:]
            s.add(real_email)

        return len(s)

    def numUniqueEmails2(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.', '') + '@' + domain)
        return len(seen)



if __name__ == '__main__':
    x = Solution()

    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    print(x.numUniqueEmails(emails))
    # s = set()


