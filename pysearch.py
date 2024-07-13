"""This module is can be used to Google Search using SerpApi. SerpApi key is needed to use this module."""

import requests

def google_search(query, num_results, key):
    """This function takes 3 aruguments, i.e.,
    query - Tell what you want to search on google,
    num_results - Specify number of results you want (provide a number between 1 - 10),
    key - SerpApi key.
    """
    url = 'https://serpapi.com/search'
    params = {
        'q': query,
        'api_key': key,
        'num': num_results
    }
    response = requests.get(url, params=params)
    results = response.json()
    
    # Extracting the results
    top_results = results.get('organic_results', [])[:num_results]
    
    # Display all the results
    if top_results:
        for i, result in enumerate(top_results, start=1):
            print(f"Result {i}:")
            print(f"Title: {result.get('title')}")
            print(f"Link: {result.get('link')}")
            print(f"Snippet: {result.get('snippet')}\n")
    else:
        print("No results found")