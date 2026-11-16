from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

def read_csv(name):
    return pd.read_csv(RAW / name)

def main():
    customers = read_csv("customers.csv")
    products = read_csv("products.csv")
    sales = read_csv("sales.csv")
    expenses = read_csv("expenses.csv")
    targets = read_csv("targets.csv")

    # Normalisation des types et contrôles simples
    customers["signup_date"] = pd.to_datetime(customers["signup_date"], errors="coerce")
    sales["sale_date"] = pd.to_datetime(sales["sale_date"], errors="coerce")
    expenses["expense_date"] = pd.to_datetime(expenses["expense_date"], errors="coerce")

    for col in ["quantity", "unit_price", "discount_rate", "revenue", "cost", "profit"]:
        sales[col] = pd.to_numeric(sales[col], errors="coerce")

    # Suppression des lignes sans identifiant/date ou avec quantités incohérentes
    sales = sales.dropna(subset=["sale_id", "sale_date", "customer_id", "product_id"])
    sales = sales[(sales["quantity"] > 0) & (sales["unit_price"] >= 0)]
    sales = sales.drop_duplicates(subset=["sale_id"])

    # Recalcul des montants pour garantir la cohérence
    sales["revenue"] = (sales["quantity"] * sales["unit_price"] *
                        (1 - sales["discount_rate"].fillna(0))).round(2)
    sales["profit"] = (sales["revenue"] - sales["cost"].fillna(0)).round(2)

    customers = customers.drop_duplicates(subset=["customer_id"])
    products = products.drop_duplicates(subset=["product_id"])
    expenses = expenses.dropna(subset=["expense_id", "expense_date", "amount"])
    expenses = expenses[expenses["amount"] >= 0].drop_duplicates(subset=["expense_id"])
    targets = targets.drop_duplicates(subset=["target_year", "target_month", "region"])
    targets = targets[targets["sales_target"] >= 0]

    # Dates au format SQL
    for frame, col in [(customers, "signup_date"), (sales, "sale_date"), (expenses, "expense_date")]:
        frame[col] = frame[col].dt.strftime("%Y-%m-%d")

    frames = {
        "customers_clean.csv": customers,
        "products_clean.csv": products,
        "sales_clean.csv": sales,
        "expenses_clean.csv": expenses,
        "targets_clean.csv": targets
    }
    for filename, frame in frames.items():
        frame.to_csv(OUT / filename, index=False)

    print("Nettoyage terminé.")
    print(f"Ventes conservées : {len(sales)}")
    print(f"Clients : {len(customers)} | Produits : {len(products)}")
    print(f"Dépenses : {len(expenses)} | Objectifs : {len(targets)}")

if __name__ == "__main__":
    main()
