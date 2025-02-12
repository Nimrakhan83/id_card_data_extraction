from llama_index import RAGRetriever, RAGGenerator

retriever = RAGRetriever(index=index)
generator = RAGGenerator()

def perform_query(query):
    docs = retriever.retrieve(query)
    response = generator.generate(query, docs)
    return response
