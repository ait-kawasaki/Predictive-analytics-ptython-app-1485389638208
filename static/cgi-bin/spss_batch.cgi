# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import json

url = "https://ibm-watson-ml.mybluemix.net/pm/v1/score/test1"
print url

querystring = {"accesskey": "N4LnXREVJ44YgZy4MCnIJaU7NCAxoihZBHpVqS6abjaubA3inBFJ/eM4ZBhB2AxLHxGxQ3pIogjgEOjN0TGDTcL0h32gVzPkwMbmHXNpi+EC1T08nu1092OflnlsegKP1CVHD9o08LGV730psB98ePdHELxpedVqkCUxFn4YxR0="}
#payload = "{\"tablename\":\"Web新規申し込み\",\"header\":[\"顧客番号\",\"性別\",\"年齢\",\"職業区分\",\"所有車区分\",\"所有車メーカー\",\"下取り\",\"Web検索語スコア\",\"Web滞在秒数\",\"Web遷移スコア\",\"Web遷移タイプ\",\"検討度合\",\"運転歴\"], \"data\":[[9817297,\"男性\",24,\"自営業\",\"他社\",\"外国車\",\"ない\",112,269,2,\"タイプA\",3,0]]}"
payload = {
    'tablename': 'Web新規申し込み',
    'header': ['顧客番号','性別','年齢','職業区分','所有車区分','所有車メーカー','下取り','Web検索語スコア','Web滞在秒数','Web遷移スコア','Web遷移タイプ','検討度合','運転歴'],
    'data': [[9817297,'男性',24,'自営業','他社','外国車','ない',112,269,2,'タイプA',3,0]]
    }
headers = {
    'content-type': "application/json;charset=UTF-8"
    }

response = requests.request("POST", "https://ibm-watson-ml.mybluemix.net/pm/v1/score/test1",headers=headers,params=querystring, data=json.dumps(payload))

print "Content-type: text/html"
print
print "<title>Test CGI</title>"
print "<p>Hello World!</p>"
print(response.text)