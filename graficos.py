import plotly.express as px
import plotly.graph_objects as go   

def graf_barra(x, y, cores, titulo):
    fig1 = px.bar(x=x, y=y, color=cores)
    fig1.update_layout(
                    title=titulo,
                    title_x=0.1,
                    title_y=0.9,
                    xaxis=dict(
                    tickmode='array',
                    tickvals=x,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    legend=dict(
                    font=dict(size=14, family='Arial Black')),
                    legend_title=None
                    )
    return fig1

def graf_barra_linha(dataframe, coluna1, coluna2, titulo):
    df = dataframe.groupby([coluna1], sort=False)[coluna2].sum().reset_index()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=df[coluna1],
        y=df[coluna2],
        name='Barras'))
    
    cores = []
    for valor in df[coluna2]:
        if valor == df[coluna2].min():
            cores.append('red')  # Cor para a menor barra
        elif valor == df[coluna2].max():
            cores.append('mediumseagreen')  # Cor para a maior barra
        else:
            cores.append('aqua')  # Cor para as barras intermediárias
    fig2.update_traces(
                    marker=dict(
                    color=cores,
                    opacity=0.8))        

    fig2.add_trace(go.Scatter(
        x=df[coluna1],
        y=df[coluna2],
        name='Linhas'))
    fig2.update_layout(
                    title=titulo,
                    title_x=0.1,
                    title_y=0.9,
                    xaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    showlegend=True)               

    return fig2


def graf_barra_count(dataframe, coluna1, coluna2, titulo):
    df = dataframe.groupby([coluna1, coluna2], sort=False)[coluna2].count().reset_index(name='Contagem')
    fig3 = px.bar(df, coluna1, 'Contagem', color=coluna2, barmode='group', title=titulo)
    fig3.update_layout(
                    title_x=0.1,
                    title_y=0.9,
                    xaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    legend=dict(
                    font=dict(size=14, family='Arial Black')),
                    legend_title=None)  
    return fig3

def graf_pie(names, values, cores, titulo):
    fig4 = px.pie(names=names, values=values, color=cores, title=titulo,)
    fig4.update_layout(
                    xaxis=dict(
                    tickmode='array',
                    tickvals=names,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    legend=dict(
                    font=dict(size=14, family='Arial Black')),
                    font=dict(size=14, family='Arial Black'),
                    legend_title=None
                    )
    return fig4

def graf_pie2(dataframe, names, values, titulo):
    fig5 = px.pie(dataframe, values=values, names=names, title=titulo)
    fig5.update_layout(
                    xaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    legend=dict(
                    font=dict(size=14, family='Arial Black')),
                    legend_title=None
                    )
    return fig5

def graf_line(x, y, titulo):
    fig6 = px.line(x=x, y=y, title=titulo, markers='o')
    fig6.update_traces(line=dict(color='green', width=2))
    fig6.update_layout(
                    xaxis=dict(
                    tickmode='array',
                    tickvals=x,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')))
    return fig6

def graf_funil(x, y):
    fig7 = px.funnel(x=x, y=y)
    fig7.update_layout(
                    xaxis=dict(
                    tickmode='array',
                    tickvals=x,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')))
    return fig7 

def graf_barra_agrupada(x, y1, y2, nome1, nome2, titulo):
    fig8 = go.Figure()
    fig8.add_trace(go.Bar(
        x=x,
        y=y1,
        name=nome1
    ))
    fig8.add_trace(go.Bar(
        x=x,
        y=y2,
        name=nome2,
        marker=dict(color='red', opacity=0.7)
    ))
    fig8.update_layout(
        barmode='group',
        title=titulo,
        xaxis_title=None,
        yaxis_title=None,
        legend_title=None,
        font=dict(size=14, family='Arial Black')
    )

    return fig8

def graf_barra_agrupada2(dataframe, coluna1, coluna2, coluna3, titulo):
    df = dataframe.groupby([coluna1, coluna3], sort=False)[coluna2].sum().reset_index()
    fig9 = px.bar(df, x=coluna1, y=coluna2, color=coluna3, barmode='group')
    fig9.update_layout(
        title=titulo,
        title_x=0.1,
        title_y=0.9,
        xaxis_title=None,
        yaxis=dict(tickformat=',', title=None, tickfont=dict(size=14, family='Arial Black')),
        font=dict(size=14, family='Arial Black'))

    return fig9


def graf_line_agrupada(x, y1, y2, nome1, nome2, titulo):
    fig10 = go.Figure()
    fig10.add_trace(go.Scatter(
        x=x,
        y=y1,
        name=nome1
    ))
    fig10.add_trace(go.Scatter(
        x=x,
        y=y2,
        name=nome2,
        marker=dict(color='red', opacity=0.7)
    ))
    fig10.update_layout(
        title=titulo,
        xaxis_title=None,
        yaxis_title=None,
        legend_title=None,
        font=dict(size=14, family='Arial Black')
    )

    return fig10

def graf_funil_agrupada(x, y1, y2, nome1, nome2):
    fig11 = go.Figure()
    fig11.add_trace(go.Funnel(
        name = nome1,
        y = x,
        x = y1,
        ))
    fig11.add_trace(go.Funnel(
        name = nome2,
        y = x,
        x = y2))
    fig11.update_layout(
                    xaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    legend=dict(font=dict(size=14, family='Arial Black')))
    return fig11

def graf_mapa(dataframe, latitude, longitude, bolha, cores):
    df = dataframe.groupby([cores, latitude, longitude])[bolha].sum().reset_index()
    fig12 = px.scatter_mapbox(df, lat=latitude, lon=longitude, size=bolha, color=cores, zoom=3, mapbox_style='open-street-map')
    return fig12      