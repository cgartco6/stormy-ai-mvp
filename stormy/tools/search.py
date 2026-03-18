from duckduckgo_search import DDGS

def web_search(query: str, max_results: int = 3) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "Found nothing. Maybe stop asking dumb questions."
        summary = "\n".join([f"• {r['title']}: {r['body'][:140]}..." for r in results])
        return f"Search results, genius:\n{summary}"
    except Exception as e:
        return f"Search crashed. Probably your fault. {str(e)}"
