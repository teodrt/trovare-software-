import json,sys,urllib.parse,subprocess
base=sys.argv[1]; q=sys.argv[2]
u=base+"/search.json?"+urllib.parse.urlencode(dict(q=q))
r=subprocess.run(["curl","-sS","-m","60","-A","Mozilla/5.0",u],capture_output=True,text=True).stdout
try: d=json.loads(r)
except Exception: print('ERR',r[:200]); sys.exit()
topics={t['id']:t for t in d.get('topics',[])}
for p in d.get('posts',[])[:int(sys.argv[3]) if len(sys.argv)>3 else 20]:
  t=topics.get(p['topic_id'],{})
  print(f"{p['created_at'][:10]} likes{p.get('like_count')} | {t.get('title','')[:90]} | {base}/t/{t.get('slug','')}/{p['topic_id']}\n    {p.get('blurb','')[:260]}")
