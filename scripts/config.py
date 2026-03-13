import os
from pathlib import Path

# Xác định thư mục gốc của toàn bộ dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Đường dẫn file dữ liệu (chunks.json)
DATA_PATH = BASE_DIR / "data" / "processed" / "chunks.json"

# Cấu hình Vector Database
CHROMA_DB_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "my_knowledge_base"

# Cấu hình Model Embedding
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
