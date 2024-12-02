import requests
from bs4 import BeautifulSoup
import re

def fetch_article_text(url):
    # 发送 GET 请求获取页面内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析页面内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 使用正则表达式查找包含 articleTxt 变量的 <script> 标签
        script_tag = soup.find('script', string=re.compile(r'var articleTxt ='))

        if script_tag:
            # 提取 script 标签的内容
            script_content = script_tag.string
            
            # 使用正则表达式提取 articleTxt 变量的内容
            article_txt_match = re.search(r'var articleTxt = "(.*?)</div>"', script_content, re.DOTALL)
            
            if article_txt_match:
                article_txt = article_txt_match.group(1)
                
                # 去除 <span> 和 </span> 标签
                article_txt = re.sub(r'</?span.*?>', '', article_txt)

                # 去除 <div> 和 </div> 标签
                article_txt = re.sub(r'</?div.*?>', '', article_txt)
                
                # 将 <p> 和 </p> 标签替换为换行符
                article_txt = re.sub(r'</?p.*?>', '\n', article_txt)
                
                # 移除 &nbsp;
                article_txt = article_txt.replace('&nbsp;', '')
                
                return article_txt
            else:
                print("articleTxt 变量未找到")
        else:
            print("包含 articleTxt 变量的 <script> 标签未找到")
    else:
        print(f"请求失败，状态码: {response.status_code}")

    return None

# 示例调用
if __name__ == "__main__":
    url = "https://caifuhao.eastmoney.com/news/20241129165900633511510"
    article_text = fetch_article_text(url)
    if article_text:
        print(article_text)