# Financial Performance & Sales Analytics
## Projet personnel Business Intelligence — Niveau intermédiaire

### 1. Présentation
Ce projet construit une chaîne décisionnelle pour suivre les performances commerciales et financières d'une entreprise fictive. Il couvre la préparation des données avec Python, leur stockage relationnel avec MySQL et leur analyse dans Power BI.

**Important :** les données fournies sont entièrement synthétiques. Elles servent à l'apprentissage et ne représentent aucune entreprise réelle.

### 2. Objectifs métier
- Suivre le chiffre d'affaires, le coût, le bénéfice et la marge.
- Comparer les ventes par mois, région, catégorie et produit.
- Identifier les produits et régions les plus performants.
- Comparer le chiffre d'affaires réel aux objectifs mensuels.
- Suivre les dépenses opérationnelles.

### 3. Architecture
CSV bruts → Python/Pandas (contrôle et nettoyage) → MySQL (modèle relationnel) → Power BI (modèle, DAX, rapports).

### 4. Contenu du dossier
- `data/raw/` : fichiers CSV synthétiques.
- `python/clean_data.py` : contrôle qualité et préparation des fichiers.
- `python/load_mysql.py` : chargement des CSV préparés dans MySQL.
- `sql/schema.sql` : création des tables.
- `sql/analysis_queries.sql` : requêtes SQL d'analyse.
- `powerbi/measures_dax.dax` : mesures DAX proposées.
- `powerbi/dashboard_specification.md` : pages, visuels et filtres recommandés.
- `docs/data_dictionary.md` : dictionnaire des données.
- `docs/project_methodology.md` : démarche et critères de validation.

### 5. Prérequis
- Python 3.10+
- MySQL 8+
- Power BI Desktop
- Pilote MySQL/ODBC adapté pour la connexion depuis Power BI

### 6. Installation et exécution
1. Décompresser le dossier.
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Copier `.env.example` vers `.env`, puis renseigner les paramètres MySQL.
4. Créer la base et les tables en exécutant `sql/schema.sql` dans MySQL.
5. Nettoyer les données :
   ```bash
   python python/clean_data.py
   ```
6. Charger les données dans MySQL :
   ```bash
   python python/load_mysql.py
   ```
7. Dans Power BI Desktop, se connecter à MySQL et importer les tables `dim_*` et `fact_*`.
8. Créer les relations selon le modèle décrit dans `powerbi/dashboard_specification.md`.
9. Ajouter les mesures de `powerbi/measures_dax.dax`, puis construire les pages du rapport.

### 7. Résultats attendus
Un rapport Power BI de trois pages :
- Synthèse exécutive : CA, bénéfice, marge, dépenses, évolution mensuelle.
- Performance commerciale : ventes par région, catégorie et produit.
- Analyse financière : coûts, dépenses, bénéfice et atteinte des objectifs.

### 8. Limites
Les données sont synthétiques et les objectifs mensuels sont générés pour le projet. Les conclusions ne doivent pas être présentées comme des faits concernant le marché tunisien ou une entreprise réelle.
