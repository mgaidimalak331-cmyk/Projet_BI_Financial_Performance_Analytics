# Dictionnaire des données

Toutes les données sont synthétiques.

| Fichier / table | Champ | Description |
|---|---|---|
| customers / dim_customer | customer_id | Identifiant unique du client |
| | customer_name | Nom fictif du client |
| | region | Région commerciale |
| | customer_segment | Particulier, Entreprise ou PME |
| | signup_date | Date d'inscription |
| products / dim_product | product_id | Identifiant du produit |
| | product_name | Nom du produit |
| | category | Catégorie commerciale |
| | unit_price | Prix unitaire fictif |
| | unit_cost | Coût unitaire fictif |
| sales / fact_sales | sale_id | Identifiant unique de vente |
| | sale_date | Date de vente |
| | customer_id / product_id | Références client et produit |
| | quantity | Quantité vendue |
| | discount_rate | Taux de remise (ex. 0.10 = 10 %) |
| | revenue | Chiffre d'affaires net de remise |
| | cost | Coût total des articles |
| | profit | Bénéfice brut de la vente |
| expenses / fact_expense | expense_id | Identifiant de dépense |
| | expense_date | Date de dépense |
| | expense_type | Type de dépense |
| | amount | Montant de la dépense |
| targets / fact_target | target_year / target_month | Période de l'objectif |
| | region | Région concernée |
| | sales_target | Objectif de chiffre d'affaires |

## Règles métier
- Chiffre d'affaires = quantité × prix unitaire × (1 − remise).
- Bénéfice brut = chiffre d'affaires − coût des articles.
- Marge (%) = bénéfice brut / chiffre d'affaires.
- Écart à l'objectif = chiffre d'affaires réel − objectif.
