import os
from zipfile import ZipFile

def main():
    # Step 1: User Input
    user_input = input("What do you want to build? ")
    
    # Step 2: Send Prompt to AI
    ai_response = send_prompt_to_ai(user_input)
    file_structure = parse_ai_response(ai_response)
    
    # Step 3: Generate Files
    generated_files = []
    for filename, content in file_structure.items():
        filepath = os.path.join("generated_app", filename)
        with open(filepath, "w") as file:
            file.write(content)
        generated_files.append(filepath)
    
    # Ensure we don't exceed 20 files
    if len(generated_files) > 20:
        print("Error: Maximum file limit exceeded.")
        return
    
    # Step 4: Zip Output
    zip_output(generated_files, "application.zip")
    
    # Optional Step 5: Testing
def send_prompt_to_ai(prompt):
    return {"file_structure": {}}

def parse_ai_response(response):
    return {}

def zip_output(filepaths, zip_filename):
    with ZipFile(zip_filename, 'w') as zipObj:
        for filePath in filepaths:
            zipObj.write(filePath, os.path.basename(filePath))

if __name__ == "__main__":
    main()
