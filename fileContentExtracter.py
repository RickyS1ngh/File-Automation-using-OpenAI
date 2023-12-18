from PyPDF2 import PdfReader
import docx


def contentExtracter(file, extension):
    if extension in ("py", "c", "cpp", "java", "html", "txt"):
        with open(file) as file:
            fileContents = file.read()
        return fileContents

    elif extension == "pdf":
        with open(file, "rb") as file:
            reader = PdfReader(file)
            page = reader.pages[0]
            fileContents = page.extract_text()
        return fileContents
    else:
        with open(file, "rb") as file:
            doc = docx.Document(file)
            fileContents = doc.paragraphs[0]
        return fileContents
