import asyncio
from urllib.parse import urldefrag
from crawl4ai import AsyncWebCrawler
from config.config import get_browser_config, get_crawler_config, get_memory_dispatcher

async def recursive_crawler(start_urls, max_depth=3, max_concurreny=10):
    all_pages = []
    visited = set()
    
    def normalize_url(url:str):
        return urldefrag(url)[0]
    
    current_urls = set([normalize_url(u) for u in start_urls])

    async with AsyncWebCrawler(config=get_browser_config()) as crawler:
        for depth in range(max_depth):
            print(f"\n=== Crawling Depth {depth+1} ===")

            urls_to_crawl = [normalize_url(u) for u in current_urls if normalize_url(u) not in visited]            

            if not urls_to_crawl:
                break

            results = await crawler.arun_many(
                urls=urls_to_crawl,
                config=get_crawler_config(),
                dispatcher=get_memory_dispatcher(max_concurreny)
            )

            next_level_urls = set()
            

            for result in results: # type: ignore
                norm_url = normalize_url(result.url)
                visited.add(norm_url)

                if(result.success):
                    print(f"[OK] {result.url} | Markdown: {len(result.markdown) if result.markdown else 0}")
                    all_pages.append(result.markdown)
                    
                    for link in result.links.get("internal", []):
                        next_url = normalize_url(link['href'])
                        if next_url not in visited:
                            next_level_urls.add(next_url)
                else:
                    print(f"[ERROR] {result.url}: {result.error_message}")
                
            current_urls = next_level_urls
    return all_pages

async def scarpe_website(url, max_depth=2, max_concurrency=10):
    all_pages = await recursive_crawler(url, max_depth=max_depth, max_concurreny=max_concurrency)
    docs_file = "../DOCS.txt"

    with open(docs_file, "w") as f:
        f.write("\n\n".join(all_pages))


