import streamlit as st
import pandas as pd
import plotly.express as px

# Charger les données
@st.cache_data
def load_data():
    df = pd.read_csv("Trafic_aerien_France_with_coords.csv")
    return df

df = load_data()

# Titre et description
st.title("Etude du Trafic Aérien Français")

st.markdown("""
        Cette étude explore les données relatives aux principaux aéroports français, 
        fournissant des informations détaillées telles que leur superficie en km², 
        le nombre de compagnies aériennes opérant sur chaque plateforme, le nombre de 
        destinations desservies, ainsi que leur localisation géographique.
""")
st.write("""
        De plus, l'analyse inclut des données sur le trafic aérien, notamment le nombre 
        annuel de passagers et de vols pour chacun de ces aéroports, couvrant une période 
        allant de 1986 à 2011.
""")

# Trier le DataFrame par la colonne 'Annee'
df = df.sort_values(by='Annee')

with st.sidebar:
    # Extraire la liste des aéroports uniques
    aeroports = df["Aeroport"].unique().tolist()
    # Ajouter l'option "Tous" au début de la liste
    options = ["Tous"] + aeroports
    # Widget multisélection avec "Tous" sélectionné par défaut
    aeroports_selectionnes = st.multiselect(
        "Sélectionnez un ou plusieurs aéroports :",
        options,
        default=["Tous"]
    )

    # Extraire la liste des années uniques
    annees = df["Annee"].unique().tolist()
    # Ajouter l'option "Tous" au début de la liste
    options = ["Toutes"] + annees
    # Widget multisélection avec "Tous" sélectionné par défaut
    annees_selectionnees = st.multiselect(
        "Sélectionnez une ou plusieurs années :",
        options,
        default=["Toutes"]
    )
    annees_selectionnees2 = st.slider(
    "Sélectionnez une plage d'années",
    min_value=1986,
    max_value=2011,
    value=(1986, 2011),
    step=1,
    )

    # Filtrer le DataFrame en fonction des sélections
    donnees_filtrees = df.copy()

    # Appliquer le filtre des aéroports si "Tous" n'est pas sélectionné
    if "Tous" not in aeroports_selectionnes:
        donnees_filtrees = donnees_filtrees[donnees_filtrees["Aeroport"].isin(aeroports_selectionnes)]

    # Appliquer le filtre des années si "Toutes" n'est pas sélectionné
    if "Toutes" not in annees_selectionnees:
        donnees_filtrees = donnees_filtrees[donnees_filtrees["Annee"].isin(annees_selectionnees)]

    # Appliquer le filtre des années si le curseur slider n'est pas sur sa position initiale:
    if  (1986, 2011) != annees_selectionnees2:
        donnees_filtrees = donnees_filtrees[donnees_filtrees["Annee"].isin(annees_selectionnees2)]

# Créer les onglets
titres_onglets = ["Exploration des données",
                  "Analyse de l'évolution annuelle du trafic aérien français par aéroport",
                  "Analyse des données des aéroports français",
                  "Documentation"
                  ]
onglet1, onglet2, onglet3, onglet4 = st.tabs(titres_onglets)

with onglet1:
    st.subheader("Exploration des données")

    # Créer les sous onglets
    titres_sous_onglets = [
                    "Données filtrées", 
                    "Statistiques générales"
                    ]
    sous_onglet1, sous_onglet2 = st.tabs(titres_sous_onglets)

    with sous_onglet1:
        # Afficher les données filtrées
        st.subheader("Données filtrées")
        st.write(donnees_filtrees)
        st.write("Description des données disponibles pour l'analyse:")
        st.write("Annee: Année de relevé de la donnée.")
        st.write("Passagers_(en_milliers): Nombre de passagers en milliers (ici 1 unité = 1000 passagers réels), ayant transités par l'aéroport, au cours de l'année correspondante.")
        st.write("Mouvements_(en_milliers): Nombre de vols en milliers (ici 1 unité = 1000 vols réels), ayant transités par l'aéroport, au cours de l'année correspondante.")
        st.write("Aeroport: Nom de l'aéroport en question.")
        st.write("LATITUDE: 1ère coordonnée de l'aéroport.")
        st.write("LONGITUDE: 2nde coordonnée de l'aéroport.")
        st.write("Superficie_(km^2): Superficie de l'aéroport, donnée en kilomètre carré. (1 km^2 = 100 hectares)")
        st.write("Nb_Compagnie: Nombre de compagnies aériennes présentes, au sein de l'aéroport.")
        st.write("Nb_Destinations: Nombre de destinations disponibles, en passant par l'aéroport en question.")

    with sous_onglet2:
        # Affichage des statistiques de base
        st.subheader("Statistiques générales")
        st.write(donnees_filtrees.describe())

