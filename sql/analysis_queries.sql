-- 1. Chiffre d'affaires et bénéfice par mois
SELECT YEAR(sale_date) AS annee, MONTH(sale_date) AS mois,
       SUM(revenue) AS chiffre_affaires, SUM(profit) AS benefice
FROM fact_sales
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY annee, mois;

-- 2. Top 10 produits par chiffre d'affaires
SELECT p.product_name, p.category, SUM(s.revenue) AS chiffre_affaires
FROM fact_sales s JOIN dim_product p ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY chiffre_affaires DESC LIMIT 10;

-- 3. Performance par région
SELECT region, SUM(revenue) AS chiffre_affaires,
       SUM(profit) AS benefice, SUM(quantity) AS quantites
FROM fact_sales GROUP BY region ORDER BY chiffre_affaires DESC;

-- 4. Rentabilité par catégorie
SELECT p.category, SUM(s.revenue) AS ca, SUM(s.cost) AS cout,
       SUM(s.profit) AS benefice,
       ROUND(100 * SUM(s.profit) / NULLIF(SUM(s.revenue),0), 2) AS marge_pct
FROM fact_sales s JOIN dim_product p ON s.product_id = p.product_id
GROUP BY p.category ORDER BY benefice DESC;

-- 5. Dépenses par type
SELECT expense_type, SUM(amount) AS depenses
FROM fact_expense GROUP BY expense_type ORDER BY depenses DESC;

-- 6. CA réel comparé aux objectifs (agrégation mensuelle/région)
SELECT YEAR(s.sale_date) AS annee, MONTH(s.sale_date) AS mois, s.region,
       SUM(s.revenue) AS ca_reel, t.sales_target,
       SUM(s.revenue) - t.sales_target AS ecart
FROM fact_sales s
JOIN fact_target t ON YEAR(s.sale_date)=t.target_year
                  AND MONTH(s.sale_date)=t.target_month
                  AND s.region=t.region
GROUP BY YEAR(s.sale_date), MONTH(s.sale_date), s.region, t.sales_target
ORDER BY annee, mois, s.region;

-- 7. Clients les plus importants
SELECT c.customer_id, c.customer_name, c.region,
       SUM(s.revenue) AS ca_client, COUNT(*) AS nb_achats
FROM dim_customer c JOIN fact_sales s ON c.customer_id=s.customer_id
GROUP BY c.customer_id, c.customer_name, c.region
ORDER BY ca_client DESC LIMIT 15;
