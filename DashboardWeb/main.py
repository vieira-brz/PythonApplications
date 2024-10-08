import streamlit as st
import pandas as pd
import plotly.express as px

# Página cobrindo a área toda...
st.set_page_config(layout="wide")

# Base de dados do tipo CSV
df = pd.read_csv('./supermarket_sales.csv', sep=';', decimal=',')

# Tratamento de datas...
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

# Mês e ano separados...
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Filtro por mês...
df_filtered = df[df["Month"] == month]

# Criando colunas do streamlit para "abrigar" os gráficos...
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Faturamento por dia, filtrado pelo mês selecionado / cidade...
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Tipo de produto mais vendido...
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Contribuição por filial...
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Faturamento por tipo de pagamento...
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Como estão as avaliações das filiais por cidade?
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)

#
# Rodar streamlit >> streamlit run main.py
#