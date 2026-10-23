# 📊 Analyse Budgétaire : Budget Prévisionnel vs Dépenses Réelles

## 📌 Présentation du projet

Ce projet consiste à analyser et à comparer les dépenses budgétisées aux dépenses réellement engagées sur une période de 12 mois, de janvier à décembre 2023.

Développé avec Python et Streamlit, ce projet propose un tableau de bord interactif permettant de suivre la performance financière, d'identifier les écarts budgétaires et de faciliter la prise de décision fondée sur les données.
## 📸 Aperçu du tableau de bord

Voici un aperçu du tableau de bord interactif développé avec Python et Streamlit pour analyser les écarts entre les dépenses budgétisées et les dépenses réelles.

## 🎯 Objectifs du projet

- Comparer les dépenses prévisionnelles aux dépenses réelles.
- Suivre l'exécution budgétaire mensuelle.
- Identifier les catégories de dépenses présentant des dépassements budgétaires.
- Calculer et analyser les écarts budgétaires et leurs pourcentages.
- Produire des indicateurs et des visualisations pour faciliter le pilotage financier.
- Formuler des recommandations pour améliorer la maîtrise des coûts et la planification budgétaire.

## 📸 Aperçu du tableau de bord

![Tableau de bord Analyse Budgétaire](budget_vs_actual_dashboard.png)

## 🛠️ Outils et technologies

- **Python** : programmation et calculs financiers.
- **Pandas** : manipulation, nettoyage et analyse des données.
- **Plotly** : création de visualisations interactives.
- **Streamlit** : développement du tableau de bord interactif.
- **GitHub** : gestion du code source et documentation du projet.

## 📈 Principaux résultats financiers

| Indicateur | Résultat |
|---|---:|
| Budget total | 1 762 200 |
| Dépenses réelles | 1 718 180 |
| Écart budgétaire total | -44 020 |
| Taux d'exécution budgétaire | 97,50 % |
| Période analysée | Janvier–décembre 2023 |

**Interprétation :** les dépenses réelles sont inférieures au budget prévisionnel de 44 020 unités monétaires, soit un taux d'exécution budgétaire de 97,50 %.

## 🔍 Principaux constats

- Les dépenses globales sont restées inférieures au budget annuel prévu.
- Les coûts opérationnels dépassent le budget de 9 082 unités monétaires.
- Les coûts de maintenance présentent un dépassement de 2 487 unités monétaires.
- Les coûts de développement, de marketing, de déplacement et de formation sont restés globalement en dessous de leurs budgets respectifs.
- L'analyse mensuelle met en évidence des périodes de dépassement et de sous-exécution budgétaire.

## 💡 Recommandations métier

- Examiner les causes des dépassements observés dans les coûts opérationnels et de maintenance.
- Mettre en place un suivi régulier des écarts budgétaires afin de détecter rapidement les anomalies.
- Réviser les hypothèses budgétaires à partir des dépenses réellement observées.
- Renforcer le contrôle des coûts tout en préservant les activités essentielles.
- Utiliser les résultats de l'analyse pour améliorer la planification financière et l'allocation des ressources.

## 🚀 Tableau de bord interactif

Le tableau de bord permet aux utilisateurs de :

- Filtrer les données par mois et par catégorie de dépenses.
- Comparer les budgets prévisionnels aux dépenses réelles.
- Visualiser les écarts budgétaires mensuels.
- Identifier les catégories en dépassement ou en dessous du budget.
- Consulter un tableau récapitulatif des indicateurs financiers.

**Application en ligne :** [Accéder au tableau de bord Budget vs Actual Analysis](https://budget-vs-actual-analysis-bvkcg5ux3bsnme5wgej3rs.streamlit.app/)

*Remplace le lien ci-dessus par l'URL de ton application Budget vs Actual Analysis.*

## 📂 Structure du dépôt GitHub

```text
Budget-vs-Actual-Analysis/
├── budget_Vs_Actual.py
├── budget_vs_actual.csv
├── budget_vs_actual_dashboard.png
├── requirements.txt
└── README.md
```

## ▶️ Installation et exécution en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/lordleny-png/Budget-vs-Actual-Analysis.git
```

### 2. Accéder au dossier du projet

```bash
cd Budget-vs-Actual-Analysis
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application

```bash
streamlit run budget_Vs_Actual.py
```

Le tableau de bord s'ouvrira dans ton navigateur.

## 📊 Source des données

Le jeu de données provient de Kaggle :

[Financial Dataset — Expenses Budget vs Actual](https://www.kaggle.com/datasets/saharsyed/financial-dataset-expenses-budget-vs-actual)

Il contient les budgets prévisionnels et les dépenses réelles mensuelles de six catégories de coûts pour l'année 2023.

## ⚠️ Avertissement

Ce projet est réalisé à des fins pédagogiques et de constitution d'un portfolio professionnel. Les résultats dépendent exclusivement du jeu de données utilisé et ne constituent pas des états financiers audités.

## 👤 Auteur

**Leny Napala**

Business Analytics | Analyse de données | Suivi de la performance financière
