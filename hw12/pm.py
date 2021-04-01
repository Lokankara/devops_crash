import paramiko

ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='207.244.229.74',username='testuser',password='*,<R#!$(2udw{Zgz')
ftp_client=ssh_client.open_sftp()
ftp_client.get('/opt/testuser/logfile.log','logfile.log')
ftp_client.close()
