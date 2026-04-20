"""
Fetches the total citation count for Marc Porosoff from Google Scholar
and updates the stat in index.html.
"""

import re
import sys
from scholarly import scholarly

SCHOLAR_ID = "a3zZPXwAAAAJ"   # Google Scholar user ID
INDEX_FILE = "index.html"

def get_citation_count():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics"])
    return author.get("citedby", None)

def update_html(count):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Match the citation stat block, e.g.: <div class="stat-num">6,037</div>
    # followed by a stat-label containing "Citations"
    pattern = r'(<div class="stat-num">)([\d,+]+)(</div>\s*<div class="stat-label">Total Citations</div>)'
    formatted = f"{count:,}"
    new_html, n = re.subn(pattern, rf'\g<1>{formatted}\g<3>', html)

    if n == 0:
        print("WARNING: Citation stat block not found in index.html — pattern may need updating.")
        sys.exit(1)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"Updated citation count to {formatted}.")

if __name__ == "__main__":
    print("Fetching citation count from Google Scholar...")
    count = get_citation_count()
    if count is None:
        print("ERROR: Could not retrieve citation count.")
        sys.exit(1)
    print(f"Citations found: {count}")
    update_html(count)
