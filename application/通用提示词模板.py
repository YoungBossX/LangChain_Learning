import os
import dotenv
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv(Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

# 创建模型对象，不传model默认用的是 gpt-3.5-turbo
chant_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL_ID")
)

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 性别{gender}, 他喜欢什么？简单回答。"
)

chain = prompt_template | chant_model

response = chain.invoke(input={"lastname": "谢", "gender": "男"})

print(response.content)