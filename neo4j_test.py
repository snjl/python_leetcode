from py2neo import Node, Relationship, Graph,NodeMatcher

graph = Graph("http://db-home.neo4j.shusnjl.cn:17474/db/data/", user='neo4j', password='snjl')
# data = graph.data('MATCH (n1)-[r]->(n2) RETURN r, n1, n2 LIMIT 25')
matcher = NodeMatcher(graph)
matcher.match("Person", name="Keanu Reeves").first()
for m in matcher:
    print(m)
a = Node('Person', name='Alice', age=12)
b = Node('Person', name='Bob')
a['age'] = 44
r = Relationship(a, 'KNOWS', b)
r['time'] = '2017/08/31'
# print(a, b, r)
