# coding:utf-8

import socket
import sys
import os

def help_():
    "没有输入文件名字函数"
    print '----------------------------------'
    print '以下为 Python2 案例, 在同一个目录执行'
    print '请输入 Python python程序 file(文件的名字)   '
    print '----------------------------------'

def external_feil():
    "获取外部程序的参数进行返回"
    return sys.argv[1:]

def error_feil():
    "输入文件名字错误函数"
    print '----------------------------------'
    print '|      请输入正确的文件名字         |'
    print '----------------------------------'

def check_find_feil(feil):
    """查找文件是否存在"""
    list_feil = os.listdir('.')
    for li_feil in list_feil:
        if li_feil == feil:
            return True
    return False

def read_feil(client, feil):
    """将数据传送到服务器, 读取文件, 发送文件, 关闭文件, """
    fp = open(feil, 'rb')
    feil_read = fp.read()
    client.send(feil_read)
    fp.close()

def socket_feil(ip, port):
    """Python- TCP 客户端主程序, 建立 socket, """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 建立 socket
    client.connect( (ip, port) )# 绑定端口
    feil = external_feil()
    # feil = 'timg.gif'
    print '[*]:=%s' %feil
    if len(feil):# 判断是否输入文件名字
        there_are = check_find_feil(feil[0])# 查找文件
        if there_are:
            try:
                feil = feil[0]
                client.send(feil)# 将文件的名字发送过去
                ok_accept = client.recv(1024)# 接受服务器, 发送过来的, 确定码
                if ok_accept == 'ok':
                    read_feil(client, feil)# 发送数据函数
            except Exception as error:
                print '[*]:%s' %error
            finally:# 回滚执行
                successful = client.recv(1024)
                if successful == '1':
                    read_feil(client, feil)
                    print '[&]:文件回滚 ok 啦 :[&]'

                else:
                    print '[*]-文件传送完毕-[*]'
        else:
            error_feil()
    else:
        help_()

if __name__ == "__main__":
    ip = '0.0.0.0'
    port = 9999
    socket_feil(ip, port)