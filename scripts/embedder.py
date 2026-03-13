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
