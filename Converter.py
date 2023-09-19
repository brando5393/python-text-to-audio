import pyttsx3
import PyPDF2

class Converter:

    def __init__(self):
        pass

    def convert_to_audio(self, files):
        """Checks to see if the file(s) specified are in text or PDF format and converts them to an audio file"""
        
        # Initialize the text-to-speech engine
        speaker = pyttsx3.init()
        
        # Iterate through the list of files
        for file in files:
            # Check if the file has a ".txt" or ".pdf" extension
            if file.endswith((".txt", ".pdf")):
                # If it's a text file
                if file.endswith(".txt"):
                    # Read the content of the text file
                    with open(file, "r") as txt_file:
                        text = txt_file.read()
                # If it's a PDF file
                elif file.endswith(".pdf"):
                    # Initialize a PDF reader
                    pdfreader = PyPDF2.PdfFileReader(open(file, 'rb'))
                    text = ""
                    # Extract text from each page in the PDF
                    for page_num in range(pdfreader.numPages):
                        page = pdfreader.getPage(page_num)
                        text += page.extractText()
                
                # Clean the text by removing extra whitespace and line breaks
                clean_text = text.strip().replace('\n', ' ')
                
                # Generate an output filename based on the input filename,
                # replacing the ".txt" or ".pdf" extension with ".mp3"
                output_file = file.replace(".txt", ".mp3").replace(".pdf", ".mp3")
                
                # Save the cleaned text as an audio file in MP3 format
                speaker.save_to_file(clean_text, output_file)
            else:
                # If the file has an unsupported extension, skip it
                pass
