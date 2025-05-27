from fastapi import FastAPI, Request
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

app = FastAPI()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("faiss_index", embedding)
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=db.as_retriever())

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data["question"]
    answer = qa_chain.run(question)
    return {"answer": answer}
