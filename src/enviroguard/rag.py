# src/enviroguard/rag.py
import os
try:
    from sentence_transformers import SentenceTransformer
    import faiss
except Exception:
    SentenceTransformer = None
    faiss = None

class LocalRAG:
    def __init__(self, index_path='data/env_docs'):
        self.docs = []
        self.index = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2') if SentenceTransformer else None
        self._ensure_docs()

    def _ensure_docs(self):
        docs_dir = 'data/env_docs'
        if not os.path.exists(docs_dir):
            os.makedirs(docs_dir, exist_ok=True)
            sample = [
                'Deforestation was observed along river corridor in 2019 due to logging.',
                'Flooding in area X caused road closures and infrastructure damage.',
                'Water quality monitoring detected elevated pollutants upstream.'
            ]
            for i,d in enumerate(sample):
                with open(os.path.join(docs_dir, f'doc_{i}.txt'), 'w', encoding='utf-8') as f:
                    f.write(d)
        for fname in os.listdir('data/env_docs'):
            with open(os.path.join('data/env_docs', fname), 'r', encoding='utf-8') as f:
                self.docs.append(f.read())
        if self.model and faiss:
            embs = self.model.encode(self.docs, convert_to_numpy=True)
            dim = embs.shape[1]
            self.index = faiss.IndexFlatL2(dim)
            self.index.add(embs)

    def search(self, query, top_k=3):
        if self.index is None or self.model is None:
            return self.docs[:top_k]
        q_emb = self.model.encode([query], convert_to_numpy=True)
        D,I = self.index.search(q_emb, top_k)
        return [self.docs[i] for i in I[0] if i < len(self.docs)]
