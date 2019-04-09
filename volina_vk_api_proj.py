
import urllib.request
import json

TOKEN = '2a095101aed0df2c92439d565d49d15fea3aea0b78fd7dba8767a9c83f15bfa95fce39e5fc59e65303c69'

#тут в range пишем количество сотен постов, которое хотим получить
def add_into_file(file_name, text):
    file = open(file_name, 'a', encoding="utf-8")
    file.write(text)
    file.close()

    #качаем посты (¬Ќ»ћј“≈Ћ№Ќќ следить за OFFSET!!!) 
def get_posts(offset, count):
    global TOKEN
    curr_req = 'https://api.vk.com/method/wall.get?owner_id=-125842747' + '&offset='
    curr_req += offset + '&v=5.92&access_token=' + TOKEN
    
    response = ''
    response = urllib.request.urlopen(curr_req)
    #print(response)
    result = ''
    result = response.read().decode('utf-8')
    print(result)
    final = ''
    final = json.loads(result)
    return final   

'''def post_comments(post_id):
    global TOKEN
    curr_req = 'https://api.vk.com/method/wall.get?owner_id=-125842747' + '&offset='
    curr_req += offset + '&v=5.92&access_token=' + TOKEN
    response = urllib.request.urlopen(curr_req) 
    result = response.read().decode('utf-8')
    print(result)
    return json.loads(result)    
   ''' 
get_posts('0', '1')
#print(get_posts('0', '1')['response'])
'''for i in range(2):
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
        if ans.count(' ') >= 10: # чтобы добавл€ть только длинные (только важные :3) посты 
            res += "//" + str(count) + '\n' # номера постов с последнего до первого (нумераци€ с 1, не с 0)
            res += ans + '\n' # собственно текст поста
            add_info(res)
            count += 1
            print('OK', end=' ')
        print('done')
#https://oauth.vk.com/blank.html#access_token=2a095101aed0df2c92439d565d49d15fea3aea0b78fd7dba8767a9c83f15bfa95fce39e5fc59e65303c69&expires_in=86400&user_id=308903303'''