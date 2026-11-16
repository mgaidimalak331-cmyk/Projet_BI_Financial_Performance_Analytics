from pathlib import Path
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
required = ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]
missing = [k for k in required if not os.getenv(k)]
if missing:
    raise SystemExit("Variables manquantes dans .env : " + ", ".join(missing))

url = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?charset=utf8mb4"
)
engine = create_engine(url)

DATA = ROOT / "data" / "processed"

def main():
    mapping = {
        "customers_clean.csv": ("dim_customer", {"customer_id":"customer_id","customer_name":"customer_name","region":"region","customer_segment":"customer_segment","signup_date":"signup_date"}),
        "products_clean.csv": ("dim_product", {"product_id":"product_id","product_name":"product_name","category":"category","unit_price":"unit_price","unit_cost":"unit_cost"}),
        "sales_clean.csv": ("fact_sales", {"sale_id":"sale_id","sale_date":"sale_date","customer_id":"customer_id","product_id":"product_id","region":"region","quantity":"quantity","unit_price":"unit_price","discount_rate":"discount_rate","revenue":"revenue","cost":"cost","profit":"profit"}),
        "expenses_clean.csv": ("fact_expense", {"expense_id":"expense_id","expense_date":"expense_date","region":"region","expense_type":"expense_type","amount":"amount"}),
        "targets_clean.csv": ("fact_target", {"target_year":"target_year","target_month":"target_month","region":"region","sales_target":"sales_target"})
    }
    with engine.begin() as conn:
        # Réinitialisation contrôlée des tables de faits/dimensions pour rendre le chargement reproductible
        conn.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        for table, _ in mapping.values():
            conn.execute(text(f"TRUNCATE TABLE {table}"))
        conn.execute(text("SET FOREIGN_KEY_CHECKS=1"))

    for filename, (table, _) in mapping.items():
        df = pd.read_csv(DATA / filename)
        df.to_sql(table, engine, if_exists="append", index=False, method="multi", chunksize=500)
        print(f"{table}: {len(df)} lignes chargées")

    print("Chargement MySQL terminé.")

if __name__ == "__main__":
    main()
