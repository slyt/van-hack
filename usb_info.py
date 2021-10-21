import subprocess, json

out = subprocess.getoutput("PowerShell -Command \"& {Get-PnpDevice | Select-Object Status,Class,FriendlyName,InstanceId | ConvertTo-Json}\"")
j = json.loads(out)
for dev in j:
    print(dev['Status'], dev['Class'], dev['FriendlyName'], dev['InstanceId'] )