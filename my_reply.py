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

def query_reply_data_from_eastmoney(pageindex):
    url = config['reply_url']

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


def pull_reply_data():
    try:
        with open('last_reply_id.txt', 'r') as file:
            latest_record_reply_id = int(file.read().strip())
    except FileNotFoundError:
        latest_record_reply_id = 0
    except ValueError:
        latest_record_reply_id = 0

    new_reply_list = []
    
    # 遍历回帖数据，找出最新的回帖保存到new_reply_list中
    meet_old_record = False
    for pageindex in range(1, 3):
        if meet_old_record:
            break
        else:
            reply_list = query_reply_data_from_eastmoney(pageindex)
            
            for item in reply_list:
                reply_id = item.get('reply_id')
                if reply_id > latest_record_reply_id:
                    new_reply_list.append(item)
                else:
                    meet_old_record = True
                    break

    # 将最新的回帖ID保存到文件中
    if len(new_reply_list) > 0:
        latest_reply_id = new_reply_list[0].get('reply_id')
        with open('last_reply_id.txt', 'w') as file:
            file.write(str(latest_reply_id))
    else:
        print(f"{datetime.datetime.now()} No new reply data found.")
        print("-" * 40)

    send_msg_to_feishu_bot(new_reply_list)


def send_msg_to_feishu_bot(reply_list):
    # 将回帖数据发送给飞书机器人
    for item in reply_list:
        if isinstance(item, dict):
            reply_id = item.get('reply_id')
            reply_user_nickname = item.get('reply_user').get('user_nickname')
            reply_guba = item.get('reply_guba').get('stockbar_name')
            reply_publish_time = item.get('reply_publish_time')
            reply_text = item.get('reply_text')
            reply_picture = item.get('reply_picture')
            source_post_id = item.get('source_post_id')
            source_reply_text = item.get('source_reply_text')
            source_reply_user_nickname = item.get('source_reply_user_nickname')
            source_post_title = item.get('source_post_title')
            source_post_time = item.get('source_post_time')
            source_reply_time = item.get('source_reply_time')
            
            print(f"Reply ID: {reply_id}")
            print(f"Reply Guba: {reply_guba}")
            print(f"Reply Publish Time: {reply_publish_time}")
            print(f"Reply Text: {reply_text}")
            print(f"Reply Picture: {reply_picture}")
            print(f"Source Post ID: {source_post_id}")
            print(f"Source Reply Text: {source_reply_text}")
            print(f"Source Reply User Nickname: {source_reply_user_nickname}")
            print(f"Source Post Title: {source_post_title}")
            print(f"Source Post Time: {source_post_time}")
            print(f"Source Reply Time: {source_reply_time}")

            if source_reply_text != "":
                source_reply_user_text =  f"@{source_reply_user_nickname}: {source_reply_text}"

                if reply_text == "图片评论":
                    reply_user_text = f"@{reply_user_nickname}:{reply_text}:{reply_picture}"
                else:
                    reply_user_text = f"@{reply_user_nickname}:{reply_text}"
            else:
                reply_user_text = f"@{reply_user_nickname}:{reply_text}"
                source_reply_user_text =  ""

            feishu_doc_bot_url = config['feishu_doc_bot_url']
            text = f"{reply_id}#{reply_guba}#{reply_publish_time}#{reply_user_text}#{source_reply_user_text}#{source_post_title}#{source_reply_time}"
            print(f"Post Text: {text}")
            payload = {
                "text": text
            }
            response = requests.post(feishu_doc_bot_url, json=payload, headers=headers)
            if response.status_code != 200:
                print(f"Failed to send message to Feishu Doc bot: {response.status_code}, {response.text}")

            feishu_teamchat_bot_url = config['feishu_teamchat_bot_url']

            noti_text = (f"💥💥💥评论有更新！💥💥💥\n"
                        f"评论ID:{reply_id}\n"
                        f"股吧:{reply_guba}\n"
                        f"发布时间:{reply_publish_time}\n"
                        f"评论内容:{reply_user_text}\n"
                        f"源评论内容: {source_reply_user_text}\n"
                        f"源评论标题:{source_post_title}\n"
                        f"源评论时间:{source_reply_time}\n")
            
            chat_headers = {
                "Content-Type": "application/json"
            }
            data = {
                "msg_type": "text",
                "content": {
                    "text": noti_text
                }
            }
            response = requests.post(feishu_teamchat_bot_url, headers=chat_headers, data=json.dumps(data))

            if response.status_code == 200:
                print("Message sent successfully")
            else:
                print(f"Failed to send message: {response.status_code}, {response.text}")

        else:
            print(f"Unexpected item type: {type(item)}")
        print("-" * 40)
    

if __name__ == "__main__":
    pull_reply_data()