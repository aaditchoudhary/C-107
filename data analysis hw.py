import pandas as pd
import plotly.express as px
import math
import csv
import plotly.graph_objects as go
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\data visualisation.csv")
student_df=df.loc[df['student_id']=='TRL_mda']
a=student_df.groupby("level")["attempt"].mean()
as_index=False
print(a)
fig=go.Figure(go.Scatter(x=a,y=['level1','level2','level3','level4'],orientation='h',color='attempt'))
fig.show()