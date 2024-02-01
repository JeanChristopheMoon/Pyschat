import transformers
import docx
from docx import Document
from docx.shared import Inches

doc_path = "x"
doc = Document(doc_path)
text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

# print(text)



tokenizer = transformers.AutoTokenizer.from_pretrained('bert-base-uncased')
with open(text, "r") as f:
    text = f.read()


