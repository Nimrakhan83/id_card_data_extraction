from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import camelot
import pandas as pd
from llama_index import GPTSimpleVectorIndex

app = FastAPI()
index = Index()  # Initialize Llama Index


class Query(BaseModel):
    query: str


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open("temp.pdf", "wb") as temp_file:
        temp_file.write(contents)

    tables = camelot.read_pdf("temp.pdf", pages='all')
    for table in tables:
        # Index the tables' data
        df = table.df
        index.add_documents(df.to_dict(orient='records'))

    return {"message": "File processed and indexed successfully"}


@app.post("/query/")
def query_data(query: Query):
    results = index.query(query.query)
    return {"results": results}
