import pyb
from pyb import UART
from pyb import Pin
from ubinascii import hexlify
from ubinascii import *
from dht11 import DHT11#������ʪ�ȴ������Ŀ�

ulan = UART(6, 115200)#���崮�ڣ��ҵ�����������115200�Ĳ�����
K=1
#*******************************������**********************************
print('while')
while (K>0):
    #init DHT11 
    dht=DHT11('X8')
    data_=dht.read_data()#��ȡ��ʪ�ȵ�ֵ
    temp=str(data_[0])#�¶�
    hum=str(data_[1])#ʪ��
    print('temp:'+temp)
    print('hum:'+hum)
    ulan.write('temperature is:'+temp+'\r\n')#�ϴ��¶�
    pyb.delay(2000)#����ʱ��Ϊ���ø�ģ�������һ����Ӧʱ��
    ulan.write('wet is:'+hum+'%'+'\r\n')#�ϴ�ʪ��
    pyb.delay(12000)