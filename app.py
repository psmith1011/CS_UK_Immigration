import streamlit as st
import pandas as pd
import geopandas as gpd
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Global variables

# Function to load data
def load_data1():
    # Load your data from a CSV file, for example
    df = pd.read_csv(r'C:\Users\patri\OneDrive\Documents\Brainstation\df_reduced_nat.csv')
    return df

# Load the data and assign to df_nat
df_nat = load_data1()  # This should be a DataFrame now

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
image_welcome = Image.open('C:/Users/patri/OneDrive/Documents/Brainstation/the-wrong-trousers1.png')


def home_page():
    st.title("Welcome to the UK Immigration Data Analysis App!")
    st.image(image_welcome, caption='Wallace & Gromit Welcome You to the UK', use_column_width=True)
    st.write("This app provides insights into immigration applications, decisions, and outcomes.")
    st.markdown("### Those Affected")
    st.markdown("- How to work this app:")
    st.markdown("    - Use the sidebar to navigate between different sections.")
    st.markdown("    - The 'Home' page provides an overview of the app.")
    st.markdown("    - The 'Data Info' page describes the dataset columns.")
    st.markdown("    - The 'Project Overview' page provides a summary of the project.")
    st.markdown("    - The 'General Data Info' page repeats the dataset column information.")
    st.markdown("    - The 'Visualizations' page displays interactive visualizations.")
    st.markdown("""

    

                
        Note: You can use the first sidebar to include a fixed graph or map, in addition to the 2nd sidebar
                
        ### Those Affected

        **Target Groups:**
        - Individuals contemplating immigration among multiple country options, assisting in decision-making about where they might have the best opportunities.
        - Organizations, policymakers, and researchers interested in immigration trends, policy impacts, and integration processes.

        ## Potential Impact

        **Benefits of the Model:**
        - Provides a decision-support tool for potential immigrants evaluating their options, offering insights into the likelihood of successful immigration processes.
        - Enhances policymaking with data-driven insights, allowing for the formulation of more effective and transparent immigration policies.
        - Contributes societal value by deepening the understanding of immigration dynamics, which can improve integration strategies and overall policy decisions impacting immigrants.

        ## Summary

        - We have combined data from 15 Excel files sourced from the UK government, encompassing over 1.5 million rows and 47 columns featuring strings, floats, and integers.
        - This comprehensive dataset covers various aspects of immigration and citizenship, providing insights into trends and patterns.
        - These datasets cover various timeframes and categories, with some files sharing similar columns while others span different date ranges, from 2001 to 2023.
    """)
    st.dataframe(df_nat.sample(10))
    st.markdown(f"## This is a sample of our dataset, which includes {df_nat.shape[0]} rows and {df_nat.shape[1]} columns.")

def dataset_info():
    st.title("Dataset Information")
    st.markdown("""

    This is a breakdown of all the main columns of interest in our UK Immigration Database
                
        | Column             | Descriptor                                                                                              | Datatype |
        |--------------------|---------------------------------------------------------------------------------------------------------|----------|
        | Year               | Year in which the event occurred, including initial decisions or resettlements.                         | int      |
        | Quarter            | Quarter of the year in which the event occurred (Q1, Q2, Q3, Q4).                                       | object   |
        | Nationality        | Nationality of the individual involved in the immigration process.                                      | object   |
        | Region             | World region of the individual's country of nationality.                                                | object   |
        | Age                | Age of the individual at the time of the event.                                                         | int      |
        | Sex                | Gender of the individual (Male, Female, Other).                                                         | object   |
        | Visa type group    | Grouped category of the visa applied for, describing the general purpose (e.g., work, study, family).   | object   |
        | Visa type          | Specific type of visa applied for within the grouped category.                                          | object   |
        | Visa type subgroup | Detailed classification of visa type, providing further specifics within the visa category.             | object   |
        | Applications       | Number of applications filed.                                                                           | int      |
        | Case outcome       | Outcome of the immigration case (granted, refused, withdrawn, etc.).                                    | object   |
        | Decisions          | Number of decisions made in cases.                                                                      | float64  |                                                                         
        | Occupation         | Occupation of the individual associated with the visa application.                                      | object   |
        | Industry           | Industry sector relevant to the visa application.                                                       | object   |
        | General_Region     | General geographical region in the UK associated with the immigration case.                             | object   |
    """)

