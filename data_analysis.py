import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a style for the plots for better visualization
sns.set_theme(style="whitegrid")

# Task 1: Data Loading and Exploration

# Load the Iris dataset from scikit-learn
try:
    iris = load_iris()
    # Create a pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    # Add the species column
    df['species'] = iris.target
    # Replace numerical targets with species names for better readability
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    # Handle the case where the dataset couldn't be loaded
    # In a real-world scenario, you might have a local file
    # and use a try-except block to handle file not found errors.
    # For example: df = pd.read_csv('iris.csv')
    df = None

if df is not None:
    # Display the first few rows
    print("\n--- First 5 rows of the dataset ---")
    print(df.head())

    # Explore the structure and data types
    print("\n--- Dataset Info ---")
    df.info()

    # Check for missing values
    print("\n--- Missing values per column ---")
    print(df.isnull().sum())

    # Since the Iris dataset from sklearn has no missing values,
    # this step is for demonstration purposes. If there were missing values,
    # we would handle them here.
    # Example:
    # df.fillna(df.mean(), inplace=True) # Fill with mean
    # df.dropna(inplace=True) # Drop rows with missing values

    # Task 2: Basic Data Analysis

    # Compute basic statistics of numerical columns
    print("\n--- Basic Statistics of Numerical Columns ---")
    print(df.describe())

    # Perform groupings on the 'species' column and compute the mean
    print("\n--- Mean values per species ---")
    print(df.groupby('species').mean())

    # Findings/Observations from Basic Analysis:
    # - Sepal Length and Sepal Width have similar means across all species, but there are differences.
    # - Petal Length and Petal Width show clear differences across the species.
    #   - 'setosa' has the smallest petals.
    #   - 'virginica' has the largest petals.
    #   - 'versicolor' is in between.
    # - This suggests that petal dimensions are better predictors for distinguishing between species than sepal dimensions.

    # Task 3: Data Visualization

    # Line Chart (not ideal for this dataset, but for demonstration)
    # We can visualize the trend of a feature as we go through the dataset
    plt.figure(figsize=(10, 6))
    plt.plot(df['sepal length (cm)'], label='Sepal Length')
    plt.plot(df['petal length (cm)'], label='Petal Length')
    plt.title('Sepal and Petal Length Trends')
    plt.xlabel('Sample Index')
    plt.ylabel('Length (cm)')
    plt.legend()
    plt.show()

    # Bar Chart: Comparison of average petal length across species
    plt.figure(figsize=(8, 6))
    df_grouped_petal_length = df.groupby('species')['petal length (cm)'].mean().reset_index()
    sns.barplot(x='species', y='petal length (cm)', data=df_grouped_petal_length)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.show()

    # Histogram: Distribution of Petal Length
    plt.figure(figsize=(8, 6))
    sns.histplot(df['petal length (cm)'], kde=True, bins=15)
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter Plot: Relationship between Sepal Length and Petal Length
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title('Sepal Length vs. Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

    # Findings/Observations from Visualizations:
    # - The bar chart and scatter plot confirm the findings from the basic analysis.
    # - The scatter plot shows a very clear separation of the three species based on their sepal and petal lengths.
    # - 'setosa' occupies a distinct cluster with shorter petal lengths and shorter sepal lengths.
    # - 'versicolor' and 'virginica' are more intertwined but still form separate clusters.
    # - The histogram shows a bimodal or trimodal distribution for petal length, which is expected since it is composed of three distinct species with different petal lengths.