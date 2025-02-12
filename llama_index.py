from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document

# Example function to create the index
def create_llama_index(tables):
    documents = []

    for table in tables:
        table_text = table.to_string()  # Convert table (Pandas DataFrame) to string
        documents.append(Document(text=table_text))  # Wrap table data in Document class

    # Create the index from the documents
    index = VectorStoreIndex.from_documents(documents)
    return index

def query_llama_index(index, query):
    response = index.query(query)
    return response
