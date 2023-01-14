import pandas as pd
import plotly.express as px


df = pd.read_json('db.json')
fig = px.pie(df, values='Red Meat')
fig.show()

