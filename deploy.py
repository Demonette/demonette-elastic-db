from elasticsearch import Elasticsearch
es = Elasticsearch()

es.indices.delete(index='demonette', ignore=[400, 404])
es.indices.create(index='demonette')
header = open('header.csv', 'r').readlines()[0].split('\t')
db_csv = open('demonette-1.2.csv', 'r', encoding='ISO-8859-3').readlines()
cpt = 0
for l in db_csv:
    if l:
        d_dict = {}
        l_l = l.split(',')
        for idx, el in enumerate(header):
            d_dict[el] = l_l[idx].replace('\"', '').replace('\n', '')

        es.create(index='demonette', doc_type='relation', id=cpt, body=d_dict)
        cpt += 1
        print('write :' + str(d_dict))
