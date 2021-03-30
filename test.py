from QuoteEngine import *

csvpath = "_data/DogQuotes/DogQuotesCSV.csv"
docxpath = "_data/DogQuotes/DogQuotesDOCX.docx"
txtpath = "_data/DogQuotes/DogQuotesTXT.txt"
pdfpath = "_data/DogQuotes/DogQuotesPDF.pdf"
#print(DocxIngestor.parse(docxpath))
#print(CsvIngestor.parse(csvpath))
#print(TxtIngestor.parse(txtpath))
print(PdfIngestor.parse(pdfpath))
# ALL WORKING NICe