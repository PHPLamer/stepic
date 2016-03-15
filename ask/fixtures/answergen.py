import json
import copy
import random


file = open('answer.json', 'r')
fileData = json.loads(file.read())
data = fileData[0]
result = []
for i in range(1, 1001):
    for j in range(1, 11):
        tmp = copy.deepcopy(data)
        tmp['fields']['question'] = i
        tmp['pk'] = (i * 10) + j
        result.append(tmp)
open('answers.json', 'w+').write(json.dumps(result))
