import pyttsx3
import PyPDF2
import os
import LogManager as logger

class Converter:
    def __init__(self):
        pass

    def convert_to_audio(self, files):
        """Checks if the specified file(s) are in text or PDF format and converts them to an audio file"""

        # Initialize the text-to-speech engine
        speaker = pyttsx3.init()

        # Iterate through the list of files
        for file in files:
            try:
                # Check if the file has a ".txt" or ".pdf" extension
                if file.endswith((".txt", ".pdf")):
                    # If it's a text file
                    if file.endswith(".txt"):
                        # Read the content of the text file with specified encoding
                        with open(file, "r", encoding="utf-8") as txt_file:
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

                    # Log successful conversion using self.logger
                    self.logger.add_event("info", "File converted successfully", f"Output file: {output_file}")
                else:
                    # Log unsupported file type
                    self.logger.add_event("alert", "The specified file is not supported and could not be converted.", f"{file}")
            except Exception as e:
                # Log the error and continue with the next file
                error_message = f"Failed to convert file '{file}' to audio: {str(e)}"
                self.logger.add_event("error", error_message)
