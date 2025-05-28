# RAG-based Knowledge Assistant on Red Hat OpenShift AI

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline for querying internal documents using OpenShift AI, PostgreSQL+pgvector, and OpenAI.

## Components

- **Jupyter Notebook** for document ingestion and embedding
- **PostgreSQL+pgvector Vector Store** for similarity search
- **FastAPI Backend** to serve QA endpoint
- **React Frontend** as a chatbot interface
- **Deployed on OpenShift** using containerized microservices

## Setup Steps

1. Upload PDFs to `data/` and run the notebook
2. Deploy backend and frontend using provided YAMLs
3. Access the app via OpenShift Route