def Population_UK():
    st.title("Population of the UK (71-21)")
    st.markdown("""
                
### Population of the United Kingdom 1971-2021

|                | 1971  | 1981  | 1991  | 2001  | 2011  | 2021  |
|----------------|-------|-------|-------|-------|-------|-------|
| All People     | 52.6M | 53.6M | 54.9M | 57.1M | 63.3M | 67.0M |
| Born Abroad    | 3.2M  | 3.4M  | 3.8M  | 4.9M  | 8.0M  | 9.5M |
| % T            | 5.1%  |  6.3%  | 6.9%  | 8.6% | 12.6%  | 14.1% |
| % Δ Decade     | 24.0%  | 7.5%  | 11.8%  | 27.7% | 63.0% | 18.6% |

As of 2021, the population of foreign-born habitants in the UK has risen to 9.5M, ~14% of the total population. 

Given the limited land space in the UK, the ongoing increase in population density might raise challenges related to infrastructure, housing, and public services. The UK has a limited amount of space available at ~250,000 square km. To put it in perspective, Canada, one of the largest countries in the world by landmass, is ~10 million square km.

The steady rise in the population born abroad in the UK suggests that immigration will continue to play a crucial role in the country's demographic dynamics. These factors necessitate continued attention and effective policy-making to manage the implications of a growing and increasingly diverse population.
    """)


def plot_map():
    # Load the data
    df_nat = load_data1()
    # Get a list of all unique years
    years = sorted(df_nat['Year'].unique())
    # Create a slider for selecting a year
    selected_year = st.slider('Select a year', min_value=min(years), max_value=max(years), value=min(years))
    # Filter the data based on the selected year
    df_year = df_nat[df_nat['Year'] == selected_year]
    # Group by nationality and sum the 'Decisions'
    sums = df_year.groupby('Nationality')['Decisions'].sum()
    # Convert the sums to a DataFrame
    df_sums = pd.DataFrame({'Country': sums.index, 'Decisions': sums.values})
    # Merge the GeoDataFrame with the sums DataFrame
    merged = world.set_index('name').join(df_sums.set_index('Country'))
    # Fill NaN values with 0 for areas without data
    merged['Decisions'] = merged['Decisions'].fillna(0)
    # Plot the map using matplotlib
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    merged.plot(column='Decisions', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True, scheme='quantiles')
    plt.title(f'Immigration to the UK in {selected_year} - Global Amount of Applications')
    plt.axis('off')
    st.pyplot(fig)


