#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# r'' 不转义
print(r'不转义 no trans ,,.."""""')

# ''' pre 
print('''
        my
      format
        pre
''')
#  格式化
PI = 3.1415

str1 = "hello world"
str2 = 'Hi %s, do you have $%d' % ('weibin', 1000)
str3 = 'hello {0} and {1:.2f}'.format('xiao ming', 12.345)
str4 = f'Pi = {PI} about {PI:.2f}'