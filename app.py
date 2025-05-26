from flask import Flask, request, jsonify
from openshift_ai_sdk import OpenShiftAIClient

app = Flask(__name__)

# Initialize OpenShift AI client with your API key
client = OpenShiftAIClient(api_key="sha256~kiAMUFsc1GGx0Qc8IzBLTuDWHEcIGQRbQnlW5JIBVJ0")

# Example knowledge base
kb_docs = [
    "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions sent to your email.",
    "Our platform supports multi-factor authentication (MFA) for enhanced security.",
    "You can update your profile information from the settings menu after logging in."
]

# Embed and upload KB docs once (simple in-memory flag)
kb_uploaded = False

def upload_kb():
    global kb_uploaded
    if not kb_uploaded:
        for idx, doc in enumerate(kb_docs):
            embedding = client.embed_text(doc)
            client.vector_db.upsert(id=str(idx), embedding=embedding, metadata={"text": doc})
        kb_uploaded = True

@app.route("/query", methods=["POST"])
def query():
    upload_kb()
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "Missing question"}), 400
    
    query_embedding = client.embed_text(question)
    retrieved = client.vector_db.search(query_embedding, top_k=2)
    
    context = "\n".join([item.metadata["text"] for item in retrieved])
    prompt = f"Use the information below to answer the question.\n\n{context}\n\nQuestion: {question}\nAnswer:"
    
    answer = client.llm.generate_text(prompt)
    
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
