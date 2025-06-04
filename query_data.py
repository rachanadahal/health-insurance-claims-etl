import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

print(" Script started")

conn = sqlite3.connect('claims.db')
cursor = conn.cursor()

# Showing all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Showing sample data
cursor.execute("SELECT * FROM claims LIMIT 5;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Checking out column names and sample data
cursor.execute("SELECT * FROM claims LIMIT 5;")
rows = cursor.fetchall()

# Printing the sample data
for row in rows:
    print(row)

# Printing out the column names
col_names = [description[0] for description in cursor.description]
print("🧾 Column Names:", col_names)

# Average claim amount by gender
cursor.execute("""
    SELECT gender, AVG(Cost) AS avg_cost
    FROM claims
    GROUP BY gender
""")
results = cursor.fetchall()
print("Average Claim Cost by Gender:")
for row in results:
    print(row)



avg_cost_by_gender = [
    ('Female', 400.0),
    ('Male', 750.0)
]

# Separating the data for plotting
genders = [item[0] for item in avg_cost_by_gender]
avg_costs = [item[1] for item in avg_cost_by_gender]

# Creating a simple bar plot
sns.barplot(x=genders, y=avg_costs, palette="pastel")

plt.title("Average Claim Cost by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Cost")
plt.show()

conn.close()
