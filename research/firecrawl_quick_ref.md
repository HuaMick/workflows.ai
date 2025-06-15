# Firecrawl Quick Reference

Firecrawl is a service that allows you to turn websites into LLM-ready markdown. It can crawl all accessible subpages of a URL and provide clean markdown for each one.

## Key Features

- **Scrape**: Scrapes a single URL and returns its content in various formats (markdown, HTML, etc.).
- **Crawl**: Recursively crawls a website from a starting URL, scraping all accessible subpages.
- **Search**: a web search that returns scraped content from the results.
- **Extract**: Uses an LLM to extract structured data from a page.
- **Actions**: Allows for interaction with a page (clicking, scrolling, typing) before scraping.

## Installation

To use Firecrawl in a Python project, you need to install the `firecrawl-py` library:

```bash
pip install firecrawl-py
```

## Authentication

Firecrawl requires an API key for all requests. The key should be passed to the `FirecrawlApp` constructor.

```python
from firecrawl import FirecrawlApp

# It's recommended to load the API key from environment variables
# In this project, it is handled by the MCP configuration.
# os.getenv("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key="YOUR_FIRECRAWL_API_KEY")
```

## Basic Usage

### Scraping a URL

To scrape a single URL, use the `scrape_url` method.

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp() # api_key is read from FIRECRAWL_API_KEY env var

scrape_result = app.scrape_url('https://docs.firecrawl.dev/')

# The result is a dictionary containing the scraped data.
print(scrape_result['markdown'])
```

### Crawling a Website

To crawl a website, use the `crawl_url` method. This is an asynchronous operation. The method returns a list of dictionaries, where each dictionary represents a scraped page.

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp() # api_key is read from FIRECRAWL_API_KEY env var

crawl_result = app.crawl_url('https://docs.firecrawl.dev/', limit=10)

for page in crawl_result:
    print(f"URL: {page['metadata']['sourceURL']}")
    print(f"Markdown: {page['markdown'][:200]}...")
```

## Advanced Usage

### LLM-based Extraction

Firecrawl can extract structured data from a webpage using a Pydantic schema.

```python
from firecrawl import FirecrawlApp, JsonConfig
from pydantic import BaseModel, Field
from typing import List

app = FirecrawlApp()

class Article(BaseModel):
    title: str
    url: str

class TopArticles(BaseModel):
    articles: List[Article] = Field(description="List of top articles")


llm_extraction_result = app.scrape_url(
    'https://news.ycombinator.com',
    formats=["json"],
    json_options=JsonConfig(
        schema=TopArticles.model_json_schema()
    )
)

if llm_extraction_result.json:
    # Process the extracted JSON data
    print(llm_extraction_result.json)
```
### Actions
Firecrawl can perform actions on a page before scraping.

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp()

scrape_result = app.scrape_url('google.com',
    actions=[
        {"type": "write", "selector": "textarea[title=\\"Search\\"]", "text": "firecrawl"},
        {"type": "press", "key": "Enter"},
        {"type": "wait", "milliseconds": 2000},
        {"type": "scrape"},
    ]
)

print(scrape_result)

```

For more details, refer to the [official Firecrawl documentation](https://docs.firecrawl.dev/). 