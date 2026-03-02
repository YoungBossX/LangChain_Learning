import os
import dotenv
from pathlib import Path
from langchain_chroma import Chroma
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader

dotenv.load_dotenv(Path(__file__).parent / ".env")

os.environ["OPENAI_API_KEY"] = os.getenv("LLM_API_KEY")
os.environ["OPENAI_API_BASE"] = os.getenv("LLM_BASE_URL")

vector_store = InMemoryVectorStore(
    embedding=OpenAIEmbeddings(model=os.getenv("LLM_EMBEDDING_MODEL_ID"))
)

vector_store = Chroma(
    collection_name="test",
    embedding_function=OpenAIEmbeddings(model=os.getenv("LLM_EMBEDDING_MODEL_ID")),
    persist_directory=str(Path(__file__).parent / "chroma_db")
)

# loader = CSVLoader(
#     file_path=str(Path(__file__).parent / "data" / "info.csv"),
#     encoding="utf-8",
#     source_column="source",
# )

# documents = loader.load()

# id1 id2 id3 id4 ...
# 向量存储的 新增、删除、检索
# vector_store.add_documents(
#     documents=documents,        # 被添加的文档，类型：list[Document]
#     ids=["id"+str(i) for i in range(1, len(documents)+1)] # 给添加的文档提供id（字符串）  list[str]
# )

# 删除  传入[id, id...]
# vector_store.delete(["id1", "id2"])

# 检索 返回类型list[Document]
result = vector_store.similarity_search(
    "大模型开发",
    3,
    filter={"source": "黑马程序员"}
)

print(result)