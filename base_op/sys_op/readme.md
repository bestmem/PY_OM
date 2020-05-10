# 系统信息采集

使用模块：psutil

psutil是一个跨平台的系统信息采集第三方模块，能过获取系统CPU、内存、磁盘、网络、进程等信息。常用于系统监控，可以实现类似于以下的命令的功能：ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。支持linux/unix/osx/windows等平台

**模块安装**

```
(venv) [root@master scripts]# python -m pip install psutil
```

CPU监测

```python
In [2]: psutil.cpu_times()	      获取CPU（逻辑CPU）占用时间的详细信息
In [6]: psutil.cpu_times(percpu=True)	获取每个CPU占用时间的详细信息
In [4]: psutil.cpu_count() 	获取CPU逻辑数
In [7]: psutil.cpu_count(logical=False)	获取CPU物理数
In [8]: psutil.cpu_percent()	CPU占比
psutil.cpu_percent(percpu=True)	每个CPU占比
```

内存监测

```python
In [10]: psutil.virtual_memory()
```

磁盘监测

```python
In [13]: psutil.disk_partitions() 	查看磁盘分区、挂载、挂载类型等
In [14]: psutil.disk_usage('/')  	查看磁盘使用率

```

网络监测

```python
In [15]: psutil.net_io_counters()   获取网络读取字节/包的个数
In [16]: psutil.net_if_addrs() 	获取网络接口信息
In [17]: psutil.net_if_stats()  获取网络接口状态
In [18]: psutil.net_connections() 	获取网络当前连接信息
```

进程监测

```python
In [21]: for pid in psutil.pids(): 	获取所有进程pid
    ...:     print(pid) 
    
In [21]: for proc in psutil.process_iter(attrs=['pid', 'name', 'username']): 
    ...:     if proc.info['name'].startswith('nginx'): 	查找nginx相关进程
    ...:         print(proc.info) 

```

> psutil.process_iter()返回的是一个进程相关信息的可迭代对象，每个元素使用info属性可以获取一个存放进程详细信息的字典（CPU占用、线程数、内存占用）

还可以使用如下方式查看某进程的占用资源信息

```python
In [3]: psutil.Process(1).cpu_times()	获取pid为1的进程cpu占用时间
In [4]: psutil.Process(1).memory_info()	获取pid为1的进程内存占用情况，rss为实际占用内存
In [5]: psutil.Process(1).num_threads()	获取pid为1的进程线程数
In [6]: psutil.Process(1).memory_percent()	获取pid为1的进程使用内存占比
```