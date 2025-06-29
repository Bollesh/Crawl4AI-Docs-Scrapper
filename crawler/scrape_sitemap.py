import asyncio
import requests
from typing import List
from xml.etree import ElementTree
from crawl4ai import AsyncWebCrawler
from config.config import get_browser_config, get_crawler_config, get_memory_dispatcher

async def parallel_crawler(urls: List[str], max_concurrency: int = 10):
    async with AsyncWebCrawler(config=get_browser_config()) as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=get_crawler_config(),
            dispatcher=get_memory_dispatcher(max_concurrency)
        )
        success_count = 0
        fail_count = 0

        docs_file = "../DOCS.txt"

        with open(docs_file, 'w') as f:
            for result in results: # type: ignore
                if result.success:
                    success_count += 1
                    f.write(f"\n========== PAGE {success_count} START==========\n")
                    f.write(result.markdown)
                    f.write(f"\n========== PAGE {success_count} END==========\n")
                else:
                    print(f"Error crawling {result.url}: {result.error_message}")
                    fail_count += 1
            
        
        print(f"\nSummary:")
        print(f"  - Successfully crawled: {success_count}")
        print(f"  - Failed: {fail_count}")

def get_doc_urls(url: str):
    """
        Fetches all the links from the sitemap.xml url

        returns List[str]: List of URLs
    """

    try:
        res = requests.get(url=url)
        res.raise_for_status()

        root = ElementTree.fromstring(res.content)
        
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = {loc.text for loc in root.findall('.//ns:loc', namespace)}

        return urls

    except Exception as e:
        print(f"Error fetching sitemap: {e}")



async def scrape_sitemap(url: str, max_concurrency=10):
    urls = get_doc_urls(url)
    if urls:
        print(f"Found {len(urls)} URLs to crawl") # type: ignore
        await parallel_crawler(urls, max_concurrency=max_concurrency)  # type: ignore
    else:
        print("No URLs to crawl")


