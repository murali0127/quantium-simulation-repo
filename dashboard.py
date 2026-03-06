from dash import  Dash, html, dcc, Output, Input, callback
import glob
import plotly.express as px
import pandas as pd

# file = glob.glob('./task-2_formating_data_completed.csv')

#Load CSV data
df = pd.read_csv('./data/task-2_formating_data_completed.csv')

df['Date'] = pd.to_datetime(df['date'])

#Sort by date
df.sort_values('Date', inplace=True)

fig = px.line(df,
              x='Date',
              y='sales',
              title='Pink Morsels Sales Before and After Price Increase.',
              markers=True)
fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=df["sales"].max(),
    line=dict(color="red", dash="dash")
)
fig.update_layout(
      xaxis_title = 'Date',
      yaxis_title = 'Sales',
      template = 'plotly_white'
)
#Annotations
fig.add_annotation(
    x="2021-01-15",
    y=df["sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=2
)



#PIE CHART
price_change = pd.to_datetime('2021-01-15')
df['period'] = df['Date'].apply(
      lambda x : 'Before Price Increase' if x < price_change else 'After Price Increase'
)
pie_data = df.groupby('period')['sales'].sum().reset_index()

pie_fig = px.pie(
      pie_data,
      names='period',
      values='sales',
      title='Sales Distribution before and after price increase'
)
#Initialize Dash App
app = Dash(__name__)


app.layout = html.Div(className='container',
      children=[html.H1(children='Hello User'),
                html.Div(className='contianer', id='title',children='''Visualization of Pink Morsels Sales based on date.'''),
                dcc.Graph(id='total-sales',figure=fig),
                dcc.RadioItems(
                      id='region-filter',
                      options = [
                            {'label': 'North', 'value': 'north'},
                            {'label': 'East', 'value': 'east'},
                            {'label': 'South', 'value': 'south'},
                            {'label': 'West', 'value': 'west'},
                            {'label': 'All', 'value': 'all'}
                      ],
                      value = 'all',
                      inline = True
                ),
                 html.Div(className="charts", children=[
                       dcc.Graph(id="sales-chart"),
                       html.Div(
                             children=[
                                   dcc.Graph(id="sales-pie", figure=pie_fig)                                   
                             ]
                             
                       )
                  ])

                ])

@app.callback(
      Output('sales-chart', 'figure'),
      Input('region-filter', 'value')

)


def update_chart(region):
      if region == 'all':
            filtered_df = df
      else:
            df['region'] = df['region'].str.lower()
            filtered_df = df[df['region'] == region]
      fig = px.line(
            filtered_df,
            x = 'Date',
            y = 'sales',
            title='Pink morsel sales' ,
            color = 'region'
      )
      fig.add_shape(
            type="line",
            x0="2021-01-15",
            x1="2021-01-15",
            y0=0,
            y1=filtered_df["sales"].max(),
            line=dict(color="red", dash="dash")
      )

      fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Sales',
            template='plotly_white'
      ) 
      return fig


if __name__ == '__main__':
      app.run(debug=True)

