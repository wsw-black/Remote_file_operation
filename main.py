import paramiko


# # 实例化SSHClient
# ssh_client = paramiko.SSHClient()
# # 自动添加策略，保存服务器的主机和密钥信息，如果不添加，那么不在本地know_hosts文件中记录的主机无法连接，此方法必须放在connect方法前面
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 链接主机
# ssh_client.connect(hostname="10.4.66.70", port=22, username='root', password='hbhl9500$')
# # 打开一个channel(通信)并执行命令, 结果放到stdout中，如果有错误将放到stderr中
# stdin, stdout, stderr = ssh_client.exec_command('df')
# # 输出返回信息
# stdout_info = stdout.read().decode('utf-8')
# print(stdout_info)
# # 输出返回错误信息
# stderr_info = stderr.read().decode('utf-8')
# print(stderr_info)
# ssh_client.close()
# 登录参数
hostname = '10.4.66.70'
host_port = 22
username = 'root'
password = 'hbhl9500$'

def target_info():
    '''获取需要强关的文件路径和名称'''
    file_info = input("请输入需要强关文件的路径:").strip()

def ssh_client_con():
    """ 创建ssh并建立链接"""
    ssh_client = paramiko.SSHClient()  # 1.实例化对象
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 2.连接服务器
    ssh_client.connect(hostname=hostname, port=host_port, username=username, password=password)
    # 3.执行命令
    # shell指令
    shell_command = 'df'
    stdin, stdout, stderr = ssh_client.exec_command(shell_command)
    # 4. 打印结果
    stdout_info = stdout.read().decode('utf-8')
    print(stdout_info)
    stderr_info = stderr.read().decode('utf-8')
    print(stderr_info)
    ssh_client.close()


def sftp_client_con():
    # 1. 创建transport 通道
    tran = paramiko.Transport((hostname, host_port))
    tran.connect(username=username, password=password)
    # 2. 创建sftp实例化
    sftp = paramiko.SFTPClient.from_transport(tran)
    # 3. 执行上传功能
    local_path = 'E:\\test.txt'    # 本地路径
    remote_path = '/srv/dev-rbd0/技术部/王世伟/test.txt'    # 远程路径
    # put_info = sftp.put(local_path, remote_path, confirm=True)
    # print(put_info)
    # print('上传%s完成'%local_path)
    sftp.remove(remote_path)
    print('%s已删除'%remote_path)
    # 关闭通道
    tran.close()



target_info()
# ssh_client_con()
sftp_client_con()