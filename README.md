# School Search and Niche Scraper

A comprehensive tool to search for schools, scrape their Niche.com pages using Firecrawl, and generate summaries using Google's Gemini Pro AI.

## Features

- **Multiple Search Methods**: DuckDuckGo, SerpAPI, Selenium, and direct URL construction
- **Web Scraping**: Clean content extraction using Firecrawl
- **AI Summarization**: Intelligent summaries using Gemini Pro
- **Batch Processing**: Handle multiple schools with rate limiting
- **Jupyter Notebook**: Interactive development environment

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the test**:
   ```bash
   python test_search.py
   ```

4. **Use the Jupyter notebook**:
   ```bash
   jupyter notebook check.ipynb
   ```

## Search Methods

### 1. DuckDuckGo (Recommended)
- Free and reliable
- No API key required
- Best for general use

### 2. Direct Niche URL Construction
- Fastest method
- Works for most major schools
- No external API calls

### 3. SerpAPI
- Most accurate Google results
- Requires paid API key
- Professional-grade reliability

### 4. Selenium
- Uses real browser
- Bypasses most bot detection
- Requires Chrome/ChromeDriver

## API Keys Required

- **Firecrawl**: Get from [firecrawl.dev](https://firecrawl.dev)
- **Gemini Pro**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **SerpAPI** (optional): Get from [serpapi.com](https://serpapi.com)

## Usage Example

```python
from utils.gsearch import SchoolSearcher

searcher = SchoolSearcher()

# Search for a school
results = searcher.search_school_comprehensive("Harvard University", "duckduckgo")

# Get Niche links
niche_links = results['niche_results']
print(f"Found {len(niche_links)} Niche pages")
```

## Project Structure

```
├── check.ipynb              # Main Jupyter notebook
├── utils/
│   ├── gsearch.py          # School search functionality
│   └── nichescraper.py     # Niche scraping utilities
├── test_search.py          # Test different search methods
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - feel free to use this project for your own purposes.

## Troubleshooting

### Google Search Blocked
- Use DuckDuckGo method instead
- Try the Selenium method with delays
- Consider using SerpAPI for reliable results

### Firecrawl Errors
- Check your API key is valid
- Ensure you have sufficient credits
- Try with a smaller batch size

### Gemini API Issues
- Verify your API key is active
- Check rate limits
- Ensure content isn't too long (8000 chars max)