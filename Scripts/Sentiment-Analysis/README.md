# Gemini Sentiment Analysis Script

This script uses Google's Gemini AI to analyze the sentiment of text data in a CSV file. It adds a new column to your CSV with a sentiment score for each row.

## What it does

The script reads a CSV file, extracts text from a specified column, sends it to the Gemini AI for analysis, and then writes the results (including the original data and the sentiment scores) into a new CSV file named `output.csv`.

## Prerequisites

Before you can use this script, make sure you have the following:

1. **Python 3.9 or higher:** You need Python installed on your computer. If you don't have it, download and install it from [python.org](https://www.python.org/).
2. **`google-generativeai` library:** This Python library allows you to interact with the Gemini API. Install it using pip:

    ```bash
    pip install google-generativeai
    ```
3. **Gemini API Key:** You'll need an API key to use the Gemini AI. Get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).
4. **CSV Data File:**  A CSV (Comma Separated Values) file containing the text you want to analyze. Make sure the file is accessible to the script.

## How to Use

1. **Place the Script:** Put the Python script (`GeminiSentimentAnalysis.py`) in a folder where you can easily access it.
2. **Prepare Your Data:** Ensure your CSV file is in the same folder as the script or in a location you can easily specify.
3. **Configure the Script:**
    *   **API Key:** Open the `GeminiSentimentAnalysis.py` file in a text editor. Replace `"Insert-API-Key"` on line 21 with your actual Gemini API key. Keep the quotation marks.
    *   **Sentiment Column:** Find the line `sentimentColumn = 0` (around line 10). Change `0` to the index of the column in your CSV that contains the text you want analyzed. Remember that the first column is index 0, the second is 1, and so on.
4. **Run the Script:**
    *   Open your terminal or command prompt.
    *   Navigate to the folder where you placed the script using the `cd` command. For example:

        ```bash
        cd path/to/your/script/folder
        ```
    *   Run the script using the following command, replacing `your_data.csv` with the actual name of your CSV file:

        ```bash
        python GeminiSentimentAnalysis.py your_data.csv
        ```
5. **Get the Results:** Once the script finishes (it may take some time depending on the size of your data), you'll find a new file named `output.csv` in the same folder. This file will contain your original data plus a new column called "AI-Sentiment" with the sentiment scores.

## Understanding the Sentiment Scores

The script will add a new column named "AI-Sentiment" to your CSV. The values in this column are:

*   **Numbers from 0 to 10:** These represent the sentiment score, where 0 is the most negative sentiment and 10 is the most positive sentiment.
*   **"N/A":** This means the script couldn't get a sentiment score for that row. This might happen if there's an issue with the API or if the text in that row was problematic.

## Important Notes

*   **Rate Limits:** If you're using the free Gemini API plan, there might be limits on how many requests you can make in a certain time. The script includes a 1-second pause between each request to help avoid hitting these limits, but for very large datasets, you might need to use a paid plan or modify the script to handle rate limiting in a more sophisticated manner.
*   **Error Handling:** The script has basic error handling. If there's a problem with the API or the data, it will try to print an error message and continue. It will also mark the row with "N/A" in the output file.
*   **Model:** The model used in this script is `gemini-1.5-flash-8b`. It's possible that in the future, this model may be deprecated. If that happens, you'll need to update the `model_name` variable in the script to a different Gemini model.

## Troubleshooting

*   **`ModuleNotFoundError: No module named 'google.generativeai'`:**  Make sure you installed the `google-generativeai` library correctly using `pip install google-generativeai`.
*   **`FileNotFoundError`:** Check if your CSV file is in the correct location and if you're using the correct file name in the command.
*   **API Key Errors:** Double-check that you've correctly pasted your API key into the script and that the key is valid.

If you encounter other issues, carefully read the error messages in the terminal. They might provide clues about what went wrong.