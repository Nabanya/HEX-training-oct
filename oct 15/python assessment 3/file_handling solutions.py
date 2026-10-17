import json
import pandas as pd

# section E
# 47 & 52
with open("event_log.txt", "w", encoding="utf-8") as f:
    f.write("Event registration system initialized.\n")
    f.write("Batch 1 registrations processing...\n")
    f.write("Validation completed for batch 1.\n")

# 48 & 52
with open("event_log.txt", "a", encoding="utf-8") as f:
    f.write("Notification emails sent to confirmed attendees.\n")
    f.write("Event log file updated successfully.\n")

# 49
print("49. Reading Complete File:")
with open("event_log.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 50-51
print("51. Display Line by Line (Without Extra Blank Lines):")
with open("event_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
print("\n")

import csv

# section F
# 53-54
registrations_data = []
with open("registrations.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
        registrations_data.append(cleaned_row)

# 55
print("55. Confirmed Registrations:")
for r in registrations_data:
    if r["status"].lower() == "confirmed":
        print(f"    {r['registration_id']} - {r['attendee_name']}")

# 56
print("\n56. Registrations from Hyderabad:")
for r in registrations_data:
    if r["city"].lower() == "hyderabad":
        print(f"    {r['registration_id']} - {r['attendee_name']}")

# 57-58
print("\n58. Registrations with Amount > ₹7,000:")
for r in registrations_data:
    r["amount"] = float(r["amount"])
    if r["amount"] > 7000:
        print(f"    {r['attendee_name']} (₹{r['amount']:.2f})")

# 59
total_reg_amount = sum(r["amount"] for r in registrations_data)
print(f"\n59. Total Registration Amount: ₹{total_reg_amount:.2f}")

# 60
all_reg_cities = [r["city"] for r in registrations_data]
unique_reg_cities = set(all_reg_cities)
print(f"60. Unique Cities: {unique_reg_cities}\n")

# section G

# 61
with open("staff.json", "r", encoding="utf-8") as file:
    staff_data = json.load(file)

# 62
print(f"62. Datatype of staff_data: {type(staff_data)}")

# 63
print("63. Staff Names:", [s["name"] for s in staff_data])

# 64
ops_staff = [s["name"] for s in staff_data if s["department"].lower() == "operations"]
print("64. Operations Department Staff:", ops_staff)

# 65
high_salary_staff = [s["name"] for s in staff_data if s["salary"] > 75000]
print("65. Salary > ₹75,000:", high_salary_staff)

# 66
python_staff = [s["name"] for s in staff_data if "Python" in s["skills"]]
print("66. Staff with Python Skill:", python_staff)

# 67
print("\n67. Staff Performance Metrics:")
for s in staff_data:
    rating = s["performance"]["rating"]
    events_handled = s["performance"].get("events handled") or s["performance"].get("events_handled")
    print(f"    Name: {s['name']} | Rating: {rating} | Events Handled: {events_handled}")

# 68
top_performers = [s["name"] for s in staff_data if s["performance"]["rating"] > 4.5]
print(f"\n68. Staff Rating > 4.5: {top_performers}")

# 69
all_skills = []
for s in staff_data:
    all_skills.extend(s["skills"])
print("69. All Extracted Skills:", all_skills)

# 70
unique_skills = set(all_skills)
print(f"70. Unique Skills: {unique_skills}")

# 71
sorted_by_salary = sorted(staff_data, key=lambda s: s["salary"], reverse=True)
print("71. Sorted by Salary Descending:", [f"{s['name']} (₹{s['salary']})" for s in sorted_by_salary])

# 72
sorted_by_rating = sorted(staff_data, key=lambda s: s["performance"]["rating"], reverse=True)
print("72. Sorted by Rating Descending:", [f"{s['name']} ({s['performance']['rating']})" for s in sorted_by_rating])

# 73
for s in staff_data:
    s_id = s.get("staff id") or s.get("staff_id")
    if s_id == 503:
        if "Pandas" not in s["skills"]:
            s["skills"].append("Pandas")

# 74
with open("staff_updated.json", "w", encoding="utf-8") as file:
    json.dump(staff_data, file, indent=4)
print("74. Modified data saved to 'staff_updated.json'\n")


# section I
# 80
df_regs = pd.read_csv("registrations.csv")
df_regs.columns = df_regs.columns.str.strip()

for col in df_regs.select_dtypes(include="object").columns:
    df_regs[col] = df_regs[col].str.strip()

# 81
print("81. First 5 Rows:\n", df_regs.head())
print("\n81. Last 5 Rows:\n", df_regs.tail())
print("\n81. Shape:", df_regs.shape)
print("\n81. Columns:", df_regs.columns.tolist())
print("\n81. Datatypes:\n", df_regs.dtypes)

# 82
print("\n82. Selected Columns:\n", df_regs[['attendee_name', 'city', 'status', 'amount']])

# 83
confirmed_df = df_regs.query("status == 'Confirmed'")
print("\n83. Confirmed Registrations (via query()):\n", confirmed_df[['registration_id', 'attendee_name', 'status']])

# 84
amt_gt_6000 = df_regs[df_regs['amount'] > 6000]
print("\n84. Registrations > ₹6,000:\n", amt_gt_6000[['attendee_name', 'amount']])

# 85
hyd_confirmed = df_regs[(df_regs['status'] == 'Confirmed') & (df_regs['city'] == 'Hyderabad')]
print("\n85. Confirmed Registrations from Hyderabad:\n", hyd_confirmed[['attendee_name', 'city', 'status']])

# 86
print("\n86. Registration Count by Status:\n", df_regs['status'].value_counts())

# 87
print("\n87. Total Amount by Status:\n", df_regs.groupby('status')['amount'].sum())

# 88
print("\n88. Average Amount by City:\n", df_regs.groupby('city')['amount'].mean())