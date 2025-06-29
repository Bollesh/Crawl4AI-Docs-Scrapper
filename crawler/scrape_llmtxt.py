import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
import re

async def scrape_and_chunk_md(url: str):
    """
        Scrape markdown and split into chunks
    """

    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig()
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)
        if not result.success: # type: ignore
            print("Failed to fetch markdown")
            return
        markdown = result.markdown  # type: ignore

        header_pattern = re.compile(r'^(# .+|## .+)$', re.MULTILINE)

        headers = [m.start() for m in header_pattern.finditer(markdown)] + [len(markdown)]

        chunks = []

        for i in range(len(headers) - 1):
            chunk = markdown[headers[i]:headers[i+1]].strip()
            if chunk:
                chunks.append(chunk)

        print(f"Split into {len(chunks)} chunks:")

        docs_file = "../DOCS.txt"

        with open(docs_file, "w") as f:
            for idx, chunk in enumerate(chunks):
                f.write(f"{chunk}\n")
                print(f"\n--- Chunk {idx+1} ---\n{chunk}\n")

async def scarpe_llmtxt(url):
    await scrape_and_chunk_md(url)
        
