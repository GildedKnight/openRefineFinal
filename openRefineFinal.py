
import requests
from pprint import pprint




url = 'http://127.0.0.1:3333/'                                          #url on the local
createProject = 'command/core/create-project-from-upload'               #Create project:command:POST '/command/core/create-project-from-upload'
getModel = 'command/core/get-models?'                                   #Get project models:GET '/command/core/get-models?'
applyOp = 'command/core/apply-operations?'
expRow = 'command/core/export-rows'
delProject = 'command/core/delete-project'
projectStatus = 'command/core/get-processes'
metaDataInfo = 'command/core/get-all-project-metadata'
files = {'file': (open('/home/musadiq/Downloads/drugList-csv.csv'))}              #Path for the file you want to upload 

#POST call to upload the document 
response = requests.post(url+createProject, data={                      #Multipath/form data
   'project-file' : 'inode/x-empty',                                    #MIME type of the file you want to upload
   'project-name' : 'project',                                          #Name of the project
   'format' : 'text/line-based/*sv'                                     #Format of the file that is to uploaded
   }, files=files)
res = response.url
print("POST request link for project creation: ",res)
print(response.status_code)
# print(type(res))
# print(len(res))



#Extracting the project_id from the response url
projectID = res[38:]
print("Project ID: ",projectID)

pprint("--------------------------------------------------------------------------------")




pprint("GET call")
pprint("GET Request JSON Data")

#GET Model 
# payload = {'project' : 'projectID'}
response = requests.get(url+getModel+'project='+projectID)
data = response.json()
link = response.url
pprint(data)
pprint("Response Link for GET Request")
print("GET Response link: ",link)

resp = response.status_code
print(resp)





#Apply operations
#Command: POST /command/core/apply-operations?
#POST call
file = open('/home/musadiq/Desktop/envs/refineAPI/filterx.json').read()
# jj = open(filterx.json).read()
# jj = """[
#   {
#     "op": "core/text-transform",
#     "description": "Text transform on cells in column genericName using expression value.replace(/Olodaterol/i,\"this is refined\")",
#     "engineConfig": {
#       "facets": [],
#       "mode": "record-based"
#     },
#     "columnName": "genericName",
#     "expression": "value.replace(/Olodaterol/i,\"this is refined\")",
#     "onError": "keep-original",
#     "repeat": false,
#     "repeatCount": 10
#   }
# ]"""
PARAM = {'project' : projectID,
        'operations' : file}
response = requests.post(url+applyOp,data=PARAM)
print(response.status_code)
respn = response.url
# print("POST request link for project creation: ",res)
# print(type(res))
# print(len(res))

print(respn)
print(response.json())




#Exporting ROWS

data = {'project' : projectID,
  'engine' : '{"facets":[text],"mode":"row-based"}',
  'format' : 'html'}

#Command: POST /command/core/export-rows

response = requests.post(url+expRow, data=data)
print(response.status_code)
print(response.text)





#Delete the Project
#Command: POST /command/core/delete-project
data= {'project' : projectID}

response = requests.post(url+delProject,data=data)
print(response.url)
code = response.status_code
if code == 200:
    print("Successfully Deleted The Project ")




#Get all projects metadata:
#Command: GET /command/core/get-all-project-metadata

response= requests.get(url+metaDataInfo)
print(response.status_code)
pprint(response.json())


