#creating search paper function

def search_papers(query):
    return f"found papers for : {query}"

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