"""Check profile assets, navigation and external destinations without dependencies."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import urllib.request

root = Path(__file__).resolve().parents[1]
text = (root / 'README.md').read_text(encoding='utf-8')
for path in re.findall(r'src="([^"]+)"', text):
    assert (root / path).is_file(), f'Missing asset: {path}'
for target in re.findall(r'\]\((docs/[^)]+)\)', text):
    assert (root / target).is_file(), f'Missing document: {target}'
headings = {re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-') for heading in re.findall(r'^## (.+)$', text, re.M)}
for anchor in re.findall(r'\]\(#([^)]+)\)', text):
    assert anchor in headings, f'Missing section: {anchor}'
urls = sorted({url.split('#')[0] for url in re.findall(r'https://[^\s)"<>]+', text)})


def check(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'kenitoa-profile'})
    with urllib.request.urlopen(request, timeout=30) as response:
        assert response.status == 200, f'{url}: {response.status}'


with ThreadPoolExecutor(max_workers=6) as pool:
    list(pool.map(check, urls))
print(f'Assets, documents, navigation and {len(urls)} external destinations OK')
