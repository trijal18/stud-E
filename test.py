import os
import google.generativeai as genai
import json
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=key)

reader = PdfReader(r"D:\study\4th sem\mc iot\Unit_3_Introduction_to_IoT.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print((text))

#genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="""
        **Prompt:**  
        "Generate multiple-choice questions based on the given text. Provide the question, a list of plausible answer options, and indicate the correct answer. Format the response as a JSON object. Ensure the question and options are clear and directly related to the content of the text.  

        **Example Output:**
        {
        "question": "What is VNC used for in the context of a Raspberry Pi?",
        "options": [
            "To access the Raspberry Pi's graphical interface remotely",
            "To control the Raspberry Pi's camera",
            "To update the Raspberry Pi's operating system",
            "To connect the Raspberry Pi to a network"
        ],
        "answer": "To access the Raspberry Pi's graphical interface remotely"
        }
        """,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(text)

print(response.text)
summary=chat_session.send_message("Give summary of given text")
print(type(summary.text))
def genrate_summary(file_path):
    summary=""
    return summary