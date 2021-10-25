#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question:
    For household 04, at a certain time on New Year's Day, which particular 
    plug/appliance consumes most power?

@author: Runze Yin
"""

import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

li = []

for i in range(1,9):
    filename =  "04/0" + str(i) + "/2013-01-01.csv"
    print(filename)
    df = pd.read_csv(filename, names=['consumption'])
    li.append(df)
    
# 01: Fridge (no. days: 194, coverage: 97.01%)
# 02: Kitchen appliances (no. days: 194, coverage: 96.81%) (*)
# 03: Lamp (no. days: 170, coverage: 93.54%) (**)
# 04: Stereo and laptop (no. days: 169, coverage: 90.98%)
# 05: Freezer (no. days: 192, coverage: 93.08%)
# 06: Tablet (no. days: 189, coverage: 93.6%)
# 07: Entertainment (no. days: 186, coverage: 94.69%) (***)
# 08: Microwave (no. days: 194, coverage: 97.08%)

Fridge = li[0]
Fridge['appliance'] = 'Fridge'
Kitchen = li[1]
Kitchen['appliance'] = 'Kitchen appliances'
Lamp = li[2]
Lamp['appliance'] = 'Lamp'
Stereo = li[3]
Stereo['appliance'] = 'Stereo and laptop'
Freezer = li[4]
Freezer['appliance'] = 'Freezer'
Tablet = li[5]
Tablet['appliance'] = 'Tablet'
Entertainment = li[6]
Entertainment['appliance'] = 'Entertainment'
Microwave = li[7]
Microwave['appliance'] = 'Microwave'

for df in [Fridge, Kitchen, Lamp, Stereo, Freezer, Tablet, Entertainment, Microwave]:
    df.index = pd.to_datetime(df.index, unit='s', 
                              origin=pd.Timestamp(2013, 1, 1, 0)) 
    df['time'] = df.index.strftime("%M:%S")
    df['hour'] = df.index.strftime("%H")

data = pd.concat([Fridge, Kitchen, Lamp, Stereo, Freezer, Tablet, Entertainment, Microwave])
    
fig = px.line(data, 
        x="time", 
        y="consumption", 
        color="appliance",
        title="Appliances Power Consumption",
        animation_group="appliance",
        animation_frame="hour")

fig.write_html("plotly.html")













