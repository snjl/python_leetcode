class Solution:
    def subdomainVisits(self, cpdomains):
        m = dict()
        for time_domains in cpdomains:
            time, domains = time_domains.split(' ')
            time = int(time)
            m[domains] = m.get(domains, 0) + time
            while domains.find('.') != -1:
                domains = domains[domains.find('.') + 1:]
                m[domains] = m.get(domains, 0) + time
        s= list()
        for k,v in m.items():
            s.append('{} {}'.format(v,k))
        return s
