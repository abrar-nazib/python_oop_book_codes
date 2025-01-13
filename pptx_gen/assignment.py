import pandas as pd
import numpy as np
from scipy import stats

df1 = pd.read_excel("data/public_school_data.xlsx")
df2 = pd.read_excel("data/private_school_data.xlsx")
df3 = pd.read_excel("data/kindergarden_school_data.xlsx")

df1["Group"] = "Group A"
df2["Group"] = "Group B"
df3["Group"] = "Group C"

# Calculate Z-scores for each group
df1["Z Score"] = stats.zscore(df1["Test Score"])
df2["Z Score"] = stats.zscore(df2["Test Score"])
df3["Z Score"] = stats.zscore(df3["Test Score"])


def get_percentiles(df):
    percentiles = {
        "25th": np.percentile(df["Test Score"], 25),
        "50th": np.percentile(df["Test Score"], 50), 
        "75th": np.percentile(df["Test Score"], 75),
    }
    return percentiles


# Calculate and print percentiles for each group
print("=== Percentiles for each group ===")
for group_name, group_df in [("Group A", df1), ("Group B", df2), ("Group C", df3)]:
    percentiles = get_percentiles(group_df)
    print(f"\n{group_name}:")
    print(f"25th percentile: {percentiles['25th']}")
    print(f"50th percentile: {percentiles['50th']}")
    print(f"75th percentile: {percentiles['75th']}")

# Combine all dataframes and sort by Z Score
df = pd.concat([df1, df2, df3])
df = df.sort_values(by="Z Score", ascending=False).reset_index(drop=True)

# Add merit rank
df["Merit Rank"] = df.index + 1


# Function to calculate percentage of students from each group in top 100
def calculate_group_percentages(top_df):
    total = len(top_df)
    group_counts = top_df["Group"].value_counts()
    percentages = (group_counts / total) * 100
    return percentages


# Get top 100 students and calculate percentages
top_100 = df.head(100)
group_percentages = calculate_group_percentages(top_100)

print("\n=== Percentage of students from each group in top 100 ===")
for group, percentage in group_percentages.items():
    print(f"{group}: {percentage:.2f}%")

# Save the final merit list to Excel
df.to_excel("final_merit_list.xlsx", index=False)

# Print summary statistics
print("\n=== Summary Statistics ===")
print(f"Total number of students: {len(df)}")
print("\nZ-Score Statistics:")
print(df.groupby("Group")["Z Score"].describe())

# Optional: Display first few rows of the merit list
print("\n=== Top 10 Students in Merit List ===")
print(df[["Merit Rank", "Name", "Group", "Test Score", "Z Score"]].head(10))
