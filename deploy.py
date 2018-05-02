from elasticsearch import Elasticsearch
import re
es = Elasticsearch()

es.indices.delete(index='demonette', ignore=[400, 404])
es.indices.create(index='demonette')
header = open('header.csv', 'r').readlines()[0].split('\t')
map = open('fields-to-mapped.txt', 'r').readlines()
db_csv = open('demonette-1.2.csv', 'r', encoding='ISO-8859-3').readlines()

analyzer = {
    "analysis": {
      "analyzer": {
        "custom_analyzer": {
          "type": "custom",
          "tokenizer": "whitespace",
          "filter": [
            "lowercase",
          ]
        }
      }
    }
}
es.indices.close(index='demonette')
es.indices.put_settings(index='demonette', body=analyzer)
es.indices.open(index='demonette')

cpt = 0

for m in map:
    if re.match('type_[0-9]', m):
        d_map = {
            "properties": {
                m.replace('\n', ''): {
                    "type": "text",
                    "fielddata": "true",
                    "analyzer": "custom_analyzer"
                }
            }
        }
    else:
        d_map = {
                "properties": {
                    m.replace('\n', ''): {
                        "type": "text",
                        "fielddata": "true",
                        "analyzer": "custom_analyzer"
                }
            }
        }
    es.indices.put_mapping(index='demonette', doc_type='relation', body=d_map)

for l in db_csv:
    if l:
        d_dict = {}
        l_l = l.split(',')
        for idx, el in enumerate(header):
            d_dict[el] = l_l[idx].replace('\"', '').replace('\n', '')
        es.create(index='demonette', doc_type='relation', id=cpt, body=d_dict)
        cpt += 1
