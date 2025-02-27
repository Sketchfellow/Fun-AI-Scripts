import google.generativeai as genai
from google.api_core import retry # incase there is transient errors when generating response
import csv
import sys
import time # for rate limit handling

sentimentColumn = 0 # Change this to the actual analysis column.

# Check if the file path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python GeminiSentimentAnalysis.py <data.csv>")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = 'output.csv'  

# Start Gemini
genai.configure(api_key= "Insert-API-Key") # I know this is bad practice. CS people may strike me down and burn me at the stake. 

systemPrompt = "You are an AI that classifies numerical sentiment scores from a given text for a dataset. DO NOT provide any commentary. Only output a single number from 0 - 10 with 0 being the most negative and 10 being the most positive."

def analyze(prompt):
    """Analyzes the sentiment of a given text using the Gemini API.
    Args:
        prompt: The text to analyze.

    Returns:
        The sentiment score as a string, or "N/A" if an error occurred.
    """
    # flash-lite is fast, has higher rate limits, and is smart enough. Model may be deprecated in the future.
    model = genai.GenerativeModel(
        model_name = 'gemini-2.0-flash-lite',
        system_instruction = systemPrompt) 

    try:
        response = model.generate_content(
            prompt,
            request_options={"retry": retry.Retry(predicate=retry.if_transient_error)})
        return response.text
    
    except Exception as e:
        print(f"An API error occurred: {e}")
        return "N/A"    

# Initialize a list to store the rows
data = []

# Open and read the CSV file
with open(input_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    
    # Iterate over each row and append it to the list
    for i, row in enumerate(csv_reader):
        if i == 0:
            header = row + ["AI-Sentiment"]
            data.append(header)  
        else:
            sentimentText = row[sentimentColumn]
            response = analyze(sentimentText)
            time.sleep(2) # Sleep for x seconds. Used for potential rate limits if you're a free user
            # check documentation for rate limits. 2.0 flash-lite has 30 requests per minute and 1500 requests per day for free plan.
            # for large datasets you should use a paid plan. 

            try:
                sentimentScore = float(response)
            except ValueError:
                sentimentScore = "N/A"
                print(f"N/A at row {i}: {response}")
            
            newRow = row + [sentimentScore]
            data.append(newRow)

# Write the rows into a new CSV file
with open(output_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write each row from the list into the CSV file
    for row in data:
        csv_writer.writerow(row)

print(f"Data has been written to {output_file_path}")

