from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

loader = PyPDFLoader(
    file_path=str(Path(__file__).parent / "data" / "pdf1.pdf"),
    mode="page",        # 默认是page模式，每个页面形成一个Document文档对象；single模式，不管有多少页，只返回1个Document对象
    # password="..."
)

i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20, i)