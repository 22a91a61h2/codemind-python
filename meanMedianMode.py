# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:40:20 2023

@author: Johnwesly
"""

import pandas as pd
d = pd.DataFrame({'player':['A','B','C','D','E'],'game1':[18,28,38,48,58],'game':[12,23,43,45,56]})
print(d)
print(d.mean(numeric_only=True))