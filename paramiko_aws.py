# aws lightsail instance 끼리의 paramiko 사용을 하기 위해서는
# 개인적 경험으로는 인스턴스 SSH 설정 시 개인키로 설정하지 말고,
# 기본키로 설정해서 LightsailDefaultKey-ap-northeast-2.pem 를
# 이용하면 성공가능성이 높은 듯 합니다.
# 다만, 관련된 각종 보안문제는 개인의 책임이겠지요.

import paramiko
 
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
cli.connect('IP or 호스트명', username='사용자명', password='있으면 넣고 없으면 none', key_filename='/경로/LightsailDefaultKey-ap-northeast-2.pem')
stdin, stdout, stderr = cli.exec_command("ls -la")
lines = stdout.readlines()
print(''.join(lines))
 
cli.close()