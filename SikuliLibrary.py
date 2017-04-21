#-*- coding:utf-8 -*-
import jpype
import os

JAVA_HOME = os.environ.get("JAVA_HOME")
SIKULI_JAR = 'C:\\Users\\raychang\\Desktop\\sikuli\\sikulix.jar'

def StartJvm(java_home = JAVA_HOME, sikuli_jar = SIKULI_JAR):
    jpype.startJVM("%s/jre/bin/client/jvm.dll" % java_home, "-ea","-Djava.class.path=%s" % sikuli_jar)
    
    App = jpype.JClass('org.sikuli.script.App')  
    Screen = jpype.JClass('org.sikuli.script.Screen')


def ShutdownJvm():
    jpype.shutdownJVM()  