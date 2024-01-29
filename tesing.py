import csv
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

input_csv_filename = 'input.csv'
output_csv_filename = 'output.csv'

# ... (rest of your code remains unchanged)

# Function to download files
def download_file(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from the URL
        filename = os.path.basename(urlparse(url).path)

        # Ensure the filename is not empty
        if not filename:
            raise ValueError("Empty filename")

        # Save the content to the file in the same location as the script with tqdm progress bar
        bar_format = "{desc}{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}]"
        with tqdm.wrapattr(open(filename, 'wb'), "write", miniters=1, desc=filename, total=int(response.headers.get('content-length', 0)), unit='B', unit_scale=True, bar_format=bar_format, colour='green') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f'Downloaded: {filename}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading {url}: {e}')
    except ValueError as ve:
        print(f'Error extracting filename for {url}: {ve}')

# Function to download files concurrently using threads
def download_files_concurrently(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:  # You can adjust max_workers as needed
        executor.map(download_file, urls)

# Generate output CSV file
#make_url_list(input_csv_filename)

# Get the list of URLs from output CSV file
with open(output_csv_filename, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    urls = [row[0] for row in csv_reader]  # Assuming URLs are in the first column

# Download files concurrently
download_files_concurrently(urls)
