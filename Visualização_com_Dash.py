import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def cria_graficos(df):
    # Histograma
    fig1 = px.histogram(df, x='Gênero', nbins=30, title='Distribuição por Gênero')
    fig2 = px.pie(df, names='Temporada', color='Temporada', hole=0.2, color_discrete_sequence=px.colors.sequential.RdBu)
    #
    # # Gráfico de bolha
    fig3 = px.scatter(df, x='Gênero', y='Temporada', size='Preço', color='Gênero', hover_name='Temporada', size_max=60)
    fig3.update_layout(title='Preço por temporada e Gênero')
    #
    # Gráfico de linha
    fig4 = px.line(df, x='Gênero', y='Preço', color='Gênero', facet_col='Nota')
    fig4.update_layout(
        title='Gênero por Preço e Gênero para cada Nota',
        xaxis_title='Gênero',
        yaxis_title='Preço'
    )
    #
    # Gráfico 3D
    fig5 = px.scatter_3d(df, x='Preço', y='Gênero', z='Nota', color='Gênero')
    # Gráfico de Barra
    fig6 = px.bar(df, x="Gênero", y="Preço", color="Gênero", barmode="group", color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig6.update_layout(
        title='Preço por Gênero',
        xaxis_title='Gênero',
        yaxis_title='Preço',
        legend_title='Gênero por Cores',
        plot_bgcolor='rgba(222, 555, 253, 1)', # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)' # Fundo Externo
    )
    return fig1, fig2, fig3, fig4, fig5, fig6


def cria_app(df):
    # Cria App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 =cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])
    return app

df = pd.read_csv('C:/Users/jonat/Downloads/ecommerce_estatistica.csv')
print(df)

if __name__ == '__main__':
        app = cria_app(df)
        # Executa App
        app.run_server(debug=True, port=8050) # Defalt 8050
