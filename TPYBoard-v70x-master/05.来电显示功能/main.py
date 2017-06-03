import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from ubinascii import hexlify
from ubinascii import *#��������Ϊ������ʹ�õ����


leds = [pyb.LED(i) for i in range(1,5)]
P,L,SHUCHU=0,0,0
SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
#DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
#CLK =>SPI(1).SCK  'X6' SPI clock
RST    = pyb.Pin('X20')
CE     = pyb.Pin('X19')
DC     = pyb.Pin('X18')
LIGHT  = pyb.Pin('X17')
lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)#��������Ϊ��������ʼ����ʾ��
count_=0
N2 = Pin('Y3', Pin.OUT_PP)#���塰Y3��Ϊ���ģʽ����������ǿ��Ʒ������ģ����绰����Ҫ�����
N1 = Pin('Y6', Pin.OUT_PP)#���塰Y6��λ���ģʽ����Y6�������ǰ���ͨ��ϵͳ�Ŀ��ؿ�������
N1.low()
pyb.delay(2000)
N1.high()
pyb.delay(10000)#ͨ���������߿���������ţ�����ͨ��ϵͳ
u2 = UART(4, 115200)#���ô���4�������ô��ڲ�����Ϊ115200
i='0'
w=0
d=0
q=0
G=0
j=0
while 0<1:
    N2.low()#���÷�������������Ϊ�͵�ƽ�����÷�������
    if(u2.any()>0):#��⴮��4�Ƿ������ݣ����������ִ������
        _dataRead=u2.readall()
        if _dataRead!=None:#�жϴ���4�������Ƿ�Ϊ�գ���Ϊ��ִ�����´���
            print('ԭʼ����=',_dataRead)
            print('ԭʼ���ݳ���:',len(_dataRead))
            print('123',_dataRead[2:6])
            RING=_dataRead[2:6]#��ȡ��ͷ�������ͷ��Ϊ���ж������Ƿ���ȷ����Ҫ����
            print('111',_dataRead[18:29])
            HM=_dataRead[18:29]#���ݵ�18��29λ��������Я�����ֻ����룬���ǰ����Ǳ������
            WD='No such person'#����һ������������������ǿ��Գ�Ϊ�ǵ绰����ȱ���
            if(RING==b'RING'):#�жϰ�ͷ��ȷ��ִ���������
                if(HM==b'18654868920'):#�ж������Ƿ���һ���Ѿ��洢�ĺ���
                    WD='TPYBoard_GPS'#����ǣ���ʾ�洢����,���û�д洢��ʾ'Nosuch person'
                N2.high()#���߷������������ţ�ʹ����������
                lcd_5110.lcd_write_string('Phone Number:',0,0)
                lcd_5110.lcd_write_string(HM.decode("utf8"),2,1)
                lcd_5110.lcd_write_string('The contact:',0,2)
                lcd_5110.lcd_write_string(str(WD),0,3)#��ʾ��Ӧ��������룬�����˳�ν
        pyb.delay(1000)