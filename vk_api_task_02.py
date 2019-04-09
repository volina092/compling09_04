import urllib.request
import json
#тут в range пишем количество сотен постов, которое хотим получить
for i in range(2):
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-33276697&count=100&offset=' + str(100 * i) + '&v=5.92&access_token=805f93966f172b22e92c013e37665e062cb07e325c53b91c74062ef3ab7bd80409ca8bf3460fffa8e90bf') 
    
    response = urllib.request.urlopen(req) 
    result = response.read().decode('utf-8')
    data = json.loads(result) 
    #print(type(data))
    for j in range(100):
        ans = data['response']['items'][j]['text']
        print("//" + str(i * 100 + j + 1)) # номера постов с последнего до первого (нумерация с 1, не с 0)
        print(ans + '\n') # собственно текст поста
#https://oauth.vk.com/blank.html#access_token=805f93966f172b22e92c013e37665e062cb07e325c53b91c74062ef3ab7bd80409ca8bf3460fffa8e90bf&expires_in=86400&user_id=308903303