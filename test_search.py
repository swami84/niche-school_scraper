#!/usr/bin/env python3

from utils.gsearch import SchoolSearcher
import os
from dotenv import load_dotenv

load_dotenv()

def test_search_methods():
    searcher = SchoolSearcher()
    test_school = "Harvard University"
    
    print("Testing different search methods for:", test_school)
    print("=" * 60)
    
    # Method 1: DuckDuckGo (Recommended - no API key needed)
    print("\n1. Testing DuckDuckGo Search:")
    try:
        results = searcher.search_school_comprehensive(test_school, 'duckduckgo')
        print(f"Found {len(results['niche_results'])} Niche results")
        for result in results['niche_results']:
            print(f"  - {result['title']}: {result['url']}")
    except Exception as e:
        print(f"DuckDuckGo failed: {e}")
    
    # Method 2: Direct Niche URL construction
    print("\n2. Testing Direct Niche URL Construction:")
    try:
        direct_results = searcher.direct_niche_search(test_school)
        print(f"Found {len(direct_results)} direct URLs")
        for result in direct_results:
            print(f"  - {result['title']}: {result['url']}")
    except Exception as e:
        print(f"Direct search failed: {e}")
    
    # Method 3: SerpAPI (if API key available)
    serpapi_key = os.getenv('SERPAPI_KEY')
    if serpapi_key:
        print("\n3. Testing SerpAPI:")
        try:
            results = searcher.search_school_comprehensive(test_school, 'serpapi', serpapi_key)
            print(f"Found {len(results['niche_results'])} Niche results")
            for result in results['niche_results']:
                print(f"  - {result['title']}: {result['url']}")
        except Exception as e:
            print(f"SerpAPI failed: {e}")
    else:
        print("\n3. SerpAPI: No API key found (set SERPAPI_KEY in .env)")
    
    # Method 4: Selenium (if installed)
    print("\n4. Testing Selenium (if available):")
    try:
        results = searcher.search_school_comprehensive(test_school, 'selenium')
        print(f"Found {len(results['niche_results'])} Niche results")
        for result in results['niche_results']:
            print(f"  - {result['title']}: {result['url']}")
    except Exception as e:
        print(f"Selenium failed: {e}")

if __name__ == "__main__":
    test_search_methods()