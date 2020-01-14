import json, requests
login_url = "http://hzkdeey.gnway.cc:9080/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
query_url = "http://hzkdeey.gnway.cc:9080/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"
login_data = {"acctid":"5e187e0d9366f9","username":"SPLAT01","password":"888888","lcid": 2052}
def login (): # define the login function
    login_response = requests.post (url = login_url, data = login_data)
    return login_response.cookies # return cookies, so you can bring them on your next visit
post_data = {"data": json.dumps ({"FormId": "PUR_PurchaseOrder", "FieldKeys": "FBillNo", "FilterString": "FDocumentStatus = 'D'"})}
response = requests.post (url = query_url, data = post_data, cookies = login ())
print (response.text)