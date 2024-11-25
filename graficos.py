import plotly.express as px
import plotly.graph_objects as go   

def graf_barra(x, y, cores, titulo):
    fig = px.bar(x=x, y=y, color=cores, title=titulo)
    fig.update_layout(
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
                    font=dict(size=14, family='Arial Black'),
                    legend_title=None
                    )
    return fig

def graf_pie(names, values, cores, titulo):
    fig2 = px.pie(names=names, values=values, color=cores, title=titulo,)
    fig2.update_layout(
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
    return fig2

def graf_line(x, y, titulo):
    fig3 = px.line(x=x, y=y, title=titulo, markers='o')
    fig3.update_traces(line=dict(color='green', width=2))
    fig3.update_layout(
                    xaxis=dict(
                    tickmode='array',
                    tickvals=x,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')))
    return fig3

def graf_funil(x, y):
    fig4 = px.funnel(x=x, y=y)
    fig4.update_layout(
                    xaxis=dict(
                    tickmode='array',
                    tickvals=x,
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')),
                    yaxis=dict(
                    tickformat=',',
                    title=None,
                    tickfont=dict(size=14, family='Arial Black')))
    return fig4 

def graf_barra_agrupada(x, y1, y2, nome1, nome2, titulo):
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        x=x,
        y=y1,
        name=nome1
    ))
    fig5.add_trace(go.Bar(
        x=x,
        y=y2,
        name=nome2,
        marker=dict(color='red', opacity=0.7)
    ))
    fig5.update_layout(
        barmode='group',
        title=titulo,
        xaxis_title=None,
        yaxis_title=None,
        legend_title=None,
        font=dict(size=14, family='Arial Black')
    )

    return fig5

def graf_line_agrupada(x, y1, y2, nome1, nome2, titulo):
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(
        x=x,
        y=y1,
        name=nome1
    ))
    fig5.add_trace(go.Scatter(
        x=x,
        y=y2,
        name=nome2,
        marker=dict(color='red', opacity=0.7)
    ))
    fig5.update_layout(
        title=titulo,
        xaxis_title=None,
        yaxis_title=None,
        legend_title=None,
        font=dict(size=14, family='Arial Black')
    )

    return fig5

def graf_funil_agrupada(x, y1, y2, nome1, nome2):
    fig6 = go.Figure()
    fig6.add_trace(go.Funnel(
        name = nome1,
        y = x,
        x = y1,
        ))
    fig6.add_trace(go.Funnel(
        name = nome2,
        y = x,
        x = y2))
    return fig6
        