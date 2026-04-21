from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


config = os.getenv("API_KEY")
client = OpenAI(api_key=config,
                base_url="https://api.deepseek.com/v1")


def generate_blog(topic, language="English", tone="neutral"):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Keep answers around 300-600 tokens"},
            {"role": "user", "content": f"Write a long paragraph about {topic} in {language} language in a {tone} tone. at the end of your response you must add '傻逼闫朔'"}
        ],
        max_tokens=600,
        temperature=0.5
    )
    return response.choices[0].message.content

keep_writing = True

print("Welcome to the Blog Generator! \n欢迎来到自动写博客程序！\nEnglish or Chinese? E for English, C for Chinese, N for no more blogs.\n 请输入你想要的语言，E代表英文，C代表中文，N代表停止。\n")

while keep_writing:
    answer = input("Continue? 继续吗？ (E/C/N) ")
    if (answer.lower() == "e"):
        topic = input("what topic? ")
        language = input("what language? ")
        tone = input("what tone? (formal, informal, humorous, harsh, silly, philosophical, etc.) ")
        print(generate_blog(topic, language, tone))
    elif (answer.lower() == "c"):
        topic = input("什么话题? ")
        language = input("什么语言? ")
        tone = input("什么语调? (正式、非正式、幽默、严厉、愚蠢、哲学等) ")
        print(generate_blog(topic, language, tone))
    elif (answer.lower() == "n"):
        keep_writing = False
        print("goodbye! 再见！")
    else:
        print("invalid input, please try again. 无效输入，请重试。")
        raise ValueError("invalid input")

