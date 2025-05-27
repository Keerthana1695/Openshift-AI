from fastapi import FastAPI, Request
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

app = FastAPI()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
engine = create_engine("postgresql+psycopg2://rag_user:rag_pass@vector-db:5432/rag_db")
db = PGVector.from_documents(
    documents=docs,
    embedding=embedding,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
    pre_delete_collection=True # This deletes existing collection and its data, use carefully!
)

@app.route("/query", methods=["POST"])
def query():
    query_text = request.json.get("query")
    docs = db.similarity_search(query_text, k=3)
    return jsonify({"results": [doc.page_content for doc in docs]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
