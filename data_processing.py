import camelot

def extract_tables_from_pdf(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='all')
    dataframes = [table.df for table in tables]
    return dataframes
