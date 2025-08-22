from urllib.parse import quote, urljoin
from bs4 import BeautifulSoup
import requests
import time
import random
import json

class SchoolSearcher:
    def __init__(self):
        self.session = requests.Session()
        # Rotate user agents to appear more human-like
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
        ]
    
    def _get_random_headers(self):
        """Get randomized headers to avoid detection"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
    
    def serpapi_search(self, query, api_key, num_results=10):
        """Use SerpAPI for reliable Google search results"""
        try:
            import serpapi
            
            search = serpapi.GoogleSearch({
                "q": query,
                "num": num_results,
                "api_key": api_key
            })
            
            results = search.get_dict()
            organic_results = results.get("organic_results", [])
            
            formatted_results = []
            for result in organic_results:
                formatted_results.append({
                    'title': result.get('title', ''),
                    'url': result.get('link', ''),
                    'snippet': result.get('snippet', '')
                })
            
            return formatted_results
            
        except ImportError:
            print("SerpAPI not installed. Install with: pip install google-search-results")
            return []
        except Exception as e:
            print(f"Error with SerpAPI: {e}")
            return []
    
    def duckduckgo_search(self, query, num_results=10):
        """Use DuckDuckGo as alternative search engine"""
        try:
            # from duckduckgo_search import DDGS
            from ddgs import DDGS
            
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=num_results))
                
            formatted_results = []
            for result in results:
                formatted_results.append({
                    'title': result.get('title', ''),
                    'url': result.get('href', ''),
                    'snippet': result.get('body', '')
                })
            
            return formatted_results
            
        except ImportError:
            print("DuckDuckGo search not installed. Install with: pip install duckduckgo-search")
            return []
        except Exception as e:
            print(f"Error with DuckDuckGo search: {e}")
            return []

    
    def find_niche_link(self, school_name, search_method='duckduckgo', api_key=None):
        """Search for school's Niche page using multiple methods"""
        query = f"{school_name} site:niche.com"
        

        # Fallback to search engines
        if search_method == 'serpapi' and api_key:
            results = self.serpapi_search(query, api_key, num_results=5)
        elif search_method == 'duckduckgo':
            results = self.duckduckgo_search(query, num_results=5)


        
        niche_links = []
        for result in results:
            if 'niche.com' in result['url']:
                niche_links.append(result)
        
        return niche_links
    
    def search_school_comprehensive(self, school_name, search_method='duckduckgo', api_key=None):
        """Get comprehensive search results for a school"""
        print(f"Searching for: {school_name} using {search_method}")
        
        # Search for general school info
        if search_method == 'serpapi' and api_key:
            general_results = self.serpapi_search(f"{school_name} school", api_key)
        elif search_method == 'duckduckgo':
            general_results = self.duckduckgo_search(f"{school_name} school")
        elif search_method == 'selenium':
            general_results = self.google_search_with_selenium(f"{school_name} school")
        else:
            general_results = self.google_search_stealth(f"{school_name} school")
        
        # Search specifically for Niche page
        niche_results = self.find_niche_link(school_name, search_method, api_key)
        
        return {
            'school_name': school_name,
            'general_results': general_results[:5],  # Top 5 general results
            'niche_results': niche_results
        }