# Gemini Audio Transcription and Translation Script

This script utilizes Google Gemini's multimodal capabilities to transcribe audio from a file and then translate the resulting transcript into another language.

## What it does

The script takes an audio file as input, uploads it to Gemini for transcription, saves the transcript to a file named `transcript.txt`, translates the transcript, and saves the translation to a file named `translation.txt`. Both output files are stored in an `output` directory.

## Prerequisites

Before running this script, ensure you have the following:

1. **Python 3.9 or higher:** Install Python from [python.org](https://www.python.org/) if you don't have it already.
2. **`google-generativeai` library:** This library enables interaction with the Gemini API. Install it via pip:

    ```bash
    pip install google-generativeai
    ```
3. **Gemini API Key:** Obtain a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
4. **Audio File:** The audio file you wish to transcribe and translate. Supported formats include:
    *   audio/wav
    *   audio/mp3
    *   audio/aiff
    *   audio/aac
    *   audio/ogg
    *   audio/flac

## How to Use

1. **Place the Script:** Save the Python script (`GeminiAudioTranslation.py`) in an accessible directory.
2. **Prepare Your Audio:** Make sure your audio file is in the same directory as the script or in a location you can easily specify.
3. **Configure the Script:**
    *   **API Key:** Open `GeminiAudioTranslation.py` in a text editor. Replace `"Insert-API-Key-Here"` on line 28 with your actual Gemini API key, keeping the quotation marks.
4. **Run the Script:**
    *   Open your terminal or command prompt.
    *   Navigate to the script's directory using the `cd` command. Example:

        ```bash
        cd path/to/your/script/folder
        ```
    *   Execute the script with the following command, replacing `<audio.file>` with the name and extension of your audio file:

        ```bash
        python GeminiAudioTranslation.py <audio.file>
        ```

        For example:

        ```bash
        python GeminiAudioTranslation.py my_audio.mp3
        ```
5. **Get the Results:** After the script completes, you'll find two new files in an `output` directory within the script's directory:
    *   `transcript.txt`: Contains the transcribed text from your audio.
    *   `translation.txt`: Contains the translated transcript.

## Important Notes

*   **Rate Limits:** The free Gemini API plan may have rate limits. If you're processing many audio files, consider handling rate limiting in your workflow or upgrading to a paid plan.
*   **Error Handling:** The script includes basic error handling. If issues arise with the API or data, error messages will be printed to the console.
*   **Model:** The script uses the `gemini-2.0-flash-exp` model on line 47. Future model deprecation might necessitate updating the `model_name` variable in the script to a different Gemini model.
*   **Prompt Customization:** The prompt used for transcription is "Give an accurate transcript of the following audio." For optimal results, consider modifying this prompt (line 54 in the script) to provide more context about your audio. This also applies to the translation prompt on line 75.
*   **Audio Length:** The maximum supported length of audio data for Gemini in a single prompt is 9.5 hours. 
*   **File Size:** The maximum audio upload to Gemini is 2 GB.
## Troubleshooting

*   **`ModuleNotFoundError: No module named 'google.generativeai'`:** Ensure the `google-generativeai` library is correctly installed via `pip install google-generativeai`.
*   **`FileNotFoundError`:** Verify your audio file's location and the file name used in the command.
*   **API Key Errors:** Double-check that your API key is correctly pasted into the script and that it's valid.

For other issues, carefully examine the error messages displayed in the terminal, as they often provide clues about the problem.
