import asyncio
from urllib.parse import urlparse
from scrape_sitemap import scrape_sitemap
from scrape_website import scarpe_website
from scrape_llmtxt import scarpe_llmtxt

async def main():
    url = input("Enter docs home page or sitemap: ")

    def uri_validator(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except AttributeError:
            return False
        
    if not uri_validator(url):
        print("Not a valid url")
        return
    if url.find("xml") > -1:
        await scrape_sitemap(url)
    elif url.find("llm") > -1 and url.find(".txt") > -1:
        await scarpe_llmtxt(url)
    else:
        url = [url]
        await scarpe_website(url)
    print("penr")



if __name__ == "__main__":
    asyncio.run(main())
