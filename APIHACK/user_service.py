import json
import jwt

from flask import Flask ,request, session, send_from_directory

application = Flask(__name__, static_url_path='')
app=application
#ROLE FOR AC007
APIKEY = 'WITCHERFLAG4445663337899'
JWTSECRET = 'supersecret'

error_response = '{"status","operation failed"}'
success_response = '{"status","operation successful"}'
#admin_token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoid2l0Y2hlciIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTUxNjIzOTAyMn0.b5ZxYXLWdDMMLRvtCkv7ODu336dQ4rt2_xnpvYUh4fY"


SELREGFLAG = 'WITCHERFLAG9899877665588'
APIVERFLAG = 'WITCHERFLAG0099876655774'
ADMINFLAG  = 'WITCHERFLAG1116536788549'
AUTHERR= 'INVALID_TOKEN'

# set the project root directory as the static folder, you can set others.

#Load static JSON FILE 
user_data = json.load(open("./Data/user.json"))
#student_list = json.load("./Data/user.json"))

#Home Page 
@app.route("/")
def getRoot():
    return send_from_directory('.','index.html')

#index.html
@app.route("/index.html")
def getIndex():
    return send_from_directory('.','index.html')

#img1
@app.route("/img1.jpg")
def getImg1():
    return send_from_directory('.','img1.jpg')


# create jwt token 
def createJWT(uname):
    try:
        encoded_jwt = jwt.encode({"uname": uname,"role":APIKEY }, JWTSECRET, algorithm="HS256")
        #print (encoded_jwt)
        return encoded_jwt
    except:
        return AUTHERR

# Decode JWT 
def validateLogon(token):
    try:
        decoded = jwt.decode(token,JWTSECRET,algorithms='HS256')
        return decoded
    except:
        return AUTHERR

# Admin Validation Function - BAD JWT 
def validateAdmin(token):
    try:
       decoded = jwt.decode(token,options={"verify_signature":False})
       return decoded
    except:
        return AUTHERR
# API1: Login 
@app.route("/login", methods=["GET","POST"])
def login():
    try:
        logindata = json.loads(str(request.data,"UTF-8"))
        uname = logindata["uname"]
        passwd = logindata["pass"] 
        if (uname=='ac007' and passwd=="witcher")or (uname=='ac056' and passwd=="witcher!@#"):
            token = createJWT(uname)
            apikey_d = {"APIKEY":token}
            print (apikey_d)
            return  apikey_d
        else:
            return  error_response
    except:
        return error_response

#API2: Get Self Details
@app.route("/self/details/<uid>",methods=["GET","POST"])
def get_self_details(uid):
    try:
        uAPIKEY = request.headers.get("APIKEY")
        authRes = validateLogon(uAPIKEY)
        if authRes != AUTHERR:
            return json.dumps(user_data[uid])
        else:
            return error_response
    except:
        return error_response

#API3: Get Other Witcher Details 
@app.route("/witcher/list/" , methods=["GET","POST"])
def get_user_details():
    #Get API KEY from the header 
    try:
        uAPIKEY = request.headers.get("APIKEY")
        res_data = dict()
        authRes = validateLogon(uAPIKEY)

        if authRes != AUTHERR:
            for key in user_data:
                userdata = user_data[key]
                res_data.update({key:userdata['Name']}) 
            return (res_data)
        else:    
            return error_response
    except:
        return error_response
    
   
#API4: Self Register New User Subjected to Approval 
@app.route("/selfregister/details",methods=["GET","POST"])
def self_register():
    try:
        #get user details from header 
        user_reg_data = json.loads(str(request.data,"UTF-8"))
        username = user_reg_data['uname']
        attack=0
        alist =['<','>','%','alert','<script']
        for elem in alist:
            if elem in username:
                attack=1
                break
            else:
                attack=0

        if attack==1:
            return  SELREGFLAG
        else:
            return success_response
    except:
        return error_response

#API5 :  Admin lists all data 
@app.route("/admin/hidden/v3" , methods=["GET","POST"])
def get_user_details_admin():
    #Get API KEY froms the header 
    try:
        uAPIKEY = request.headers.get("APIKEY")
        dtoken= validateAdmin(uAPIKEY)
        dtoken_str = str(dtoken)
        if 'admin' in dtoken_str:
            return ADMINFLAG
        else:    
            return '{"error","Unauthorized Access"}'
    except:
        return '{"Error","Something Went Wrong"}'

#API6 :  Admin lists all data 
@app.route("/admin/v1" , methods=["GET","POST"])
def get_user_details_admin_old():
    return  APIVERFLAG

#API7: Add Credit - New Version 
@app.route("/witcher/addcredit/v3", methods=["GET","POST"])
def addCredit():
    return '{"Error":"No card added"}'

#API8: AddCredit - Old Version 
@app.route("/witcher/addcredit/v1", methods=["GET","POST"])
def addCreditNew():
    return  APIVERFLAG


if __name__ == "__main__":
    app.run(port=8080)