import requests as r


auth_key = "Bearer xxxx" # you have to fill with your auth key
post_url = "https://kepler-beta.itu.edu.tr/api/ders-kayit/v21"

headers = {"authorization": auth_key, "Connection": "keep-alive"}
post_body = {"ECRN": ["fill","with","your","crn's"], "SCRN": []}

result = {'ecrnResultList': [{'resultCode': 'VAL06'}]}

post_result = r.post(url=post_url, json=post_body, headers=headers)
result = post_result.json()
print(result)
