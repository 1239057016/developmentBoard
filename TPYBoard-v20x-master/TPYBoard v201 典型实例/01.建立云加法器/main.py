import pyb
from pyb import UART
from pyb import Pin
from ubinascii import hexlify
from ubinascii import *

ulan = UART(6, 9600)#�����������ڵĴ���
K=1
jia=0
jie1=0
he=0
js=0#���üĴ����
#*******************************������**********************************
print('while')
while (K>0):
    _dataRead=ulan.readall()#��ȡ�ͻ�������
    if _dataRead!=None:#�жϿͻ����Ƿ�������
        print(_dataRead)
        js=js+1#�����ж�ִ�������־
        if(js==1):
            jia=_dataRead.decode('utf-8')#����ת��
            jia=int(jia)#����ת��
            print(jia)
        if(js==2):
            jia1=_dataRead.decode('utf-8')
            jia1=int(jia1)
            print(jia1)
        if(js==2):
            he=jia+jia1
            js=0
            ulan.write(str(jia)+'+'+str(jia1)+'='+str(he)+'\r\n')#���������ظ��ͻ���