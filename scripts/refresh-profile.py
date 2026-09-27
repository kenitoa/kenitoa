"""Refresh only public repository metadata; preserve README on any API failure."""
import datetime
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REPOS = ('local-ai', 'CozyNote', '-3D-')


def fetch(path):
    headers = {'User-Agent': 'kenitoa-profile', 'Accept': 'application/vnd.github+json'}
    if os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com/' + path, headers=headers), timeout=30) as response:
        return json.load(response)


def main():
    lines = ['확인일: ' + datetime.datetime.now(datetime.timezone.utc).date().isoformat() + ' (UTC)', '']
    for repo in REPOS:
        data = fetch('repos/kenitoa/' + repo)
        releases = fetch('repos/kenitoa/' + repo + '/releases?per_page=1')
        release = releases[0] if releases else None
        label = re.sub(r'[\[\]\r\n]', '', release['tag_name']) if release else ''
        tail = f"[릴리스 {label}]({release['html_url']})" if release else '공개 릴리스 없음'
        lines.append(f"- [{repo}]({data['html_url']}) · 저장소 push: {data['pushed_at'][:10]} · {tail}")
    path = ROOT / 'README.md'
    original = path.read_text(encoding='utf-8')
    pattern = r'(?<=<!-- metadata:start -->).*?(?=<!-- metadata:end -->)'
    if len(re.findall(pattern, original, re.S)) != 1:
        raise ValueError('Expected one metadata block')
    updated = re.sub(pattern, lambda _: '\n' + '\n'.join(lines) + '\n', original, flags=re.S)
    temporary = path.with_suffix('.md.tmp')
    temporary.write_text(updated, encoding='utf-8')
    temporary.replace(path)
    print('Updated public metadata for 3 repositories')


if __name__ == '__main__':
    main()
