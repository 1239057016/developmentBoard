import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *#����Ϊ����ʹ�õ������


leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST        = pyb.Pin('X20')
CE         = pyb.Pin('X19')
DC         = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
#����Ϊ��ʼ����ʾ���ĺ�������Ȼ���û���õ���ʾ�����Ǳ���
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
count_=0
N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)#����ͨ��ϵͳ��������
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)#�����������ţ�����ͨ��ϵͳ
u2 = UART(4, 115200)#���崮��4������ ������Ϊ115200
K=5#����һ��ѡ�����K
while (K==5):#���ѭ����Ϊ������ͨ������ģʽΪ͸��ģʽ��
    u2.write('AT+CIPMODE=1\r\n')
    pyb.delay(500)
    if(u2.any()>0):
        print('͸��')
        _dataRead=u2.readall()
        print('͸��',_dataRead.decode('utf-8'))
        if(_dataRead.find(b'OK')>-1):
            K=0
            pyb.delay(20)
#��������Ϊ�˴ͨ������
u2.write('AT+CIPSTART="TCP","139.196.109.178",30000\r\n')
pyb.delay(10000)
print('123')
#������Ϊ���ж�ͨ�������Ƿ��Ѿ��������������û�н�������ͨ�ŵ����ӣ���ȴ���
while (K==0):
    pyb.delay(3000)
    if(u2.any()>0):
        _dataRead=u2.readall()
        print('oo',_dataRead)
        #����ж���Ϊ���ж��Ƿ��Ѿ��ͷ�����������������
        if(_dataRead.find(b'CONNECT OK')>-1):
            #�������Ѿ��ͷ���������������������ı�ѡ�������ֵ��ʹ�������һ��ѭ��
            K=1
            pyb.LED(1).on()
#���ѭ����ִ�����ݴ��������ִ�����ڣ������ѭ���н��и������ݵĲü�ƴ�Ӻͷ��͡�
while (K==1):
    print('DOU')
    #u2.write('+++')  ��ʱ����ϵͳ����͸��ͨ��ģʽ����Ҫ�˳������͡�+++��������        #�˳���
    #u2.write('ATO0') ����ϵͳ��ָ��ģʽ����͸��ģʽ�����͡�ATO0��,�����͸����
    #pyb.delay(1500)
    pyb.LED(2).off()
    pyb.LED(3).off()
    pyb.LED(2).on()
    u2.write('TPGPS,1234567890abcde,36.67191670,119.17200000,201701120825,25,50,END')
    #���������ϸ��ʽ���շ���ƽ̨ʾ�����ĸ�ʽ��
    #�����ʽ����ľ�γ�����ݻ��ɴӶ�λϵͳ��ȡ���ľ�γ�ȣ��Ϳ���ʵʱ��λ�ˡ�
    pyb.delay(13000)#��ʱһ��ʱ�䣬�ٷ��ṩ�Ĳ���ƽ̨���ϴ�Ƶ������
    if(u2.any()>0):
#������ؽ������ڹٷ��ṩ�ķ���ƽ̨
        _dataRead=u2.readall()
        print('1212',_dataRead)
    pyb.LED(3).on()
    pyb.delay(10000)