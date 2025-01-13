import pandas as pd
import numpy as np
from scipy import stats
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Read the Excel files
df1 = pd.read_excel("data/private_school_data.xlsx")
df2 = pd.read_excel("data/public_school_data.xlsx")
df3 = pd.read_excel("data/kindergarden_school_data.xlsx")

# Add group identifiers
df1["Group"] = "Group A"
df2["Group"] = "Group B"
df3["Group"] = "Group C"

# Calculate Z-scores for each group
df1["Z Score"] = stats.zscore(df1["Test Score"])
df2["Z Score"] = stats.zscore(df2["Test Score"])
df3["Z Score"] = stats.zscore(df3["Test Score"])


# Calculate percentile ranks for each group
def calculate_percentile_ranks(df):
    df["Percentile Rank"] = df["Test Score"].rank(pct=True) * 100
    return df


df1 = calculate_percentile_ranks(df1)
df2 = calculate_percentile_ranks(df2)
df3 = calculate_percentile_ranks(df3)


# Calculate percentiles for group summary
def get_percentiles(df):
    percentiles = {
        "25th": np.percentile(df["Test Score"], 25),
        "50th": np.percentile(df["Test Score"], 50),
        "75th": np.percentile(df["Test Score"], 75),
    }
    return percentiles


# Calculate group percentiles
percentiles_data = {}
for group_name, group_df in [("Group A", df1), ("Group B", df2), ("Group C", df3)]:
    percentiles_data[group_name] = get_percentiles(group_df)

# Combine all dataframes and create merit list
combined_df = pd.concat([df1, df2, df3])
combined_df = combined_df.sort_values(by="Z Score", ascending=False).reset_index(
    drop=True
)
combined_df["Merit Rank"] = combined_df.index + 1

# Calculate top 100 statistics
top_100 = combined_df.head(100)
group_percentages = top_100["Group"].value_counts(normalize=True) * 100


def create_pdf_report(filename="student_analysis_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle(
        "CustomTitle", parent=styles["Heading1"], fontSize=24, spaceAfter=30
    )
    elements.append(Paragraph("Student Analysis Report", title_style))
    elements.append(Spacer(1, 20))

    # 1. Group Percentiles Section
    elements.append(Paragraph("1. Group Percentiles Analysis", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    percentiles_table_data = [
        ["Group", "25th Percentile", "50th Percentile", "75th Percentile"]
    ]
    for group, percs in percentiles_data.items():
        percentiles_table_data.append(
            [
                group,
                f"{percs['25th']:.2f}",
                f"{percs['50th']:.2f}",
                f"{percs['75th']:.2f}",
            ]
        )

    t = Table(percentiles_table_data)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )
    elements.append(t)
    elements.append(Spacer(1, 20))

    # 2. Top 100 Analysis Section
    elements.append(Paragraph("2. Top 100 Students Analysis", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    top_100_table_data = [["Group", "Percentage in Top 100"]]
    for group, percentage in group_percentages.items():
        top_100_table_data.append([group, f"{percentage:.2f}%"])

    t2 = Table(top_100_table_data)
    t2.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )
    elements.append(t2)
    elements.append(Spacer(1, 20))

    # 3. Top 10 Students Section with Individual Percentiles
    elements.append(Paragraph("3. Top 10 Students", styles["Heading2"]))
    elements.append(Spacer(1, 10))

    top_10_data = [
        ["Rank", "Name", "Group", "Test Score", "Z Score", "Percentile Rank"]
    ]
    for _, row in combined_df.head(10).iterrows():
        top_10_data.append(
            [
                str(int(row["Merit Rank"])),
                row["Name"],
                row["Group"],
                str(row["Test Score"]),
                f"{row['Z Score']:.3f}",
                f"{row['Percentile Rank']:.2f}%",
            ]
        )

    t3 = Table(top_10_data)
    t3.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
    )
    elements.append(t3)

    doc.build(elements)


# Generate all reports
create_pdf_report()

# Save individual group data with percentile ranks
df1.to_excel("group_a_scores.xlsx", index=False)
df2.to_excel("group_b_scores.xlsx", index=False)
df3.to_excel("group_c_scores.xlsx", index=False)
combined_df.to_excel("final_merit_list.xlsx", index=False)

print("Report generation completed!")
print("Files generated:")
print("1. student_analysis_report.pdf")
print("2. final_merit_list.xlsx")
print("3. group_a_scores.xlsx")
print("4. group_b_scores.xlsx")
print("5. group_c_scores.xlsx")
