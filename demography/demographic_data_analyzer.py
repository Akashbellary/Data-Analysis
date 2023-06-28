import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    df['count']=1
    race_count=df.groupby(['race']).count()['count']

    # What is the average age of men?
    average_age_men = df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors=df['education'].str.contains('Bachelors').sum()
    total_edu=df['education'].count()
    percentage_bachelors = (bachelors/total_edu)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df['education'].str.contains(('Bachelors|Masters|Doctorate')).sum()
    lower_education = (df['education'].count())-(df['education'].str.contains(('Bachelors|Masters|Doctorate')).sum())

    # percentage with salary >50K
    higher_education_count = len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])
    higher_education_rich_count = len(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')])

    lower_education_count = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    lower_education_rich_count = len(df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & (df['salary'] == '>50K')])

    higher_education_rich = (higher_education_rich_count / higher_education_count) * 100
    lower_education_rich = (lower_education_rich_count / lower_education_count) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_per_week = df['hours-per-week'].min()
    min_workers_df = df[df['hours-per-week'] == min_hours_per_week]
    rich_min_workers_count = len(min_workers_df[min_workers_df['salary'] == '>50K'])

    num_min_workers = len(min_workers_df)
    rich_percentage = (rich_min_workers_count / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    high_earning_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    earning_percentages = (high_earning_counts / country_counts) * 100
    highest_earning_country = earning_percentages.idxmax()
    highest_earning_country_percentage = earning_percentages.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners_df = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = india_high_earners_df['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
