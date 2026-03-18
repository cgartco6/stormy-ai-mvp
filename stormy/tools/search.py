from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 3) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "Found nothing useful. Maybe you're asking stupid questions again."
        summary = "\n".join([f"- {r['title']}: {r['body'][:150]}..." for r in results])
        return f"Here's what I found, genius:\n{summary}"
    except Exception as e:
        return f"Search failed because the internet hates you. Error: {str(e)}"
