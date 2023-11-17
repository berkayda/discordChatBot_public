
#  EDIT LINE 9 AND 41 SPECIFICALLY ACCORDING TO DISCORD CHANNEL

import requests
import random
import time

token = 'WRITEYOURS' # Discord token
channel_id = CHANNEL ID 

#instantTime = time.strftime('%H:%M:%S:')

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
    
    r = requests.post(url, data=data, headers=header)
    print(r.status_code)
    
    #print(r.instantTime)

sleep_times = [65, 77, 82, 99, 64, 68, 66, 85, 79, 70, 94, 66, 99, 90, 88, 72, 69]
messages = ['gm', 'gn', 'wagmi', 'come on guys', 'lets do it', 
'lets go', 'how are you?', 'whats going on?', 'keep going', 'greeting to everyone', 
'hello from Turkiye', 'I am so excited', 'The best community', 'It looks great', 'what are you doing?', 
'whats your level?', 'where are you from?', 'It sounds great', 'Where is your favorite city?', 'take care mates', 
'How do you feel?', 'Chat is too fast. I cant read', 'have a nice day', 'Keep going', 'Come on guys', 
'Community is crazy', 'Wen mint?', 'Lets continue', 'huge hype', 'good luck everyone', 
'Lets get WL', 'Are you whitelisted?', 'see you later', 'is everyone ok?', 'is everyone feels good?', 
'whats your favorite color?', 'what would you like to eat?', 'stay safe', 'stay healthy', 'Lets do it mates', 
'we can get WL, come on', 'nfts looks great. Wen mint?', 'Dont give up', 'how is it going?', 'nice project', 
'Are you whitelisted?', 'whats you favorite song ?', 'whats you favorite food?', 'we can do it', 'congrats guys', 
'I will see you later then', 'Thank you so much for helping', 'You should take it', 'What do you do?', 'What do you do for a living?', 
'What are your hobbies?', 'What do you like doing?', 'Sure, it is', 'Of course mate', 'How old are you?', 
'have a good day', 'have a nice day mates', 'are you hungry?', 'what about you?', 'I am fine thx', 
' I am playing video games', 'did you watch lcdp?', 'I dont like vegan foods', 'do you like chips?', 'I want to visit NYC', 
'The idea of the project is amazing', 'project is really good', 'really awesome!', 'what a hype!', 'amazing project I love this']

for i in range(75):
    sendMessage('WRITEYOURS', CHANNELID, random.choice(messages)) 
    sleep_time = random.choice(sleep_times)
    #print("'"+messages+"'" + " sent as message --------    " + str(sleep_time) + " secs slept") 
    time.sleep(sleep_time)
