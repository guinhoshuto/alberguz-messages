import pandas as pd
import json

def str_to_json(str):
    try:
        return json.loads(str)
    except:
        # print(str)
        return ''

messages = pd.read_csv('./output/teste.csv')

cassino = messages[messages['channel'] == '╰─⦁🎰-cassino'] 
mudae = cassino[cassino['author'] == 'Mudae']

fate = mudae[mudae['title'].notnull()]
fate = fate[fate['title'] ]

# object_list = [str_to_json(x.replace("'", "\"").replace("\"s", "s")) for x in fate]
# title_list = [obj for obj in object_list]
# print(json.loads(object_list[0])['description'])
# print(title_list)
print(fate.info())
fate.to_csv('./output/fate.csv')
# print(mudae)