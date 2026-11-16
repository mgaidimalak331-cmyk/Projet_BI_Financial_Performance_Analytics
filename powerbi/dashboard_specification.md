# Spécification du rapport Power BI

## Modèle de données
Créer les relations suivantes :
- `dim_customer[customer_id]` (1) → `fact_sales[customer_id]` (*)
- `dim_product[product_id]` (1) → `fact_sales[product_id]` (*)
- `Calendar[Date]` (1) → `fact_sales[sale_date]` (*)
- `Calendar[Date]` (1) → `fact_expense[expense_date]` (*)

Pour les objectifs, créer une clé YearMonthRegion dans Power Query ou dans les tables, puis relier une dimension mensuelle/région dédiée à `fact_target`. Éviter une relation directe ambiguë entre plusieurs tables de faits.

## Page 1 — Synthèse exécutive
**Cartes KPI :** Chiffre d'affaires, Bénéfice brut, Marge (%), Dépenses opérationnelles, Résultat après dépenses.

**Visuels :**
- Courbe : chiffre d'affaires par mois.
- Histogramme : CA par région.
- Barres : bénéfice par catégorie.
- Segmentations : année, région, catégorie.

## Page 2 — Performance commerciale
- Top 10 produits par CA.
- Quantités vendues par catégorie.
- CA par région et par mois.
- Tableau détaillé produit / CA / coût / bénéfice / marge.
- Filtres : date, région, catégorie, segment client.

## Page 3 — Analyse financière
- Bénéfice brut et dépenses par mois.
- Dépenses par type.
- CA réel vs objectif par mois et région.
- Écart à l'objectif et taux de réalisation.
- Tableau de contrôle des régions sous objectif.

## Bonnes pratiques
- Utiliser une palette sobre et cohérente.
- Afficher la devise choisie et la documenter. Les montants du dataset sont des unités monétaires fictives, pas des TND réels.
- Ajouter des titres dynamiques et des info-bulles.
- Vérifier les totaux du rapport avec les requêtes SQL.
