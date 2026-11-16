# Méthodologie et critères de validation

## Questions métier
1. Comment évolue le chiffre d'affaires dans le temps ?
2. Quelles régions et catégories contribuent le plus au bénéfice ?
3. Quels produits sont les plus performants ?
4. Quel est le niveau des dépenses opérationnelles ?
5. Les objectifs mensuels sont-ils atteints ?

## Contrôles qualité
- Unicité de `sale_id`, `customer_id`, `product_id` et `expense_id`.
- Absence de valeurs nulles dans les identifiants et dates indispensables.
- Quantités positives et montants non négatifs.
- Cohérence du calcul du chiffre d'affaires et du bénéfice.
- Intégrité référentielle entre ventes, clients et produits.

## Critères de réussite
- Tous les CSV traités sont chargés sans erreur.
- Les totaux SQL et Power BI concordent.
- Les filtres de date, région et catégorie fonctionnent.
- Chaque KPI possède une définition métier.
- Le README explique comment reproduire le projet.

## Évolutions possibles
- Ajouter une prévision de ventes avec une méthode de séries temporelles.
- Ajouter un suivi du stock.
- Mettre en place un rafraîchissement automatisé des données.
