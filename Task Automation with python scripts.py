import re
from pathlib import Path
# النمط القياسي للبريد الالكتروني
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
def validate_email(input_file: str, output_file: str) -> None:
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        print(f"Input file '{input_file}' does not exist.")
        return

    try : 
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()

        emails= set(re.findall(email_pattern, content))

        if not emails:
            print("No valid email addresses found in the input file.")
            return
        with open(output_path, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(f"{email}\n")
        print(f"Valid email addresses have been saved to '{output_file}'.")
        print(f"Successfully extracted {len(emails)} unique email addresses, and saved them to:'{output_file}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to the input text file: ")
    output_file = input("Enter the path to the output text file: ")
    validate_email(input_file, output_file)