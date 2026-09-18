from ddgs import DDGS


def search_web(query, max_results=5):
    """
    Search the web and return relevant results.
    """

    results = []

    with DDGS() as ddgs:
        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:
            results.append({
                "title": result.get("title", ""),
                "url": result.get("href", ""),
                "snippet": result.get("body", "")
            })

    return results


def format_sources(results):
    """
    Convert search results into text that can be
    provided to the language model.
    """

    sources = []

    for index, result in enumerate(results, start=1):
        sources.append(
            f"""
Source {index}
Title: {result['title']}
URL: {result['url']}
Information: {result['snippet']}
"""
        )

    return "\n".join(sources)