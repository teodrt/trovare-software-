import json,sys,datetime,urllib.parse,subprocess,time
sub=sys.argv[1]; q=sys.argv[2]; after=sys.argv[3] if len(sys.argv)>3 else '2024-01-01'; field=sys.argv[4] if len(sys.argv)>4 else 'query'
u="https://arctic-shift.photon-reddit.com/api/posts/search?"+urllib.parse.urlencode({'subreddit':sub,field:q,'limit':25,'after':after})
for i in range(10):
  try: d=json.loads(subprocess.run(["curl","-sS","-m","90",u],capture_output=True,text=True).stdout or '{}')
  except Exception: d={}
  if 'data' in d and not d.get('error'): break
  time.sleep(12)
for p in d.get('data') or []:
  print(f"{datetime.datetime.utcfromtimestamp(p['created_utc']).date()} s{p.get('score')} c{p.get('num_comments')} | {p['title'][:110]} | https://reddit.com/r/{p['subreddit']}/comments/{p['id']}")
if not d.get('data'): print('NONE/ERR', d.get('error'))
