#!/usr/bin/python
# -*- coding: UTF-8 -*-
#developer: Roset scmited
#e-mail: jiaqiang_luo@hansight.com

import os
import sys


def main():
    with open('result.txt', 'w') as f2:
        with open(sys.argv[1], 'r') as f:
            for url in f:
                url = url.split()
                url[0] = 'http://' + url[0]
                result = os.popen('python struts2_hunt.py %s' % url[0])
                f2.write(result.read())
                print '[*] Site Checking:  ' + url[0]
if __name__ == '__main__':
    main()
