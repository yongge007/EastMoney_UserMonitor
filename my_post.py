import requests
import datetime
import os
import json
import time


# 改变工作目录到脚本所在的目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取配置文件
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# 定义浏览器的 User-Agent 头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/json"
}

def query_post_data_from_eastmoney(pageindex):
    url = config['art_url']

    # 获取当前时间的时间戳（秒）
    current_timestamp = time.time()
    # 将时间戳转换为毫秒
    current_timestamp_ms = int(current_timestamp * 1000)

    params = {
        "pageindex": pageindex,
        "uid": config['uid'],
        "_": current_timestamp_ms
    }
    
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reply_list = data.get('result').get('list')
    else:
        response.raise_for_status()

    return reply_list

def pull_post_data():
    try:
        with open('last_post_id.txt', 'r') as file:
            latest_record_post_id = int(file.read().strip())
    except FileNotFoundError:
        latest_record_post_id = 0
    except ValueError:
        latest_record_post_id = 0

    new_post_list = []
    
    # 遍历回帖数据，找出最新的回帖保存到new_reply_list中
    meet_old_record = False
    for pageindex in range(1, 3):
        if meet_old_record:
            break
        else:
            reply_list = query_post_data_from_eastmoney(pageindex)
            
            for item in reply_list:
                post_id = item.get('post_id')
                if post_id > latest_record_post_id:
                    new_post_list.append(item)
                else:
                    meet_old_record = True
                    break

    # 将最新的回帖ID保存到文件中
    if len(new_post_list) > 0:
        latest_post_id = new_post_list[0].get('post_id')
        with open('last_post_id.txt', 'w') as file:
            file.write(str(latest_post_id))
    else:
        print(f"{datetime.datetime.now()} No new reply data found.")
        print("-" * 40)

    send_msg_to_feishu_bot(new_post_list)

def send_msg_to_feishu_bot(new_post_list):
    # post_id post_title post_content post_pic_url[] post_publish_time post_user->user_nickname post_guba->stockbar_name stockbar_code
    for post in new_post_list:
        post_id = post.get('post_id')
        post_title = post.get('post_title')
        post_content = post.get('post_content')
        post_pic_url = post.get('post_pic_url')
        post_publish_time = post.get('post_publish_time')
        post_user_nickname = post.get('post_user').get('user_nickname')
        post_guba_name = post.get('post_guba').get('stockbar_name')
        post_guba_stockbar_code = post.get('post_guba').get('stockbar_code')

        msg = f"⭐️⭐️⭐️主帖更新：{post_id}\n帖子标题：{post_title}\n帖子内容：{post_content}\n帖子图片：{post_pic_url}\n发布时间：{post_publish_time}\n发布用户：{post_user_nickname}\n股吧：{post_guba_name}({post_guba_stockbar_code})\n"

        url = config['feishu_teamchat_bot_url']
        data = {
            "msg_type": "text",
            "content": {
                "text": msg
            }
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print(f"{datetime.datetime.now()} {msg}")
            print("-" * 40)
        else:
            response.raise_for_status()

        feishu_post_bot_url = config['feishu_post_bot_url']
        post_text = f"{post_id}#{post_title}#{post_content}#{post_pic_url}#{post_publish_time}#{post_user_nickname}#{post_guba_name}({post_guba_stockbar_code})"

        payload = {
            "text": post_text
        }
        response = requests.post(feishu_post_bot_url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send message to Feishu Doc bot: {response.status_code}, {response.text}")

if __name__ == "__main__":
    pull_post_data()