# cord19_explorer_short.py

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

st.title("CORD-19 Explorer")

# Load & clean data
df = pd.read_csv('metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df.get('abstract', '').fillna('')
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))

# Filter by year
year_range = st.slider("Year range", 2019, 2022, (2020, 2021))
dff = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Visualizations
st.subheader("Publications by Year")
st.bar_chart(dff := dff := dff := dff := dff := dff := dff := dff := dff := dff := df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]['year'].value_counts().sort_index())

if 'journal' in df.columns:
    st.subheader("Top Journals")
    st.bar_chart(dff['journal'].value_counts().head(10))

if 'title' in df.columns:
    st.subheader("Word Cloud of Titles")
    wc = WordCloud(width=800, height=400, background_color='white').generate(' '.join(dff['title'].dropna().astype(str)))
    st.image(wc.to_array())

if 'source_x' in df.columns:
    st.subheader("Paper Counts by Source")
    st.bar_chart(dff['source_x'].value_counts())

st.subheader("Sample Data")
st.dataframe(dff.head())
