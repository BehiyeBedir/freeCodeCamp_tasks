import pandas as pd

# Read csv
file_path = r"C:\Users\BEHİYE BEDİR\Desktop\adult.csv"
data = pd.read_csv(file_path)

# Races
race = data["race"].value_counts()

# Average age of men
data_men = data[data["sex"] == "Male"]
age_average = data_men["age"].mean()

# Bachelor's degree percentage
bachelors_degree = data[data['education'] == 'Bachelors']
bachelors_percentage = (len(bachelors_degree) / len(data)) * 100

# People with advanced education earning more than 50k
advanced_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_income_advanced_education = advanced_education[advanced_education['income'] == '>50K']
percentage_high_income_advanced_education = (len(high_income_advanced_education) / len(advanced_education)) * 100

# People without advanced education but earning more than 50k
no_advanced_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
high_income_no_advanced_education = no_advanced_education[no_advanced_education['income'] == '>50K']
percentage_no_advanced_education_high_income = (len(high_income_no_advanced_education) / len(no_advanced_education)) * 100

# Minimum hours a person works per week
min_working_hours = data["hours.per.week"].min()

# Percentage of minimum working hours earners with income >50k (assuming minimum working hours as 40)
minimum_working_hours_earners = data[data['hours.per.week'] == 40]
high_income_minimum_working_hours_earners = minimum_working_hours_earners[minimum_working_hours_earners['income'] == '>50K']
percentage_minimum_working_hours_high_income = (len(high_income_minimum_working_hours_earners) / len(minimum_working_hours_earners)) * 100

# Country with the highest percentage of people earning more than 50k
high_income = data[data['income'] == '>50K']
country_percentages = (high_income['native.country'].value_counts() / data['native.country'].value_counts()) * 100
highest_percentage_country = country_percentages.idxmax()
highest_percentage = country_percentages.max()

# Most popular occupation for people earning >50k in India
india_high_income = data[(data['native.country'] == 'India') & (data['income'] == '>50K')]
most_popular_occupation = india_high_income['occupation'].mode().values[0]

# Print the results
print("How many people represent each race?:")
print(race)
print("---------------------------------------------------------------")
print("Average age of men:", age_average)
print("Percentage of people with a Bachelor's degree:", bachelors_percentage)
print("Percentage of people with advanced education earning more than 50k:", percentage_high_income_advanced_education)
print("Percentage of people without advanced education earning more than 50k:", percentage_no_advanced_education_high_income)
print("Minimum working hours per week for a person:", min_working_hours)
print("Percentage of minimum working hours earners with income >50k:", percentage_minimum_working_hours_high_income)
print(f"Country with the highest percentage of people earning more than 50k: {highest_percentage_country}")
print(f"Percentage of high-income earners in this country: {highest_percentage:.2f}%")
print(f"Most popular occupation for people earning >50k in India: {most_popular_occupation}")
