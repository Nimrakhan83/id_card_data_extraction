import camelot
import pdfplumber

def extract_tables_from_pdf(file_path):
    # Use pdfplumber to read the entire PDF
    with pdfplumber.open(file_path) as pdf:
        tables = []
        for page in pdf.pages:
            # Extract table data from each page using Camelot
            page_tables = camelot.read_pdf(file_path, pages=str(page.page_number))
            if page_tables:
                for table in page_tables:
                    tables.append(table.df)  # Append the dataframe of the table
    return tables
