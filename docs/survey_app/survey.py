import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


df = pd.read_csv("35__welcome_survey_cleaned.csv", sep=";")

st.title("Ankieta")

# usuniecie kolumn. Zostawienie tylko kilku dla potrenowania, sample
df.drop(columns=["fav_animals", "fav_place", "hobby_art", "hobby_books", "hobby_movies", "hobby_other",
"hobby_video_games", "learning_pref_books", "learning_pref_chatgpt", "learning_pref_offline_courses",
"learning_pref_online_courses", "learning_pref_personal_projects", "learning_pref_teaching",
"learning_pref_teamwork", "learning_pref_workshops", "motivation_career", "motivation_challenges",
"motivation_creativity_and_innovation", "motivation_money_and_job", "motivation_personal_growth", 
"motivation_remote", "hobby_sport"] , inplace=True)

# sprawdzenie w naszym brudnopisie ile jest brakujacych wartosci i odpowiednie ich uzupelnienie
df["gender"] = df["gender"].map({0: "Male", 1: "Female"}).fillna("Unknown")
df["industry"] = df["industry"].fillna("Unknown")
df["sweet_or_salty"] = df["sweet_or_salty"].fillna("Unknown")
df["years_of_experience"] = df["years_of_experience"].fillna("Unknown") 

st.write("Ilość ankietowanych osób")
c0, c1, c2 = st.columns([1,1,1])
with c0:
    st.metric(" :man::woman: Ankietowani", len(df))
with c1:
     st.metric(":man: Mężczyzni", len(df[df["gender"] == "Male"]))
with c2:
     st.metric(":woman: Kobiety", len(df[df["gender"] == "Female"]))
 
choose = st.selectbox(
        "Wybierz dane do zaprezentowania",
        [
            "Ile mezczyzn i kobiet wzieło udzial w ankiecie",
            "Jakie wykształcenie posiadają ankietowani",
            "W jakich branzach pracuja ankietowani",
            "Słodkie czy słone?",
            "Jak bardzo ankietowani są doswiadczeni",
            "W jakim przedziale wiekowym znajduja się ankietowani",
        ],
    )

if choose == "Ile mezczyzn i kobiet wzieło udzial w ankiecie":
    st.header(" Płeć")
    counts = df["gender"].value_counts()
    plt.figure(figsize=(10,5))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Płeć")
    plt.ylabel("interviewee")
    plt.grid(False)
    st.pyplot(plt)    

    # fig = px.histogram(df["gender"], x="gender")
    # fig.update_layout(
    #     title="Płeć",
    #     width=600,
    #     height=400,
    # )
    # fig.show()

if choose == "Jakie wykształcenie posiadają ankietowani":
    st.header("Wykształcenie")
    wdf = df.groupby("edu_level", as_index=False).count().rename(columns={"age": "Ankietowani", "edu_level": "Wykształcenie"})
    st.bar_chart(wdf, x="Wykształcenie", y="Ankietowani")

if choose == "W jakich branzach pracuja ankietowani":
    st.header("Branża")
    counts = df["industry"].value_counts()
    plt.figure(figsize=(8,10))
    plt.barh(counts.index, counts.values)
    plt.xlabel("Branża")
    plt.ylabel("interviewee")
    plt.grid(False)
    st.pyplot(plt) 

if choose == "Słodkie czy słone?":

    st.header("Słodkie czy słone?")
    sdf = df.groupby("sweet_or_salty", as_index=False).count().rename(columns={"sweet_or_salty":"sweet_or_salty?", "age":"Ankietowani"})
    st.bar_chart(sdf, x="sweet_or_salty?", y="Ankietowani")

if choose == "Jak bardzo ankietowani są doswiadczeni":
    st.header("Doswiadczenie")
    counts = df["years_of_experience"].value_counts()
    plt.figure(figsize=(10,5))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Doswiadczenie")
    plt.ylabel("interviewee")
    plt.grid(False)
    st.pyplot(plt)

if choose == "W jakim przedziale wiekowym znajduja się ankietowani":
    st.header("Wiek")
    counts = df["age"].value_counts()
    plt.figure(figsize=(10,5))
    plt.bar(counts.index, counts.values)
    plt.xlabel("Wiek")
    plt.ylabel("interviewee")
    plt.grid(False)
    st.pyplot(plt)

with st.sidebar:
    value = st.slider("Wybierz ilosc losowych probek", 0, 140, 5)
    if st.button("Pokaz losowe dane"):
        st.dataframe(df.sample(value), hide_index=True)