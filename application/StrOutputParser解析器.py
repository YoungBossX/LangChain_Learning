import os
import dotenv
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

dotenv.load_dotenv(Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

# 创建模型对象，不传model默认用的是 gpt-3.5-turbo
chat_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL_ID")
)

parser = StrOutputParser()
prompt = PromptTemplate.from_template(
    "我邻居姓：{lastname}，性别{gender}，请起名，仅告知我名字无需其它内容。"
)

chain = prompt | chat_model | parser | chat_model | parser

res: str = chain.invoke({"lastname": "谢", "gender": "男"})
print(res)
print(type(res))