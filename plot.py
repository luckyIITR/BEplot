import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go

df = pd.read_excel("periodic.xlsx")

ap = []
for e in df.index:
    if df.loc[e, 'Z'] % 2 == 0 and df.loc[e, "A"] % 2 == 0:
        ap.append(-33.5)
    elif df.loc[e, 'Z'] % 2 == 1 and df.loc[e, "A"] % 2 == 1:
        ap.append(33.5)
    else:
        ap.append(0)

ap = np.array(ap)

A = df['A'].values
Z = df['Z'].values

# len(A)
# len(Z)

B1 = 15.5 * A
B2 = 15.5 * A - 16.8 * A ** (2 / 3)
B3 = 15.5 * A - 16.8 * A ** (2 / 3) - 0.72 * Z * (Z - 1) / A ** (1 / 3)
B4 = 15.5 * A - 16.8 * A ** (2 / 3) - 0.72 * Z * (Z - 1) / A ** (1 / 3) - (23 * (A - 2 * Z) ** 2) / A
B5 = 15.5 * A - 16.8 * A ** (2 / 3) - 0.72 * Z * (Z - 1) / A ** (1 / 3) - (23 * (A - 2 * Z) ** 2) / A + ap * A ** (
        -3 / 4)

fig = go.Figure()
fig.add_trace(go.Scatter(x=A, y=B1 / A,
                         mode='lines',
                         name='B/A v'
                         ))
fig.add_trace(go.Scatter(x=A, y=B2 / A,
                         mode='lines',
                         name='B/A v+s'))
fig.add_trace(go.Scatter(x=A, y=B3 / A,
                         mode='lines',
                         name='B/A v+s+c'))
fig.add_trace(go.Scatter(x=A, y=B4 / A,
                         mode='lines',
                         name='B/A v+s+c+a'))
fig.add_trace(go.Scatter(x=A, y=B5 / A,
                         mode='lines',
                         name='B/A v+s+c+a+p'))
fig.update_layout(title='PLOT BE/A vs A',
                  title_font_size=30,
                  xaxis_title='A',
                  yaxis_title='BE/A')
plot(fig)
