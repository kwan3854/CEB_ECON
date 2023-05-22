import requests

payload = {"username":"carlosedubarreto@gmail.com",
           "password": "T5eD&VU$3pC8",
           
           }

# r = requests.post("https://download.is.tue.mpg.de/download.php?domain=smpl&sfile=SMPL_python_v.1.0.0.zip&resume=1", data=payload)
r = requests.post("https://download.is.tue.mpg.de/download.php?domain=smplify&sfile=mpips_smplify_public_v2.zip&resume=1",data=payload)
print('status',r.status_code)
if r.status_code == 200:
    # with open("SMPL_python_v.1.0.0.zip","wb") as f:
    with open("mpips_smplify_public_v2.zip","wb") as f:
        f.write(r.content)