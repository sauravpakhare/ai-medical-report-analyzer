import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw = pd.read_csv(os.path.join(BASE_DIR, "datasets", "RAW_DATASET.csv"))

report = []

# -------------------------
# Missing Values
# -------------------------
missing = raw.isnull().sum()
report.append("MISSING VALUES:\n")
report.append(str(missing))
report.append("\n")

# -------------------------
# Duplicate Rows
# -------------------------
duplicates = raw.duplicated().sum()
report.append(f"DUPLICATE ROWS: {duplicates}\n")

# -------------------------
# Empty Fields
# -------------------------
empty_fields = (raw == "").sum()
report.append("EMPTY FIELDS:\n")
report.append(str(empty_fields))
report.append("\n")

# -------------------------
# Invalid Ages
# -------------------------
invalid_age = raw[(raw["Age"] < 0) | (raw["Age"] > 120)]
report.append(f"INVALID AGE RECORDS: {len(invalid_age)}\n")

# -------------------------
# Unrealistic Hemoglobin
# -------------------------
invalid_hemo = raw[(raw["Hemoglobin"] < 5) | (raw["Hemoglobin"] > 25)]
report.append(f"UNREALISTIC HEMOGLOBIN RECORDS: {len(invalid_hemo)}\n")

# -------------------------
# Unrealistic Sugar
# -------------------------
invalid_sugar = raw[(raw["Blood_Sugar_Fasting"] < 20) | (raw["Blood_Sugar_Fasting"] > 600)]
report.append(f"UNREALISTIC SUGAR RECORDS: {len(invalid_sugar)}\n")

# -------------------------
# Save Report
# -------------------------
report_path = os.path.join(BASE_DIR, "reports", "validation_report.txt")

with open(report_path, "w") as f:
    f.write("\n".join(report))

print("Validation completed.")
print("Report saved to reports/validation_report.txt")