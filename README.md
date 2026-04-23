# RAG-Based Customer Support Assistant

This project implements a Retrieval-Augmented Generation (RAG) based
customer support assistant using LangGraph workflow orchestration and
ChromaDB vector storage.

## Project Objective

The goal of this system is to answer user queries using information
retrieved directly from a PDF knowledge base instead of generating
responses without context like traditional chatbots.

## Features

- PDF document ingestion
- Chunking using RecursiveCharacterTextSplitter
- Embedding generation using sentence-transformers
- Vector storage using ChromaDB
- Similarity-based retrieval
- LangGraph workflow pipeline
- Human-in-the-Loop escalation support

## Technologies Used

- Python
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers

## Project Workflow

User Query → Embedding Conversion → Similarity Search in ChromaDB →
Relevant Chunk Retrieval → Response Generation → HITL Escalation (if required)

## How to Run the Project

Install dependencies:

pip install -r requirements.txt

Run the system:

python main.py

## Author

Simran – GenAI Internship Project
