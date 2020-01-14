import requests
import json

api_ep_auth = "http://hzkdeey.gnway.cc:9080/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
api_ep_query = "http://hzkdeey.gnway.cc:9080/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"
acctID = "5e187e0d9366f9"
username = "SPLAT01"
password = "888888"
lcid = 1033

pl_auth = {"acctID" : acctID, "username" : username, "password" : password, "lcid": lcid}

def login ():
    rq_auth = requests.post(api_ep_auth, data=pl_auth)
    rp_auth = rq_auth.json()
    if rp_auth['LoginResultType'] == 1:
        print("Login succesfull...")
        return rq_auth.cookies
    else:
        print("Connection error:")
        print("")
        print(rp_auth)

post_data = {"Data": {"FormId": "PUR_PurchaseOrder", "FieldKeys": "FBillNo", "FilterString": "FDocumentStatus = 'D'"}}
#data = {"FormID" : "SAL_RETURNNOTICE", "FieldKeys": "Name", "FilterString":"", "OrderString":"", "TopRowCount":"", "StartRow":"", "Limit":""}

rq_test = requests.post(api_ep_query, data=post_data, cookies=login())
# rp_test = rq_test.json()

print(rq_test.text)


print("Code running complete!")

