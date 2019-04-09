import urllib.request
import json
#тут в range пишем количество сотен постов, которое хотим получить


def add_info(text):
    file = open('corpus_sbe.txt', 'a', encoding="utf-8")
    file.write(text)
    file.close()

for i in range(2):
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=-125842747&count=100&offset=' + str(100 * i) + '&v=5.92&access_token=2a095101aed0df2c92439d565d49d15fea3aea0b78fd7dba8767a9c83f15bfa95fce39e5fc59e65303c69') 
    
    response = urllib.request.urlopen(req) 
    result = response.read().decode('utf-8')
    data = json.loads(result) 
    #print(type(data))
    for j in range(100):
        #print(data)
        ans = data['response']['items'][j]['text']
        res = ''
        count = 1
        if ans.count(' ') >= 10: # чтобы добавлять только длинные (только важные :3) посты 
            res += "//" + str(count) + '\n' # номера постов с последнего до первого (нумерация с 1, не с 0)
            res += ans + '\n' # собственно текст поста
            add_info(res)
            count += 1
            print('OK', end=' ')
        print('done')
#https://oauth.vk.com/blank.html#access_token=2a095101aed0df2c92439d565d49d15fea3aea0b78fd7dba8767a9c83f15bfa95fce39e5fc59e65303c69&expires_in=86400&user_id=308903303
