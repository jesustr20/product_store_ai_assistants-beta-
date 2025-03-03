import chromadb

chroma_client = chromadb.PersistentClient(path="./chromadb_data")

faq_collection = chroma_client.get_or_create_collection(name="faq")

def add_faq(question, answer):
    """Agrega una pregunta frecuente a la base de datos vectorial"""
    if isinstance(answer, list):
        answer_value = " || ".join(answer)
    else:
        answer_value = answer

    faq_collection.add(
        ids=[question], 
        metadatas=[{"answer": answer_value}], 
        documents=[question]
    )

def search_faq(query):
    """Busca la pregunta más similar en la base de datos y devuelve su respuesta"""
    results = faq_collection.query(query_texts=[query], n_results=1)
    if results["ids"] and len(results["metadatas"]) > 0 and len(results["metadatas"][0]) > 0:
        return results["metadatas"][0][0]["answer"]
    return "Lo siento, no encontré una respuesta."