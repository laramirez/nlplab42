from embeddings import EmbeddingsDictionary

emb = EmbeddingsDictionary(250000)

print emb.w2neighbors("geek", 10)

query_embedding = emb.embed("Facebook") + emb.embed("Google")

emb.analogy('fifty-five', 'five', 'twenty')