#https://github.com/chwang12341/Data-Visualization/blob/master/Plotly/1/Plotly1.md
#api: xaZxcK54SYgv9yAK0hXT

import plotly.express as px
import pandas as pd

# 建立數據
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 15, 7, 12, 18]
}
df = pd.DataFrame(data)

# 繪製折線圖
fig = px.line(df, x='X', y='Y', title='簡單的折線圖')
fig.show()
