from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from hitl import check_confidence, escalate_to_human


# STEP 1: Load PDF
loader = PyPDFLoader("knowledge.pdf")
documents = loader.load()

print("\nPDF loaded successfully")


# STEP 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Chunking completed")


# STEP 3: Generate embeddings
embedding_model = HuggingFaceEmbeddings()

print("Embeddings created")


# STEP 4: Store inside ChromaDB
vector_db = Chroma.from_documents(chunks, embedding_model)

print("Stored in ChromaDB")


# STEP 5: Ask user query
query = input("\nAsk your question: ")


# STEP 6: Retrieve results
results = vector_db.similarity_search(query, k=3)


# Simulated similarity score
similarity_score = 0.4

# STEP 7: Check escalation condition
if check_confidence(similarity_score):

    final_answer = escalate_to_human()

else:

    final_answer = results[0].page_content


# STEP 8: Print final response
print("\nFinal Response:\n")

print(final_answer)