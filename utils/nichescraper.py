class NicheScraper:
    def __init__(self, firecrawl_api_key):
        self.firecrawl = FirecrawlApp(api_key=firecrawl_api_key)
    
    def scrape_niche_page(self, niche_url):
        """Scrape a Niche school page using Firecrawl"""
        try:
            print(f"Scraping: {niche_url}")
            
            # Use Firecrawl to scrape the page
            result = self.firecrawl.scrape(
                niche_url,
                  formats= ['markdown', 'html']
            )
            
            return {
                'url': niche_url,
                'content': result.markdown,
                'html': result.html,
                'metadata': result.metadata
            }
            
        except Exception as e:
            print(f"Error scraping {niche_url}: {e}")
            return None