#search tool schema

search_tool = {
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