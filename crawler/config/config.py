from crawl4ai import BrowserConfig, CrawlerRunConfig, MemoryAdaptiveDispatcher, CacheMode

def get_browser_config():
    return BrowserConfig(
    headless=True,
    verbose=False,
    extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"]
)

def get_crawler_config():
    return CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS, 
    stream=False
)

def get_memory_dispatcher(max_concurrency: int):
    return MemoryAdaptiveDispatcher(
    memory_threshold_percent=70.0,
    check_interval=1.0,
    max_session_permit=max_concurrency
)