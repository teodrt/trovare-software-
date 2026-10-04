# read a reddit thread (post + comments) via arctic shift
import json,sys,datetime,subprocess,time
pid=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 400
def get(u):
  for i in range(8):
    try:
      d=json.loads(subprocess.run(["curl","-sS","-m","90",u],capture_output=True,text=True).stdout or '{}')
      if 'data' in d and not d.get('error'): return d['data']
    except Exception: pass
    time.sleep(8)
  return []
p=get(f"https://arctic-shift.photon-reddit.com/api/posts/ids?ids={pid}")
for x in p: print(datetime.datetime.utcfromtimestamp(x['created_utc']).date(), x['subreddit'], x['title'], f"s{x.get('score')} c{x.get('num_comments')}\n", (x.get('selftext') or '')[:2500])
c=get(f"https://arctic-shift.photon-reddit.com/api/comments/search?link_id={pid}&limit=100")
for x in sorted(c,key=lambda x:-(x.get('score') or 0)):
  print(f"- [{datetime.datetime.utcfromtimestamp(x['created_utc']).date()} s{x.get('score')}] {(x.get('body') or '')[:n].replace(chr(10),' ')}")
