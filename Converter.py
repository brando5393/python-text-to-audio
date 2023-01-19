# import pyttsx3,PyPDF2

# #insert name of your pdf
# pdfreader = PyPDF2.PdfFileReader(open('book.pdf', 'rb'))
# speaker = pyttsx3.init()

# for page_num in range(pdfreader.numPages):
#     text = pdfreader.getPage(page_num).extractText()
#     clean_text = text.strip().replace('\n', ' ')
#     print(clean_text)
# #name mp3 file whatever you would like
# speaker.save_to_file(clean_text, 'story.mp3')
# speaker.runAndWait()

# speaker.stop()


class Converter:

  def __init__(self):
    pass

  def convert_to_audio(self, files):
    """Checks to see if the file(s) specified are in text or PDF format and converts them to an audio file"""
    for file in files:
      if file.endswith((".txt", ".pdf")):
        pass
      else:
        pass
