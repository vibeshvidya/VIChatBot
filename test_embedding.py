from src.helper import download_embeddings

embedding = download_embeddings()

vector = embedding.embed_query("My name is Vibesh")

print(len(vector))
print(vector[:5])