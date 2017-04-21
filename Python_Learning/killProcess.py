#-*- coding:utf-8 -*-
import os,time

def kill_process(process_name):
      time.sleep(1)
      cmd = 'taskkill /f /im %s' % process_name
      print cmd
      os.system(cmd)

if __name__ == '__main__':
    kill_process('IEDriverServer.exe')