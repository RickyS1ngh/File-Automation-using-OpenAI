from openai import OpenAI
from apiKey import API_KEY

client = OpenAI(api_key = API_KEY)

def newFileName(fileName, fileContent):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a file naming assistant, skilled in naming files with short names that describle what the file is. Please respond with only the file name"},
        {"role": "user", "content": f"Please suggest a new name of this file. The original file name {fileName} and the contents of the file are {fileContent} "}
    ]
    )

    return(completion.choices[0].message.content)
