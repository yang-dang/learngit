#coding=utf-8
#����reģ��
import re
 
# ��������ʽ�����Pattern����ע��helloǰ���r����˼�ǡ�ԭ���ַ�����
pattern = re.compile(r'hello')
 
# ʹ��re.matchƥ���ı������ƥ�������޷�ƥ��ʱ������None
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')
 
#���1ƥ��ɹ�
if result1:
    # ʹ��Match��÷�����Ϣ
    print result1.group()
else:
    print '1ƥ��ʧ�ܣ�'
 
 
#���2ƥ��ɹ�
if result2:
    # ʹ��Match��÷�����Ϣ
    print result2.group()
else:
    print '2ƥ��ʧ�ܣ�'
 
 
#���3ƥ��ɹ�
if result3:
    # ʹ��Match��÷�����Ϣ
    print result3.group()
else:
    print '3ƥ��ʧ�ܣ�'
 
#���4ƥ��ɹ�
if result4:
    # ʹ��Match��÷�����Ϣ
    print result4.group()
else:
    print '4ƥ��ʧ�ܣ�'