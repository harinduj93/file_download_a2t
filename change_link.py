import csv

# Read the HTML string from the CSV file
csv_file_path = 'input.csv'

# Initialize an empty list to store HTML content
html_list = []

try:
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterate over rows and consider the second column as HTML content
        for row in csv_reader:
            if len(row) >= 2 and row[1]:  # Check if the row has at least two columns and non-empty HTML content
                html_content = row[1]
                html_list.append(html_content)

except FileNotFoundError:
    print(f"Error: CSV file '{csv_file_path}' not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Your URL to replace the existing href values
your_url = "https://www.yourwebsite.com/"

# Loop through the HTML content and replace href values
for index, html_string in enumerate(html_list, start=1):
    new_html_string = html_string.replace("https://www.a2t.ro/", your_url)

    # Print the modified HTML string for each row
    print(f"Modified HTML for Row {index}:")
    print(new_html_string)
    print("\n" + "-" * 40 + "\n")