def plot_visualizations():
    load_data1()

    # Get a list of all unique nationalities
    nationalities = df_nat['Nationality'].unique()

    # Create a dropdown menu with the nationalities
    selected_nationality = st.selectbox('Select a nationality', nationalities)

    # Get a list of all unique case outcomes
    case_outcomes = df_nat['Case outcome'].unique()

    # Create a dropdown menu with the case outcomes
    selected_case_outcome1 = st.selectbox('Select a case outcome', case_outcomes)

    # Create another dropdown menu with the case outcomes for comparison
    case_outcomes2 = np.append(case_outcomes, 'None')
    selected_case_outcome2 = st.selectbox('Select another case outcome for comparison (or select "None")', case_outcomes2)

    # Filter the data based on the selected nationality and case outcomes
    if selected_case_outcome2 == 'None':
        filtered_df = df_nat[(df_nat['Nationality'] == selected_nationality) & (df_nat['Case outcome'] == selected_case_outcome1)]
    else:
        filtered_df = df_nat[(df_nat['Nationality'] == selected_nationality) & (df_nat['Case outcome'].isin([selected_case_outcome1, selected_case_outcome2]))]

    # Group filtered data by 'Year' and 'Case outcome' and sum the 'Decisions'
    grouped_sums = filtered_df.groupby(['Year', 'Case outcome'])['Decisions'].sum().unstack(fill_value=0)

    # Plot the data
    fig, ax = plt.subplots(figsize=(16, 8))
    grouped_sums.plot(kind='bar', stacked=False, ax=ax)
    plt.title(f'Case Outcomes for Nationality "{selected_nationality}" Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Decisions')
    plt.legend(title='Case Outcome', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()

    st.pyplot(fig)


def plot_case_outcome_over_time():
    df_nat = load_data1()  # Load the data
    df_nat['Date'] = pd.to_datetime(df_nat['Date'])  # Convert the 'Date' column to datetime
    df_nat = df_nat.sort_values('Date')  # Sort the data by date

    # Group by 'Date' and 'Case Outcome', and sum 'Decisions'
    outcome_over_time = df_nat.groupby(['Date', 'Case Outcome'])['Decisions'].sum().reset_index()

    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Date', y='Decisions', hue='Case Outcome', data=outcome_over_time)
    plt.title('Case Outcome Counted by Decisions Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Decisions')
    plt.tight_layout()
    st.pyplot(plt)

def plot_top_industry_counts():
    # Load the data
    df_nat = load_data1()

    # Count the occurrences of each industry
    industry_counts = df_nat['Industry'].value_counts().head(10)

    # Plot
    plt.figure(figsize=(12, 8))
    sns.barplot(x=industry_counts.values, y=industry_counts.index, orient='h')
    plt.title('Top 10 Industries')
    plt.xlabel('Count')
    plt.ylabel('Industry')
    plt.tight_layout()
    st.pyplot(plt)


# Create a sidebar for navigation
navigation_one = st.sidebar.selectbox('Pre-Made Graphs and Maps', ['UK Timeline (2001-2022)', 'Case Outcome Over Time', 'Top 10 Nationalities', 'Top 10 Industries', 'Map',])

if navigation_one == 'UK Timeline (2001-2022)':
    # Load the image
    image = Image.open('C:/Users/patri/OneDrive/Documents/Brainstation/UK.png')
    st.image(image, caption='UK Timeline (2021-2022)')
    Population_UK()
elif navigation_one == 'Top 10 Nationalities':
    load_data1()

    # Filter to include only the top 50 nationalities
    top_10_nationalities = df_nat['Nationality'].value_counts().head(10).index
    filtered_df = df_nat[df_nat['Nationality'].isin(top_10_nationalities)]

    # Set the size of the plot
    plt.figure(figsize=(12, 8))

    sns.countplot(y='Nationality', data=filtered_df, order=filtered_df['Nationality'].value_counts().index)

    plt.title('Top 10 Nationalities')
    plt.xlabel('Count')
    plt.ylabel('Nationality')
    plt.tight_layout()
    st.pyplot(plt)
elif navigation_one == 'Case Outcome Over Time':
    plot_case_outcome_over_time()
elif navigation_one == 'Top 10 Industries':
    plot_top_industry_counts()
elif navigation_one == 'Map':
    plot_map()



# Helper function to load images
def load_image(image_path):
    return Image.open(image_path)

# Data structure to hold questions, answers, and image paths
immigration_info = {
    "What is a Tier 2 Visa?": {
        "answer": "A Tier 2 Visa allows skilled workers to enter the UK to take up employment.",
        "image": "C:/Users/patri/OneDrive/Documents/path_to_tier2_visa_image.jpg"
    },
    "How to apply for UK citizenship?": {
        "answer": "You can apply for UK citizenship after living in the UK for five years and holding Indefinite Leave to Remain (ILR) for at least one year.",
        "image": "C:/Users/patri/OneDrive/Documents/path_to_citizenship_info_image.jpg"
    },
    "What sports did the United Kingdom invent?": {
        "answer": "Soccer, rugby, golf, boxing, and cricket were ALL invented in the United Kingdom",
        "image": "C:/Users/patri/OneDrive/Documents/soccer.jpg"
    },
    "What percentage of the global population lives outside their country of birth? How does the UK compare?": {
        "answer": "3.6%\n\nUsually people guess much higher. The fact is that there are many closed off countries than the average person expects, especially those from North America or Western Europe.\n\nThe UK, with its rich history of immigration, stands as a prime example of a diverse and multicultural society shaped significantly by its immigrant population.",
        "image": "C:/Users/patri/OneDrive/Documents/path_to_global_population_image.jpg"
    },
    "Where do fish and chips come from?": {
        "answer": "Jewish Refugees from Portugal\n\nFish and chips, a quintessential British dish, surprisingly has its roots elsewhere. Introduced by Jewish refugees from Portugal in the 16th century, this dish became a national staple in the UK. The refugees brought the tradition of frying fish, which later merged with chips (fries), a popular food among the working class in the UK. The fusion has become a beloved symbol of British food culture.",
        "image": "C:/Users/patri/OneDrive/Documents/path_to_fish_and_chips_origin_image.jpg"
    },
    "The British are known for their tea. Where did tea originate from?": {
        "answer": "East Asia (mostly China)\n\nAlthough tea is synonymous with British culture, it originally comes from East Asia, primarily China. It was introduced to Britain in the 17th century by the East India Company and has since become a deeply ingrained part of British culture, influencing social habits and becoming a national symbol.",
        "image": "C:/Users/patri/OneDrive/Documents/path_to_tea_origin_image.jpg"
    }
}

def display_faq():
    st.sidebar.title("UK Immigration FAQs")
    selected_question = st.sidebar.selectbox("Choose a question", list(immigration_info.keys()))
    answer = immigration_info[selected_question]["answer"]
    image_path = immigration_info[selected_question]["image"]
    
    st.subheader("Answer")
    st.write(answer)
    image = load_image(image_path)
    st.image(image, caption="Relevant Image", use_column_width=True)


# Prepare and train model
def prepare_and_train_model(df):
    # Assuming 'Case outcome' is a column in df with categories ['Refused', 'Study Visa Issued', 'Asylum Case']
    # Encoding categorical data
    le = LabelEncoder()
    df['Nationality'] = le.fit_transform(df['Nationality'])
    df['Case outcome'] = le.fit_transform(df['Case outcome'])
    
    features = ['Nationality', 'Age', 'Sex']  # Example feature set
    X = df[features]
    y = df['Case outcome']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    joblib.dump(model, 'immigration_decision_tree.pkl')
    return model, le

# Prediction function
def predict_outcome(nationality, age, sex, encoder, model):
    # Encoding input data
    nationality_encoded = encoder.transform([nationality])[0]
    sex_encoded = encoder.transform([sex])[0]
    input_data = np.array([nationality_encoded, age, sex_encoded]).reshape(1, -1)
    proba = model.predict_proba(input_data)
    return proba

def main():
    df = load_data()
    model, encoder = prepare_and_train_model(df)

    st.title("UK Immigration Decision Tree Model")

    # User inputs
    nationality = st.selectbox('Select your nationality', df['Nationality'].unique())
    age = st.slider('Select your age', 18, 100, 30)
    sex = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])

    if st.button('Predict Outcome'):
        prediction = predict_outcome(nationality, age, sex, encoder, model)
        st.write(f"Probability of being Refused: {prediction[0][0]:.2f}")
        st.write(f"Probability of Study Visa Issued: {prediction[0][1]:.2f}")
        st.write(f"Probability of Asylum Case Success: {prediction[0][2]:.2f}")

# Home page function
def home_page():
    st.title("Welcome to the UK Immigration Data Analysis App!")
    df = load_data()
    st.dataframe(df.head(10))  # Show a sample of the data
    st.markdown("Explore the app to see visualizations and use the prediction model!")


def main():
    st.sidebar.title("Navigation Menu")
    navigation = st.sidebar.radio("Navigate", ["Home", "Data Info", "Case Outcome Visuals", "FAQ", "Train and Display Model"])

    if navigation == "Home":
        home_page()
    elif navigation == "Data Info":
        dataset_info()
    elif navigation == "Case Outcome Visuals":
        plot_visualizations()
    elif navigation == "FAQ":
        display_faq()
    if navigation == "Train and Display Model":
        st.write("### Immigration Outcome Prediction")
        display_model_performance()
        user_df = user_input_features()
        if st.button('Predict'):
            prediction = model.predict(user_df)
            st.write('### Predicted Outcome:', prediction[0])



if __name__ == "__main__":
    main()