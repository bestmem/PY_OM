# python开发ftp

FTP（File Transfer Protocol），文件传输协议，使用两个端口：数据端口20和控制端口21（默认情况下）

ftp有两种模式：主动模式和被动模式

## 主动模式

## 被动模式

## 总结

主动方式对FTP服务器的管理有利，单对客户端的管理不利。因为ftp服务器企图与客户端的高位随机端口建立连接，而这个端口很可能被客户端防火墙阻塞掉

被动方式对FTP客户端有利，但对服务端管理不利，因为客户端要与服务器端建立两个连接，其中一个连接到一个高位随即端口，而这个端口很可能被服务器端的防火墙阻塞掉



## 简单使用

安装pyftplib第三方模块

```
python -m pip install pyftpdlib -i https://pypi.douban.com/simple
```

