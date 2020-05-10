# PY_OM
python自动化运维

## 虚拟环境创建

virtualenv模块安装

```
python3.7 -m pip install virtualenv
```

在项目目录下创建虚拟环境

```
项目目录
[root@master scripts]# pwd
/workdir/python/PY_OM/base_op/sys_op/scripts
[root@master scripts]# ls
sys_info_get.py
[root@master scripts]# python3.7 -m  virtualenv --no-site-packages venv -i https://pypi.douban.com/simple
[root@master scripts]# python3.7 -m virtualenv venv
```

启动

```
[root@master scripts]# source venv/bin/activate
(venv) [root@master scripts]#
```

退出虚拟环境

```
(venv) [root@master scripts]# deactivate
```

