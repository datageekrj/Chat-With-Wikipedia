import wikipediaapi

def get_wikipedia_page_text(page_title):
    user_agent = 'YourAppName/1.0 (YourContactInfo@example.com)'  # Replace with your app name and contact info
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent=user_agent
    )
    page = wiki_wiki.page(page_title)
    if not page.exists():
        return 0
    return page.text