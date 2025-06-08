"""
网络：
1. 网络编程三要素：Ip、端口、协议；

2. 通信协议：一组用于规定不同设备或者计算机之间如何进行数据交换和通信的规则和约定；
           通信内容包括：数据格式、传输的顺序、错误检查机制、如何处理不同情况等；

3. TCP/IP: 互联网的数据传输和网络通信，用于不同计算机之间的传输和路由，主要有两个核心协议：
    TCP(传输控制协议) 和 IP(网际协议)；

4. 分层网络模型：
    OSI七层网络模型：
        应用层、表示层、会话层、传输层、网络层、数据链路层、物理层

    TCP/IP模型：
          四层：应用层、传输层、网络层、网络接口层
          五层：应用层、传输层、网络层、数据链路层、物理层
5. 常见的网络协议
    应用层：HTTP、FTP、SMTP、NTP、DNS、SSH
    传输层：TCP UDP SCTP
    网络层：IP ICMP IGRP ARP RARP
    数据链路层：以太网 帧中继 IEEE 802.11 PPP
    物理层： 调制解调器、无线电、光纤

6. IP: 是一串数字组成，用来标识一台电脑在网络；
      Linux： ifconfig 或 ip addr查看IP;
      windows： ipconfig
7. 子网掩码（或者CIDR）：用来划分和管理IP地址的工具，他们和IP地址的关系就像邮政编码和家庭地址的关系
                      表示方法：ip + 子网掩码：192.168.1.10 + 255.255.255.0
                               ip/CIDR: 192.168.1.10/24 其中24代表24个1，即255.255.255.0的二级制表示方法
8. IPV4 IPV6
    IPV4 : A类： 大量主机的大型网络，互联网使用；
           C类： 小型局域网，内网使用；
           表示：四组十进制，以逗号分割，eg: 192.168.1.10，最大可表示42亿个地址，在2011年已用尽
    IPV6: 表示：以八组十六进制数组成， eg: 2001:db8:0:1234:0:567:8:1 ,最高表示3.402823669×10 ^ 38, 基本上可以让地球上的沙子也拥有ip地址；

9. 端口： 用户不同设备之间的通信 ，netstat -ano
         公认端口：1-1023
         动态端口：1024 - 65536
         常见端口：22 - ssh
                 21 - FTP文件传输协议
                 23 - Telnet终端仿真协议
10. socket（套接字）： 同一或者不同电脑的进程间通信的一个工具，进程之间想要进行网络通信需要基于socket。只要与网络相关的应用程序
             或者软件都使用到了socket；
11. UDP: 用户数据报协议（User Datagram Protocol)），面向数据报的通信协议；
         不可靠传递，不会做备份，也不会做错误检查和纠正的开销；
         使用场景：低延迟的流媒体、在线游戏流量；
12. TCP: 传输控制协议（Transmission Control Protocol）,面向连接的，可靠的，基于字节流的传输层通信协议；
         运行分为三个阶段：连接建立、数据传送和连接终止；
13 HTTP: 超文本传输协议 ，是一种用户分布式、协作式和超媒体信息系统的应用层协议，是万维网的数据通信基础；
         客户端请求内容： 请求行、请求头、空行和请求体；
         服务端响应消息： 状态行、 消息报头、空行和响应正文；
         请求方法(8种)：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT





"""
#socket 模块用户用于创建套接字
import socket

import starlette
import uvicorn

#TCP : SOCK_STREAM 流式套接字； AF_INET:用于internet 进程间通信
tcp_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

#UDP : SOCK_DGRAM 数据报套接字； AF_INET:用于internet 进程间通信
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

###======================Starlette 构建web接口================================
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import requests
import uvicorn

# 一言网API 地址
HITOKOTO_URL = 'https://v1.hitokoto.cn/'

# 定义一步函数来获取随机名言
async def get_hitokoto():
    try:
        params ={
            'c': 'a',
            'encode':'json'
        }
        response = requests.get(HITOKOTO_URL, params=params)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            hitokoto = data['hitokoto']
            from_who = data['from_who'] if data['from_who'] else '未知'
            return{'hitokoto': hitokoto, 'from_who': from_who}
        else:
            return{'error':f'请求一言网API失败，状态码：{status_code}'}
    except requests.RequestException as e:
        return {'error':f'请求过程中出现错误：{str(e)}'}
# 定义处理跟路径请求的异步函数
async def homepage(request):
    result = await get_hitokoto()
    return JSONResponse(result)
# 创建Starlette 应用实例
app = Starlette(debug=True ,routes=[Route('/', homepage),])

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)
