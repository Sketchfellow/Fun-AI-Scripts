import os
import sys
import google.generativeai as genai

# Usage: Upload audio file to Gemini, get a transcript of the audio, have Gemini translate the transcript

# Check if the file path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python GeminiAudioTranslation.py <audio.file>")
    sys.exit(1)

input_file_path = sys.argv[1]
audioType = input_file_path.split(".")
audioType = "audio/" + audioType[-1]
# should look like audio/flac or audio/mp3
print(audioType)
"""
Gemini supports the followiung audio formats:
- audio/wav
- audio/mp3
- audio/aiff
- audio/aac
- audio/ogg
- audio/flac
"""

# Start Gemini
genai.configure(api_key = "Insert-API-Key-Here")

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

audio = upload_to_gemini(input_file_path, mime_type = audioType) 

# It is recommended to edit the following prompt to better fit your use-case with additional context of the audio. 
prompt = "Give an accurate transcript of the following audio."
print("Getting transcript...")
# get transcript:
transcript = model.generate_content([audio, prompt])
transcript = transcript.text
print("Transcript done.\n")
print(transcript)
print("\nWriting transcript to file...")

# write transcript to file
# Create the output directory if it doesn't exist
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Create the directory

file = open(os.path.join(output_dir, "transcript.txt"), "w")  # Use os.path.join for safer path construction
file.write(transcript)
file.close()
print("Transcript saved to output/transcript.txt\n")
print("Getting translation...")

prompt = "Give an accurate translation of the following audio transcript: " + transcript
translation = model.generate_content(prompt)
translation = translation.text
print("Translation done.\n")
print(translation)
print("\nWriting translation to file....")
# write translation to file

file = open(os.path.join(output_dir, "translation.txt"), "w")  # Use os.path.join for safer path construction
file.write(translation)
file.close()
print("Translation saved to output/translation.txt\n")

# Delete file. Files are also automatically deleted after 48 hrs
audio.delete()
print("Done.")