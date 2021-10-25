#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Question:
    For household 04, in a certain hour on New Year's Day, which particular 
    real power phase consumes most power?
    
@author: Runze Yin
"""

import altair as alt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('04_sm_csv/04/2013-01-01.csv',
                 names=['powerallphases',
                             'powerl1',
                             'powerl2',
                             'powerl3',
                             'currentneutral',
                             'currentl1',
                             'currentl2',
                             'currentl3',
                             'voltagel1',
                             'voltagel2',
                             'voltagel3',
                             'phaseanglevoltagel2l1',
                             'phaseanglevoltagel3l1',
                             'phaseanglecurrentvoltagel1',
                             'phaseanglecurrentvoltagel2',
                             'phaseanglecurrentvoltagel3'
                                            ])

df = df[['powerallphases','powerl1','powerl2','powerl3']]

df.index = pd.to_datetime(df.index, unit='s', 
                              origin=pd.Timestamp(2013, 1, 1, 0)) 
df['time'] = df.index.strftime("%M:%S")
df['hour'] = df.index.strftime("%H")

df = df.groupby(['hour']).sum()
df['hour'] = df.index

df = pd.melt(df, id_vars=['powerallphases','hour'],
        var_name='real power phase', value_name='consumption')

df.info()


highlight = alt.selection(
    type="single", on="mouseover", fields=["real power phase"], nearest=True
)
base = alt.Chart(df).encode(
    x="hour:O",
    y="consumption:Q",
)
points = (
    base.mark_circle()
    .encode(
        opacity=alt.value(0),
        tooltip=["real power phase", "hour", "consumption","powerallphases"],
    )
    .add_selection(highlight)
    .properties(width=400)
)
lines = base.mark_line().encode(
    size=alt.condition(~highlight, alt.value(1), alt.value(3)),
    color=alt.condition(highlight, "real power phase", alt.value("lightgrey"), legend=None),
)
chart = (points + lines)

chart.save('altair.html')



