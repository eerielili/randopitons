import requests
USERNAME = "lionel.miquel46@gmail.com"
PASSWORD = "VEobWylvUdToab8"
LOGINURL = "https://randopitons.re"
DATAURL = "https://randopitons.re/randonnees/region/cirque-cilaos"
session = requests.session()
req_headers = {
'POST /connexion HTTP/1.1'

'Host: randopitons.re'
 
'Connection: keep-alive'
 
'Content-Length: 57'
 
'Cache-Control: max-age=0'
 
'Origin: https://randopitons.re'
 
'Upgrade-Insecure-Requests: 1'
 
'Content-Type: application/x-www-form-urlencoded'
 
'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/68.0.3440.106 Chrome/68.0.3440.106 Safari/537.36'

'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
 
'Referer: https://randopitons.re/connexion'
 
'Accept-Encoding: gzip, deflate, br'
 
'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
 
'Cookie: randop_sess=ac5cd2e84ea151bd16bf787ea46f8c95ef867684"'
}
 
formdata = {
     'UserName': USERNAME,
     'Password': PASSWORD,
     'LoginButton' : 'Login'
 }
 
 # Authenticate
r = session.post(LOGINURL, data=formdata, headers=req_headers, allow_redirects=True)
print (r.headers)
print (r.status_code)
print (r.text)
 
 # Read data
r2 = session.get(DATAURL)
print ("___________DATA____________")
print (r2.headers)
print (r2.status_code)
print (r2.text)

