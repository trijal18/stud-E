# from pypdf import PdfReader

# # creating a pdf reader object
# reader = PdfReader()

# # printing number of pages in pdf file
# print(len(reader.pages))

# # getting a specific page from the pdf file
# page = reader.pages[0]

# # extracting text from page
# text = page.extract_text()
# print(text)

from pypdf import PdfReader

reader = PdfReader(r"D:\study\4th sem\dcn\Unit-1-NS.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print((text))