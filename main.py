import pandas as pd
import matplotlib.pyplot as plt
import re

# -----------------------------
# Config-Based Scoring System
# -----------------------------
SCORING_RULES = {
    "python": 5,
    "machine learning": 5,
    "sql": 3,
    "html": 2,
    "css": 2
}

# -----------------------------
# Load CSV File
# -----------------------------
def load_data(file_path):
    return pd.read_csv(file_path)


# -----------------------------
# Clean Data (Drop Missing Values)
# -----------------------------
def clean_data(df):
    print("\nBefore Cleaning:", len(df))
    df = df.dropna()
    print("After Cleaning:", len(df))
    return df


# -----------------------------
# Email Validation
# -----------------------------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


# -----------------------------
# Remove Invalid Emails
# -----------------------------
def remove_invalid_emails(df):
    df = df[df["email"].apply(is_valid_email)]
    print("After Removing Invalid Emails:", len(df))
    return df


# -----------------------------
# Remove Duplicate Emails
# -----------------------------
def remove_duplicates(df):
    print("Before Removing Duplicates:", len(df))
    df = df.drop_duplicates(subset="email")
    print("After Removing Duplicates:", len(df))
    return df


# -----------------------------
# Calculate Score
# -----------------------------
def calculate_score(skills):
    score = 0
    skills = skills.lower()

    for skill, points in SCORING_RULES.items():
        if skill in skills:
            score += points

    return score


# -----------------------------
# Filter Candidates by Role
# -----------------------------
def filter_by_role(df, role_name):
    return df[df["role"].str.lower() == role_name.lower()]


# -----------------------------
# Skill Frequency Analysis
# -----------------------------
def skill_frequency_analysis(df):
    skill_dict = {}

    for skills in df["skills"]:
        split_skills = skills.split(",")

        for skill in split_skills:
            skill = skill.strip()

            if skill in skill_dict:
                skill_dict[skill] += 1
            else:
                skill_dict[skill] = 1

    return skill_dict


# -----------------------------
# Visualize Skill Distribution
# -----------------------------
def visualize_skills(skill_dict):
    skills = list(skill_dict.keys())
    counts = list(skill_dict.values())

    plt.figure()
    plt.bar(skills, counts)
    plt.xlabel("Skills")
    plt.ylabel("Number of Candidates")
    plt.title("Skill Distribution Among Applicants")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# -----------------------------
# Generate Advanced Report
# -----------------------------
def generate_report(df):

    print("\n========== HIRING INTELLIGENCE REPORT ==========")
    print("\nTotal Applications:", len(df))

    # Add Score Column
    df["Score"] = df["skills"].apply(calculate_score)

    # Rank Candidates
    ranked_df = df.sort_values(by="Score", ascending=False)

    print("\n🏆 Top Ranked Candidates (Overall):")
    print(ranked_df[["name", "role", "Score"]])

    # Role-Based Shortlisting
    print("\n🔎 Role-Based Shortlisting")

    roles = df["role"].unique()

    for role in roles:
        role_df = filter_by_role(ranked_df, role)
        shortlisted = role_df[role_df["Score"] >= 5]

        print(f"\nRole: {role}")
        print(shortlisted[["name", "Score"]])

    # Skill Analysis
    print("\n📊 Skill Frequency Analysis:")
    skill_dict = skill_frequency_analysis(df)
    for skill, count in skill_dict.items():
        print(f"{skill}: {count}")

    visualize_skills(skill_dict)

    # Export Ranked List
    ranked_df.to_csv("ranked_candidates.csv", index=False)
    print("\n📁 Ranked list exported to 'ranked_candidates.csv'")


# -----------------------------
# Main Execution
# -----------------------------
def main():
    df = load_data("applicants.csv")
    df = clean_data(df)
    df = remove_invalid_emails(df)
    df = remove_duplicates(df)
    generate_report(df)


if __name__ == "__main__":
    main()
