# high-engagement filter: list posts with score>=MIN_S or comments>=MIN_C matching regex
import json,sys,datetime,urllib.parse,subprocess,re,time
sub=sys.argv[1]; pat=re.compile(sys.argv[2],re.I); after=sys.argv[3]; before=sys.argv[4]; pages=int(sys.argv[5]); ms=int(sys.argv[6]); mc=int(sys.argv[7])
ok=err=0
while ok<pages and err<25:
  u="https://arctic-shift.photon-reddit.com/api/posts/search?"+urllib.parse.urlencode(dict(subreddit=sub,limit=100,after=after,before=before,sort='desc'))
  try: d=json.loads(subprocess.run(["curl","-sS","-m","90",u],capture_output=True,text=True).stdout or '{}')
  except Exception: d={}
  if d.get('error') or 'data' not in d: err+=1; time.sleep(15); continue
  ok+=1; ps=d['data']
  if not ps: break
  for p in ps:
    if (p.get('score') or 0)>=ms or (p.get('num_comments') or 0)>=mc:
      if pat.search(p['title']+' '+(p.get('selftext') or '')):
        print(f"{datetime.datetime.utcfromtimestamp(p['created_utc']).date()} s{p.get('score')} c{p.get('num_comments')} | {p['title'][:120]} | https://reddit.com/r/{sub}/comments/{p['id']}")
  before=str(int(ps[-1]['created_utc'])); time.sleep(2)
