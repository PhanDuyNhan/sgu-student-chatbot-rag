import logging
from sentence_transformers import SentenceTransformer
from typing import List

logger = logging.getLogger(__name__)

class TextEmbedder:
    
    def __init__(self, model_name: str):
        logger.info(f"Đang tải mô hình embedding: {model_name}...")
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Nhận vào danh sách văn bản, trả về danh sách các vector."""
        logger.info(f"Đang tạo embedding cho {len(texts)} văn bản...")
        return self.model.encode(texts).tolist()

import logging
import chromadb
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class ChromaDBManager:
    """Class chuyên xử lý các thao tác với Vector Database."""
    
    def __init__(self, db_path: str, collection_name: str):
        logger.info(f"Khởi tạo ChromaDB tại: {db_path}")
        self.client = chromadb.PersistentClient(path=str(db_path))
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def insert_data(self, ids: List[str], texts: List[str], embeddings: List[List[float]], metadatas: List[Dict[str, Any]]):
        """Lưu dữ liệu vào Database."""
        logger.info("Đang ghi dữ liệu vào Vector Database...")
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )
        logger.info(f"Đã lưu thành công {len(ids)} vectors!")

    def query(self, query_text: str, n_results: int = 1):
        """Truy vấn văn bản liên quan."""
        return self.collection.query(query_texts=[query_text], n_results=n_results)
