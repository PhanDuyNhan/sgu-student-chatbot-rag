import json
import os

def load_chunks():
    """Load chunks from the processed data file."""
    chunks_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'chunks.json')
    
    with open(chunks_path, 'r', encoding='utf-8') as file:
        chunks = json.load(file)
    
    return chunks

def inspect_chunks(chunks):
    """Inspect and display chunk information."""
    # Count total chunks
    total_chunks = len(chunks)
    print(f"Total chunks: {total_chunks}\n")
    
    # Print titles of first 5 chunks
    print("First 5 chunk titles:")
    for i, chunk in enumerate(chunks[:5], 1):
        print(f"{i}. {chunk['title']}")

if __name__ == '__main__':
    chunks = load_chunks()
    inspect_chunks(chunks)
