#creating search paper function
import httpx

def search_papers(query):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": 5,
        "fields": "title,authors,year,abstract,url"
    }
    response = httpx.get(url, params=params)
    papers = response.json().get("data", [])
    
    results = []
    for paper in papers:
        results.append(
            f"Title: {paper['title']}\n"
            f"Authors: {', '.join([a['name'] for a in paper['authors']])}\n"
            f"Year: {paper.get('year', 'N/A')}\n"
            f"URL: {paper.get('url', 'N/A')}\n"
        )
    
    return "\n---\n".join(results) if results else "No papers found."

#defining the search paper schema

search_papers_schema = {
    "type":"function",
    "function":{
        "name":"search_papers",
        "description":"Search for academic papers related to a topic",
        "parameters":{
            "type":"object",
            "properties":{
                "query":{
                    "type":"string",
                    "description":"the search query"
                }
            },
            "required":["query"]
        }
    }
}