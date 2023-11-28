import pyttsx3, PyPDF2
import sys

if (len(sys.argv) == 1):
    RuntimeError("Specify the file to read")

pdfreader = PyPDF2.PdfReader(open(sys.argv[1], 'rb'))
speaker = pyttsx3.init()

clean_text = ''

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text += text.strip().replace('\n', ' ')


speaker.save_to_file(clean_text, f'{sys.argv[1]}.mp3')
# runAndWait works in strange way, line below is necessary for saving file to the disk
speaker.say(clean_text)

speaker.runAndWait()
speaker.stop()
