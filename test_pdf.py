from PyPDF2 import PdfReader


def test_read_pdf():
    reader = PdfReader('unpacked/dummy.pdf')
    page = reader.pages[0]
    text = page.extract_text()
    assert 'Dumm y PDF  file' in text