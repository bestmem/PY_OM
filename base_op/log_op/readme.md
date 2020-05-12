# 日志模块的使用

python自带模块logging

日志级别（由低到高）

```python
debug
info
warning
error
critical
```

简单使用

```python
$ cat log.py
import logging
logging.debug('debug message')
logging.info('debug message')
logging.warning('debug message')
logging.error('debug message')
logging.critical('debug message')
$ python log.py
WARNING:root:debug message
ERROR:root:debug message
CRITICAL:root:debug message
```

将日志记录在文件中，日志记录方式为追加

```
import logging
logging.basicConfig(filename='./1.log')
```



## 配置日志需要记录的信息

配置日志记录信息主要通过修改logging.basicConfig()的参数来实现。

参数如下：

- filename：用指定的文件名创建FiledHandler，这样日志就会保存在该文件中
- filemode：文件的打开方式，默认为a，也可指定为w
- level：设置rootlogger的日志级别
- datefmt：指定日志时间格式
- stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr，sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
- format：指定handler使用的日志显示格式
  - %(name)s	Logger的名字
  - %(levelno)s：打印日志级别的数值。
  - %(levelname)s：打印日志级别的名称。
  - %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]。
  - %(filename)s：打印当前执行程序名。
  - %(funcName)s：打印日志的当前函数。
  - %(lineno)d：打印日志的当前行号。
  - %(asctime)s：打印日志的时间。
  - %(thread)d：打印线程ID。
  - %(threadName)s：打印线程名称。
  - %(process)d：打印进程ID。
  - %(processName)s：打印线程名称。
  - %(module)s：打印模块名称。
  - %(message)s：打印日志信息。

```python
#/usr/bin/python
#coding:utf8
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')	#log格式设置
logger = logging.getLogger(__name__)

logger.info('info message')
logger.debug('debug message')
logger.critical('critical message')
```



上面使用`logging.basicConfig()`的方式已经可以处理简单的日志记录，但是还不足以是我们了解logging模块的结构和强大，下面介绍几个组成logging模块的关键方法。

+ logger：记录器，应用程序代码能直接使用的接口
+ handler：处理器，将（记录器产生的）日志记录发送到合适的目的地
+ filter：过滤器，提供了更好的粒度控制，可以决定输出哪些日志记录
+ formatter：格式化器，指明了最终输出中日志记录的布局

```python
#/usr/bin/python
#coding:utf8
import logging
logger = logging.getLogger(__name__)    #设置记录器
logger.setLevel(level=logging.WARN)     #设置日志输出级别
handler = logging.FileHandler('./output.log')    #配置处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   #配置格式化器
handler.setFormatter(formatter) #为处理器设置格式
logger.addHandler(handler)  # 为记录器配置对应的处理器

logger.info('info message')
logger.debug('debug message')
logger.critical('critical message')
```

由上述代码可以看到logger日志的记录过程：

1. 获取logger

   ```python
   logger = logging.getLogger(__name__)
   ```

2. 配置logger

   ```python
   logger.setLevel(logging.INFO)	#配置日志记录级别
   logger.addHandler(handler)	#添加日志输出位置
   # handler是我们自己定义的handler，可以为不同的名称，也可以定义多个handler，如ch=logging.StreamHandler 指将日志输出到终端。logger可以添加多个handler，用来将日志同时输出到不同的地方。
   handler.setFormatter(formatter)	#formatter是我们自己定义的，不同的handler可以配置不同的formatter，可以实现不同的输出格式
   ```

3. 在应用程序中记录日志

   ```python
   logger.info('info message')
   logger.debug('debug message')
   logger.critical('critical message')
   ```

   

