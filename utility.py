def format_apa(author, year, title, journal, volume, issue, pages, doi):
    """
    Generate an APA-style citation.
    """
    return f"{author} ({year}). {title}. {journal}, {volume}({issue}), {pages}. https://doi.org/{doi}"

# Example usage
example_citation = format_apa(
    author="Doe, J.",
    year="2023",
    title="The Role of AI in Modern Research",
    journal="Journal of Artificial Intelligence",
    volume="10",
    issue="1",
    pages="45-67",
    doi="10.1234/ai.2023.5678"
)

print(example_citation)
