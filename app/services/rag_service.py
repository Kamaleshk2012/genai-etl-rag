from app.db.embedding import embed_text
from app.db.faiss_store import FaissStore

store = FaissStore()

def index_rows(rows):
    texts = [str(row) for row in rows]
    vectors = embed_text(texts)
    store.add(vectors, texts)

def retrieve_rows(query, k=5):
    query_vec = embed_text([query])
    return store.search(query_vec, k)
