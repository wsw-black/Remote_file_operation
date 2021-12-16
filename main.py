import paramiko
import os
import time


# 登录参数
hostname = '10.4.66.70'
host_port = 22
username = 'root'
password = 'hbhl9500$'


def target_info():
    '''获取需要强关的文件路径和名称'''
    global file_info, file_name
    file_info = input("请输入需要强关文件的路径:").strip()
    file_name = input("请输入文件名:").strip()


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
    local_path = r'D:/test/'+ file_name   # 本地路径
    # remote_path = '/srv/dev-rbd0/技术部/王世伟/test.txt'    # 远程路径
    # 下载共享上的文件到本地
    font_path = r'/srv/dev-rbd0'
    remote_path = font_path + file_info
    print(remote_path)
    sftp.get(remote_path, local_path)
    print('下载%s完成'%remote_path)
    # 删除共享上的文件
    time.sleep(5)
    sftp.remove(remote_path)
    print("%s文件删除成功"%remote_path)
    # 重新上传文件到服务器
    put_info = sftp.put(local_path, remote_path, confirm=True)
    print("%s上传成功"%local_path)
    # 关闭通道
    tran.close()


target_info()
# ssh_client_con()
sftp_client_con()