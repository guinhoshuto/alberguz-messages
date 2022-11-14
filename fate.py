import pandas as pd

messages = pd.read_csv('./output/messages.csv')

cassino = messages[messages['channel'] == '╰─⦁🎰-cassino'] 
mudae = cassino[cassino['author'] == 'Mudae']


# print(mudae)
