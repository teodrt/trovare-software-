import json,sys,subprocess,re,html
d=json.loads(subprocess.run(["curl","-sS","-m","60","https://hn.algolia.com/api/v1/items/"+sys.argv[1]],capture_output=True,text=True).stdout)
n=int(sys.argv[2]) if len(sys.argv)>2 else 600
def cl(t): return html.unescape(re.sub('<[^>]+>',' ',t or ''))
print(d.get('created_at','')[:10], d.get('title'), '\n', cl(d.get('text'))[:1500])
def walk(c,dep=0):
  for k in c.get('children',[]):
    if k.get('text'): print('  '*dep+f"- [{k['created_at'][:10]} {k.get('author')}] {cl(k['text'])[:n]}")
    if dep<1: walk(k,dep+1)
walk(d)
