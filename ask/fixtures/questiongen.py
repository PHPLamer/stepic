import json
import copy
import random


file = open('question.json', 'r')
fileData = json.loads(file.read())
question = fileData[0]
result = []
for i in range(1, 1001):
    tmp = copy.deepcopy(question)
    tmp['fields']['title'] = tmp['fields']['title'] + ' #' + str(i)
    tmp['pk'] = i
    tmp['fields']['rating'] = float(random.randrange(0, 1000))
    result.append(tmp)
open('questions.json', 'w+').write(json.dumps(result))
