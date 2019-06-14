import redis
import json

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
keys = r.keys()[5]
items = []

for i in r.lrange("ct:items",0,-1):
    value_dict = {}
    i = json.loads(i)
    print(i["summary"])
    # value_dict["title"] = i["title"]
    # value_dict["summary"] = i['summary']
    # value_dict["praise_count"] =i["praise_count"]
    # value_dict["username"] = i["username"]
    # items.append(value_dict)


