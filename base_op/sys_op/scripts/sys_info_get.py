#!/usr/bin/env python3.7
#coding: utf8
import psutil
import os
# 按名称查找进程相关信息
def find_procs_by_name(name):
	ls = []
	for proc in psutil.process_iter(attrs=['name']):
		if proc.info['name'] == name:
#		if proc.info['name'].startswith(name):
			ls.append(proc)
	return ls

# 按名称查找进程相关信息
def find_procs_by_name_1(name):
	ls = []
	for proc in psutil.process_iter(attrs=['name', 'exe', 'cmdline']):
		if proc.info['name'] == name or \
			proc.info['exe'] and os.path.basename(proc.info['exe']) == name or \
			proc.info['cmdline'] and proc.info['cmdline'][0] == name:
			ls.append(proc)
	return ls

# 杀掉进程树

#print(find_procs_by_name('nginx'))
print(find_procs_by_name_1('nginx'))
