import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

# -----------------------------
# 1. LOGIC LAYER (The functions Test_App needs)
# -----------------------------

SCORING_RULES = {
    "python": 5,
    "machine learning": 5,
    "sql": 3,
    "html": 2,
    "css": 2
}


def is_valid_email(email):
    """Checks if email format is valid."""
    if pd.isna(email):  # Handle NaN/None values
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, str(email)) is not None


def clean_data(df):
    """Removes invalid emails and duplicates."""
    # Drop rows where email is totally missing
    df = df.dropna(subset=['email'])

    # Filter for valid email formats
    df = df[df["email"].apply(is_valid_email)]

    # Remove duplicates
    df = df.drop_duplicates(subset="email")
    return df


def calculate_score(skills):
    """Calculates score based on keywords in skills string."""
    score = 0
    if pd.isna(skills):
        return 0
    skills = str(skills).lower()

    for skill, points in SCORING_RULES.items():
        if skill in skills:
            score += points
    return score


def skill_frequency_analysis(df):
    """Counts frequency of each skill."""
    skill_dict = {}

    for skills in df["skills"]:
        if pd.isna(skills):
            continue
        split_skills = str(skills).split(",")

        for skill in split_skills:
            skill = skill.strip()
            if skill in skill_dict:
                skill_dict[skill] += 1
            else:
                skill_dict[skill] = 1
    return skill_dict


# -----------------------------
# 2. UI LAYER (The Web Dashboard)
# -----------------------------
# This block ensures the UI only runs when executing 'streamlit run',
# not when importing functions for testing.

if __name__ == "__main__":
    st.set_page_config(page_title="Hiring Intelligence System")
    st.title("🚀 Internship Hiring Intelligence System")

    uploaded_file = st.file_uploader("Upload Applicants CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.subheader("Raw Data")
        st.dataframe(df)

        # CALL THE FUNCTIONS WE DEFINED ABOVE
        df = clean_data(df)

        # Apply Scoring
        df["Score"] = df["skills"].apply(calculate_score)

        # Sort
        ranked_df = df.sort_values(by="Score", ascending=False)

        st.subheader("🏆 Ranked Candidates")
        st.dataframe(ranked_df)

        st.subheader("🔎 Role-Based Filter")
        if "role" in ranked_df.columns:
            role = st.selectbox("Select Role", ranked_df["role"].unique())
            role_df = ranked_df[ranked_df["role"] == role]
            st.dataframe(role_df)

        st.subheader("📊 Skill Distribution")
        skill_dict = skill_frequency_analysis(df)

        if skill_dict:
            fig, ax = plt.subplots()
            ax.bar(skill_dict.keys(), skill_dict.values())
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)

        st.download_button(
            label="Download Ranked Candidates",
            data=ranked_df.to_csv(index=False),
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )