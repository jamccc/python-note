#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = 1.78
weight = 60
bmi = weight / (height*height) 
if bmi >32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')