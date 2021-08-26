import paramiko
import time
 
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
cli.connect('호스트', username='사용자명', password='암호 or none', key_filename='/경로/LightsailDefaultKey-ap-northeast-2.pem')
stdin, stdout, stderr = cli.exec_command("cat /경로/list.txt")
time.sleep(2)
lines = stdout.readlines()
blogname=lines[3]
cli.close()

print("======")
print(blogname)
print("======")
#테스트