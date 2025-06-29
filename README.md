# Crawl4AI Documentation Crawler

## Description

`Crawl4AI` is a powerful web crawler designed to scrape and process documentation from various sources, including websites, sitemaps, and large language model (LLM) text files. This project leverages modern asynchronous programming techniques with `aiohttp` for efficient web scraping and `Crawl4AI` to get markdown which can be easy for LLMs to read, rather than raw HTML

## Features

- **Asynchronous Scraping**: Utilizes `asyncio` to handle multiple requests concurrently.
- **Sitemap Parsing**: Supports crawling from sitemap URLs, extracting and processing all linked pages.
- **Website Crawler**: Recursively crawls websites up to a specified depth, handling internal links efficiently.
- **LLM Text Processing**: Extracts and chunks markdown content from LLM text files for further processing.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-url.git
   cd your-repo-name
   ```

2. Install the required dependencies using `pip`:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables (if any) in a `.env` file or use `python-dotenv` to load them from a `.env` file.

## Usage

### Running the Crawler

To run the crawler, execute the following command:

```sh
python project/crawler/main.py
```

You will be prompted to enter the URL of the documentation home page or sitemap. The script will then proceed to scrape and process the content based on the provided URL.

### Example Usage

1. **Crawling a Website**:
   ```sh
   python project/crawler/main.py
   Enter docs home page or sitemap: https://example.com/docs
   ```

2. **Crawling from Sitemap**:
   ```sh
   python project/crawler/main.py
   Enter docs home page or sitemap: https://example.com/sitemap.xml
   ```

3. **Processing LLM Text Files**:
   ```sh
   python project/crawler/main.py
   Enter docs home page or sitemap: https://example.com/llm.txt
   ```

## Project Structure

The project is organized as follows:

```
project/
├── crawler/
│   ├── main.py
│   ├── scrape_llmtxt.py
│   └── scrape_sitemap.py
│   └── scrape_website.py
├── crawler/config/
│   └── config.py
└── requirements.txt
```

- **crawler/**: Contains the core logic for scraping and processing documentation.
  - `main.py`: The entry point of the application, handling user input and dispatching tasks to other modules.
  - `scrape_llmtxt.py`: Handles scraping and chunking markdown content from LLM text files.
  - `scrape_sitemap.py`: Crawls sitemaps to extract URLs for further processing.
  - `scrape_website.py`: Recursively crawls websites up to a specified depth.

- **crawler/config/**: Configuration settings for the web crawler.
  - `config.py`: Defines configuration parameters such as browser and crawler run configurations.

## Dependencies

The project relies on the following packages:

```plaintext
aiofiles==24.1.0
aiohappyeyeballs==2.6.1
aiohttp==3.12.13
aiosignal==1.3.2
aiosqlite==0.21.0
annotated-types==0.7.0
anyio==4.9.0
attrs==25.3.0
beautifulsoup4==4.13.4
Brotli==1.1.0
certifi==2025.6.15
cffi==1.17.1
chardet==5.2.0
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
Crawl4AI==0.6.3
cryptography==45.0.4
cssselect==1.3.0
distro==1.9.0
fake-http-header==0.3.5
fake-useragent==2.2.0
filelock==3.18.0
frozenlist==1.7.0
fsspec==2025.5.1
greenlet==3.2.3
h11==0.16.0
hf-xet==1.1.5
httpcore==1.0.9
httpx==0.28.1
huggingface-hub==0.33.1
humanize==4.12.3
idna==3.10
importlib_metadata==8.7.0
Jinja2==3.1.6
jiter==0.10.0
joblib==1.5.1
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
litellm==1.73.2
lxml==5.4.0
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
multidict==6.6.0
nltk==3.9.1
numpy==2.3.1
openai==1.92.2
packaging==25.0
pillow==10.4.0
playwright==1.53.0
propcache==0.3.2
psutil==7.0.0
pycparser==2.22
pydantic==2.11.7
pydantic_core==2.33.2
pyee==13.0.0
Pygments==2.19.2
pyOpenSSL==25.1.0
pyperclip==1.9.0
python-dotenv==1.1.1
PyYAML==6.0.2
rank-bm25==0.2.2
referencing==0.36.2
regex==2024.11.6
requests==2.32.4
rich==14.0.0
rpds-py==0.25.1
sniffio==1.3.1
snowballstemmer==2.2.0
soupsieve==2.7
```
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to explore, contribute, and enhance this project! 🚀
