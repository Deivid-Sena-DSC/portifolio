import pandas as pd    
import plotly.express as px  


df = pd.read_excel('Excel\Vendas Consolidado.xlsx')

df['Valor Unitario'] = df['Valor Unitario'].astype('float')
df['Faturamento'] = df['Faturamento'].astype('float')
df['Lucro'] = df['Lucro'].astype('float')
df.drop_duplicates()
df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], axis=0, inplace=True)

df.loc[df['Estado'] == 'São Paulo', 'Latitude'] = -23.552462054210736
df.loc[df['Estado'] == 'São Paulo', 'Longitude'] = -46.624225038563836
df.loc[df['Estado'] == 'Tocantins', 'Latitude'] = -10.773729188270558
df.loc[df['Estado'] == 'Tocantins', 'Longitude'] = -48.55232717983442
df.loc[df['Estado'] == 'Goiás', 'Latitude'] = -15.395212888088595
df.loc[df['Estado'] == 'Goiás', 'Longitude'] = -50.15633109881238
df.loc[df['Estado'] == 'Mato Grosso', 'Latitude'] = -12.89986320910692
df.loc[df['Estado'] == 'Mato Grosso', 'Longitude'] = -55.65159660341818

dff = df.groupby(['Estado','Latitude','Longitude'])['Faturamento'].sum().reset_index()

def graf_mapa(dataframe, latitude, longitude, bolha, cores):
    df = dataframe.groupby([cores, latitude,longitude])[bolha].sum().reset_index()
    fig = px.scatter_map(df, lat=latitude, lon=longitude, size=bolha, color=cores, zoom=4, map_style='open-street-map')
    return fig

df.to_excel('Vendas Consolidados.xlsx')