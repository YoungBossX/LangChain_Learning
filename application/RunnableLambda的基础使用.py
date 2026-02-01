import os
import dotenv
from pathlib import Path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv(Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

# 创建模型对象，不传model默认用的是 gpt-3.5-turbo
chat_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL_ID")
)

# 输出解析器
str_parser = StrOutputParser()

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，性别{gender}，请帮忙起名字，"
    "并封装为JSON格式返回给我。要求key是name，value就是你起的名字，请严格遵守格式要求。"
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)

chain = first_prompt | chat_model | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt | chat_model | str_parser

for chunk in chain.stream({"lastname": "谢", "gender": "男"}):
    print(chunk, end="", flush=True)