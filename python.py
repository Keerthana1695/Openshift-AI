from openshift_ai_sdk import OpenShiftAIClient

# Initialize client (replace with your actual API key)
client = OpenShiftAIClient(api_key="sha256~kiAMUFsc1GGx0Qc8IzBLTuDWHEcIGQRbQnlW5JIBVJ0")

# Step 1: Embed KB docs and add to vector DB
doc_embeddings = []
for idx, doc in enumerate(kb_docs):
    embedding = client.embed_text(doc)
    # Upsert into vector DB with id=idx and metadata as doc text
    client.vector_db.upsert(id=str(idx), embedding=embedding, metadata={"text.txt": doc})

# Step 2: User query
query = "How do I reset my password?"

# Step 3: Embed query and retrieve top 2 docs
query_embedding = client.embed_text(query)
retrieved = client.vector_db.search(query_embedding, top_k=2)

# Step 4: Construct prompt with retrieved info
context_texts = "\n".join([item.metadata["text"] for item in retrieved])
prompt = f"Use the information below to answer the question.\n\n{context_texts}\n\nQuestion: {query}\nAnswer:"

# Step 5: Generate answer from LLM
answer = client.llm.generate_text(prompt)

print("Customer Question:", query)
print("AI Answer:", answer)
