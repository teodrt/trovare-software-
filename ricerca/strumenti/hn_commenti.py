import json,sys,urllib.parse,subprocess,re,html
q=sys.argv[1]; tags=sys.argv[2] if len(sys.argv)>2 else 'comment'; n=int(sys.argv[3]) if len(sys.argv)>3 else 10; since=int(sys.argv[4]) if len(sys.argv)>4 else 1704067200
u="https://hn.algolia.com/api/v1/search_by_date?"+urllib.parse.urlencode(dict(query=q,tags=tags,hitsPerPage=n,numericFilters=f"created_at_i>{since}"))
d=json.loads(subprocess.run(["curl","-sS","-m","60",u],capture_output=True,text=True).stdout)
for h in d['hits']:
  t=h.get('comment_text') or h.get('story_text') or ''
  t=html.unescape(re.sub('<[^>]+>',' ',t))
  # snippet around match
  k=q.strip('"').lower().split()[0]; i=t.lower().find(q.strip('"').lower()[:20]); i=max(0,i-200)
  print(f"{h['created_at'][:10]} https://news.ycombinator.com/item?id={h['objectID']} [{(h.get('story_title') or h.get('title') or '')[:60]}]\n   {t[i:i+450]}")
