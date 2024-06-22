import psutil
import sys

procesos = psutil.process_iter(attrs=['name'])
procesos_edge = [p for p in procesos if p.info['name'] == 'msedge.exe']

print(len(procesos_edge))