import json
import requests
url=requests.get("http://join.navgurukul.org/api/partners")
r=json.loads(url.text)
g=[]
v=[]
i=0
for i in range(len(r["data"])):
    f=r["data"][i]["id"]
    g.append(f)
d=input("enter no")
def acending():
        g.sort()
        for j in range(len(g)):
            for k in range(len(r["data"])):
                if g[j]==r["data"][k]["id"]:
                    b=r["data"][k]
                    v.append(b)
def decending():
        g.sort(reverse=True)
        for j in range(len(g)):
            for k in range(len(r["data"])):
                if g[j]==r["data"][k]["id"]:
                    b=r["data"][k]
                    v.append(b)
def find():
    if d=="acending":
        acending()
    elif d=="decending":
        decending()
find()
with open ("siya.json","w")as t:
    json.dump(v,t,indent=2)

