import json
import pandas as pd

tmp1='[\
    {\
        "id":1000,\
        "UP_TIME":0,\
        "POWER":948,\
        "TEMP":250\
    },\
    {\
        "id":1000,\
        "UP_TIME":1,\
        "POWER":945,\
        "TEMP":251,\
        "ERR_CD":1\
    }\
]'

tmp2='[\
    {\
        "id":1000,\
        "UP_TIME":0,\
        "POWER":949,\
        "TEMP":250\
    },\
    {\
        "id":1000,\
        "UP_TIME":1,\
        "POWER":945,\
        "TEMP":251,\
        "ERR_CD":1\
    }\
]'

df1=pd.read_json(tmp1)
df2=pd.read_json(tmp2)
df3=(df1==df2)

print(df1==df2)

print("\n", df1[(df1 == df2).all(axis=1) == False])

print("\n",df3)