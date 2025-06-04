import pandas as pd
import sqlite3

# Step 1: Extract
df = pd.read_csv("data/claims.csv")

# Step 2: Transform
df["Gender"] = df["Gender"].map({"M": "Male", "F": "Female"})

def age_group(age):
    if age < 30:
        return "Young Adult"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)

# Step 3: Load
conn = sqlite3.connect("claims.db")
df.to_sql("claims", conn, if_exists="replace", index=False)

print("✅ ETL Process Complete. Data loaded into claims.db")

conn.close()
