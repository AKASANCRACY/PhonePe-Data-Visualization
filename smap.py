import plotly.express as px
import streamlit as st
import plotly.graph_objs as go

def Map(df,s,data):
    if (data == "Transaction"):
        # Print the resulting dataframe
        df['name'] = df['name'].apply(lambda x: ' '.join([word.capitalize() if word.lower() != 'and' else word for word in x.split()]))
        # Select Name and Count columns
        df = df[['name', 'count', 'amount']]
        fig = px.choropleth(
            df[['name', 'count', 'amount']],
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='name',
            color=s,
            color_continuous_scale='Reds'
            )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
    if (data == "User"):
        # Print the resulting dataframe
        df['name'] = df['name'].apply(lambda x: ' '.join([word.capitalize() if word.lower() != 'and' else word for word in x.split()]))
        # Select Name and Count columns
        df = df[['name', 'appOpens', 'registeredUsers']]
        fig = px.choropleth(
            df[['name', 'appOpens', 'registeredUsers']],
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='name',
            color=s,
            color_continuous_scale='Reds'
            )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig)
