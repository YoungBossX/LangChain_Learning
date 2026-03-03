from pathlib import Path

BASE_DIR = Path(__file__).parent

md5_path = str(BASE_DIR / "md5.text")

# Chroma
collection_name = "rag"
persist_directory = str(BASE_DIR / "chroma_db")

# spliter
chunk_size = 300
chunk_overlap = 50
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number = 1000

# 检索返回匹配的文档数量
similarity_threshold = 1

session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }
