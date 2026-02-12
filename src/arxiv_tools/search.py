'''
Candy

Desarrollar una función con la cual podamos correr un vector_database y crear una función que dado
un documento lo guarde en el vector_database. Importante utilizar Chunking (Fragmentación) para asi
guardar el documento en trozos.

Librería recomendada: langchain-text-splitters y para la VDB algo ligero como ChromaDB o FAISS

def save_to_vdb(full_text, metadata):
    # 1. Fragmentar el texto
    # 2. Convertir fragmentos a vectores (Embeddings)
    # 3. Guardar en VDB
'''