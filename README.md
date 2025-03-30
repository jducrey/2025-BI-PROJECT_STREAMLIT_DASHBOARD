# PROJECT-STREAMLIT-DASHBOARD
Data Analysis and Data Visualization Project, through the creation of a dashboard, using the Python's package Streamlit.

## Analyse et Visualisation du Trafic Aérien Français
Ce projet propose une application interactive développée avec Streamlit pour analyser et visualiser l'évolution du trafic aérien en France. L'application permet d'explorer des données détaillées sur les principaux aéroports français, en offrant des informations sur leur superficie, le nombre de compagnies aériennes opérant, les destinations desservies, ainsi que des statistiques annuelles sur le nombre de passagers et de vols. Les données utilisées proviennent du Ministère de la transition écologique et ont été récupérées via la plateforme data.gouv.fr. Elles ont été retraitées, reformatées, agrégées et enrichies avant la construction de ce tableau de bord.
Les données originales sont disponibles à l'adresse suivante : [data.gouv](https://www.data.gouv.fr/fr/datasets/?q=Transport+a%C3%A9rien).

### Table des Matières
- Outils et Technologies
- Structuration du Dashboard
- Utilisation

### 🛠️ Outils et Technologies
Avant de pouvoir exécuter cette application, assurez-vous d'avoir installé les éléments suivants :
- VS Code (IDE)
- streamlit (package Python)
- pandas (package Python)
- pyplot (package Python)

### Structuration du Dashboard

Voici le premier visuel sur le dashboard, à l'ouverture de la page web:
<img width="869" alt="Accueil" src="https://github.com/user-attachments/assets/7016a1a8-b534-42fc-9558-94ef38b28d5c" />

Un visuel permet de parcourir les données, avec des filtres sur les aéroports et les années:
<img width="941" alt="Données" src="https://github.com/user-attachments/assets/38eec663-ad8f-4eb1-807b-eda3b68f2ddb" />

Un visuel permet de résumer les principales statistiques descriptives, pour l'ensemble des données filtrées:
<img width="940" alt="Statistiques" src="https://github.com/user-attachments/assets/44995e01-2847-4cc0-a8f5-4692901993ec" />

##### Pour l'analyse du trafic aérien français par aéroport:

Un premier graphique présente l'évolution du nombre de passagers pour les années et les aéroports de la sélection: 
<img width="940" alt="Passagers" src="https://github.com/user-attachments/assets/efc8aa57-7aa4-4e6d-8faf-03cd6094fb2e" />

Un deuxième graphique présente l'évolution du nombre de vols pour les années et les aéroports de la sélection: 
<img width="940" alt="Mouvements" src="https://github.com/user-attachments/assets/5c50a26a-c838-4673-98d0-70b0471980d7" />

Une animation permet de montrer de manière visuelle et dynamique, l'évolution du nombre de passagers en fonction de celle du nombre de vols, pour chaque aéroport sélectionné, au fil des années: 
![Evolution](https://github.com/user-attachments/assets/df6f7839-21fc-4fbf-95a7-ee7337588b23)

Des graphiques en tarte permettent de visualiser la répartition du trafic aérien, en passagers et en vols, sur diverses sélections d'aéroports et pour différentes sélections d'année entre 1986 et 2011:
<img width="864" alt="Répartition" src="https://github.com/user-attachments/assets/aa58018b-5a0f-4a9a-b65a-e7847965c004" />

##### Pour l'analyse des données des aéroports:

Une carte intéractive permet de visualiser la localisation des aéroports, ainsi que leurs aménagement en zoomant dessus:
<img width="645" alt="Map" src="https://github.com/user-attachments/assets/a91d32d9-3425-4dcc-b022-da3981250e3e" />

Un graphique à barre permet de comparer les aéroports, en fonction de leurs caractéristiques:
<img width="938" alt="Caractéristiques" src="https://github.com/user-attachments/assets/becd50dd-5176-4d8f-a8ca-d7e5ce3c61c8" />

Une page de Documentation donne le contexte, dans lequel ce dashboard a été développé:
<img width="532" alt="Documentation" src="https://github.com/user-attachments/assets/3f4fca34-cbf4-4c0f-991e-959e790bb4dc" />

Différents onglets permettent de structurer la répartition des graphes et des visuels, dans le dashboard, pour rationnaliser les aspects des analyses.

<img width="536" alt="Structure1" src="https://github.com/user-attachments/assets/00d47221-a8e0-431d-a3f7-ea11603b21ad" />
<img width="539" alt="Structure2" src="https://github.com/user-attachments/assets/b4342613-fa55-4b32-aa17-323466a0b5df" />
<img width="539" alt="Structure3" src="https://github.com/user-attachments/assets/b3f19a9a-be10-4fe8-ac61-43058a8c0cbc" />

### Utilisation
Le dépôt contient une vidéo présentant les différents onglets du dashboard et leurs contenus, ainsi que les filtres permettant de personnaliser nos analyses.

Pour lancer l'application Streamlit, exécutez la commande suivante dans le répertoire du projet :

streamlit run Dashboard_streamlit.py

Ensuite, ouvrez votre navigateur web et accédez à l'URL indiquée dans le terminal pour interagir avec l'application.

### 📩 Contact
Si vous avez des questions ou des retours, n'hésitez pas à me contacter via GitHub !
