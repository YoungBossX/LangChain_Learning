import os
import dotenv
from pathlib import Path
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv(Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

# 创建模型对象，不传model默认用的是 gpt-3.5-turbo
embed_model = OpenAIEmbeddings(
    model=os.getenv("LLM_EMBEDDING_MODEL_ID")
)

print(embed_model.embed_query("我喜欢你"))
print(embed_model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))