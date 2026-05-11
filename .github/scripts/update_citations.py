"""
Fetches the total citation count for Marc Porosoff from the Semantic Scholar API
and updates the stat in index.html.

Uses the public Semantic Scholar Graph API — no key required, no scraping.
Author ID: 13791234
"""

import json
import re
import sys
import urllib.request

AUTHOR_ID  = "13791234"   # Semantic Scholar author ID
API_URL    = f"https://api.semanticscholar.org/graph/v1/author/{AUTHOR_ID}?fields=citationCount"
INDEX_FILE = "index.html"

def get_citation_count():
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "porosoffresearchgroup-citation-bot/1.0"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return data.get("citationCount")

def update_html(count):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Match the citation stat block, e.g.: <div class="stat-num">6,166</div>
    # followed by a stat-label containing "Total Citations"
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
    print("Fetching citation count from Semantic Scholar API...")
    try:
        count = get_citation_count()
    except Exception as e:
        print(f"ERROR: Could not retrieve citation count: {e}")
        sys.exit(1)

    if count is None:
        print("ERROR: citationCount field missing from API response.")
        sys.exit(1)

    print(f"Citations found: {count}")
    update_html(count)
