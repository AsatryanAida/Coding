import logging
import re

logger = logging.getLogger('logger')
from1=open('E:\mail_logs\domain2.txt','a' ,encoding='utf-8')
with open('E:\mail_logs\mail.log', 'r') as file:
    for line in file:
        #try:
        #    if line in "roztec.ru":
        #        print(line)
        #except UnicodeDecodeError:
        #    continue
        reg = re.search(r'(?<=From:\s\<).+?(?=\>)', line)
        try:
            if type(reg)==re.Match:
                write =reg.group(0)+'\n'
                from1.write(write)
        except UnicodeDecodeError as e:
            logger.error(" error")
        # else:
        #     pass
from1.close()
print('Все сделано')


