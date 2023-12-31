# Specify the file path in the D drive where you want to create the file
file_path = r"D:\one.txt"

# Open the file in write mode ('w') to create it
# You can also use 'a' mode to append to an existing file
try:
    with open(file_path, 'w') as file:
        # You can write content to the file if needed
        file.write("This is a sample text in the file.")
    print(f"File '{file_path}' created successfully.")
except Exception as e:
    print(f"Error: {str(e)}")

