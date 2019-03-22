from py2neo import Node, Relationship, Graph

graph = Graph("http://neo4j.shusnjl.cn:7474/db/data/", user='neo4j', password='snjl')
# data = graph.data('MATCH (n1)-[r]->(n2) RETURN r, n1, n2 LIMIT 25')

a = Node('Person', name='Alice', age=12)
b = Node('Person', name='Bob')
a['age'] = 44
r = Relationship(a, 'KNOWS', b)
r['time'] = '2017/08/31'
# print(a, b, r)
