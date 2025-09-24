# File Read & Write Challenge + Error Handling Lab

def modify_content(text):
    """Example modification: convert text to uppercase"""
    return text.upper()


# Ask the user for the input filename
input_filename = input("Enter the name of the file to read: ")
output_filename = "modified_" + input_filename  # Output file name

try:
    # Try to open and read the file
    with open(input_filename, "r") as infile:
        content = infile.read()

    # Modify the content
    modified_content = modify_content(content)

    # Write the modified content to a new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ File processed successfully!")
    print(f"Modified content saved to: {output_filename}")

except FileNotFoundError:
    print("❌ Error: The file you specified does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read or write this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