with onglet2:
    st.subheader("Analyse de l'évolution annuelle du trafic aérien français par aéroport")

    # Créer les sous onglets
    titres_sous_onglets = [
                    "Évolution temporelle du trafic aérien par aéroport", 
                    "Répartitions du trafic aérien par aéroport"
                    ]
    sous_onglet1, sous_onglet2 = st.tabs(titres_sous_onglets)

    with sous_onglet1:
        st.subheader("Évolution temporelle du trafic aérien par aéroport")
        # Visualisation : évolution du trafic
        if "Annee" in df.columns:
            fig = px.line(donnees_filtrees, x="Annee", y="Passagers_(en_milliers)", color="Aeroport", title="Évolution du nombre de passagers annuels, par aéroport")
            st.plotly_chart(fig)

            fig2 = px.line(donnees_filtrees, x="Annee", y="Mouvements_(en_milliers)", color="Aeroport", title="Évolution du nombre de vols annuels, par aéroport")
            st.plotly_chart(fig2)
            st.write("Mouvements correspond au nombre de vols transitant par l'aéroport, au cours de l'année.")

            # Création du graphique animé
            fig3 = px.scatter(donnees_filtrees,
                        x='Mouvements_(en_milliers)',
                        y='Passagers_(en_milliers)',
                        color='Aeroport',
                        animation_frame='Annee',
                        size_max=60,
                        labels={'Mouvements_(en_milliers)': 'Nombre de vols', 'Passagers_(en_milliers)': 'Nombre de passagers'},
                        title="Évolution du nombre de passagers en fonction du nombre de vols par aéroport")

            # Personnalisation de la mise en page
            fig3.update_layout(legend_title_text='Aéroport')
            st.plotly_chart(fig3)


    with sous_onglet2:
        st.subheader("Répartitions du trafic aérien par aéroport")
        # Créer deux colonnes
        col1, col2 = st.columns(2)

        # Premier graphique dans la première colonne
        with col1:
            fig_pie = px.pie(donnees_filtrees, names="Aeroport", values="Passagers_(en_milliers)", title="Répartition du nombre de passagers par aéroport, pour les années sélectionnées")
            st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            fig_pie2 = px.pie(donnees_filtrees, names="Aeroport", values="Mouvements_(en_milliers)", title="Répartition du nombre de vols par aéroport, pour les années sélectionnées")
            st.plotly_chart(fig_pie2, use_container_width=True)



with onglet3:
    st.markdown("## Analyse des données des aéroports français")

    # Créer les sous onglets
    titres_sous_onglets = [
                    "Localisation des aéroports", 
                    "Caractéristiques des aéroports"
                    ]
    sous_onglet1, sous_onglet2 = st.tabs(titres_sous_onglets)

    with sous_onglet1:
        # Carte des aéroports (si tu as des coordonnées GPS)
        if "LATITUDE" in donnees_filtrees.columns and "LONGITUDE" in donnees_filtrees.columns:
            st.subheader("Localisation des aéroports")
            st.map(donnees_filtrees[["LATITUDE", "LONGITUDE"]])

    with sous_onglet2:
        st.subheader("Caractéristiques des aéroports")
        # Conversion du format large au format long
        df_long = donnees_filtrees.melt(id_vars='Aeroport', 
                        value_vars=['Superficie_(km^2)', 'Nb_Compagnie', 'Nb_Destinations'],
                        var_name='Type', 
                        value_name='Nombre')
        # Création du graphique à barres groupées
        bar_plot = px.bar(df_long, 
                    x='Aeroport', 
                    y='Nombre', 
                    color='Type', 
                    barmode='group',
                    labels={'Nombre': 'Valeur', 'Aeroport': 'Aéroport'},
                    title='Comparaison de la superficie en km^2, du nombre de compagnies aériennes et de destinations, par aéroport')
        st.plotly_chart(bar_plot)

with onglet4:
    st.subheader("Documentation")
    st.write("""Ce tableau de bord a été développé dans le cadre d'un projet visant à démontrer 
             mes compétences en analyse et visualisation de données à l'aide de Streamlit. Il 
             permet d'examiner l'évolution temporelle du trafic aérien français en s'appuyant 
             sur des données relatives aux principaux aéroports du pays. Ces données, initialement 
             fournies par le Ministère de la transition écologique et accessibles via la plateforme data.gouv.fr, ont été retraitées,
              reformatées, agrégées et enrichies avant la construction de ce tableau de bord. Les 
             versions originales des données sont disponibles aux liens suivants :""")
    st.write("https://www.data.gouv.fr/fr/datasets/?q=Transport+a%C3%A9rien")
    st.write("""Ce tableau de bord offre ainsi une interface interactive pour explorer et visualiser
            les tendances du trafic aérien en France, en s'appuyant sur des données officielles
            retraitées pour une analyse approfondie.""")

# Lancer l’application en local avec la commande :
# streamlit run Dashboard_streamlit.py