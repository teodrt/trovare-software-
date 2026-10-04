# list posts in a subreddit across a time window (paged), filter locally by regex on title+selftext
import json,sys,datetime,urllib.parse,subprocess,re,time
sub=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); after=sys.argv[3]; before=sys.argv[4]; pages=int(sys.argv[5]) if len(sys.argv)>5 else 5
seen=0
ok=0;err=0
while ok<pages and err<25:
  u="https://arctic-shift.photon-reddit.com/api/posts/search?"+urllib.parse.urlencode(dict(subreddit=sub,limit=100,after=after,before=before,sort='desc'))
  try: d=json.loads(subprocess.run(["curl","-sS","-m","90",u],capture_output=True,text=True).stdout or '{}')
  except Exception: d={}
  if d.get('error') or 'data' not in d: err+=1; time.sleep(15); continue
  ok+=1
  ps=d.get('data') or []
  if not ps: break
  for p in ps:
    seen+=1
    txt=p['title']+' '+(p.get('selftext') or '')
    m=pat.search(txt)
    if m:
      st=(p.get('selftext') or '').replace('\n',' ')
      i=max(0,st.lower().find(m.group(0).lower())-150)
      print(f"{datetime.datetime.utcfromtimestamp(p['created_utc']).date()} s{p.get('score')} c{p.get('num_comments')} | {p['title'][:110]} | https://reddit.com/r/{sub}/comments/{p['id']}\n     …{st[i:i+330]}")
  before=str(int(ps[-1]['created_utc']))
  time.sleep(2)
print('scanned',seen)
