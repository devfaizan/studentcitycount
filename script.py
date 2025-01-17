import pandas as pd 
import matplotlib.pyplot as plt 

sauce = pd.read_csv('datancaec.csv')
# Correct user input for specfic city
corrections = {
    'RWP': 'Rawalpindi',
    'Rwp': 'Rawalpindi',
    'Rawalapindi': 'Rawalpindi',
    'RAWALPINDI': 'Rawalpindi',
    'Rawallpindi': 'Rawalpindi',
    'Rawalpindi punjab': 'Rawalpindi',
    'ISB': 'Islamabad',
    'Islamabad Capital Territory': 'Islamabad',
    ' Islamabad Capital Territory': 'Islamabad',
    'FEDERAL AREA': 'Islamabad', 
    'Federal': 'Islamabad',
    'Federal ': 'Islamabad',
    'Sheikapura': 'Sheikhupura',
    'FAISALABAD': 'Faislabad',
    'ABBOTTABAD': 'Abbottabad',
    'Toba Tek singh': 'Toba Tek Singh',
}
# relpace with correct values 
corrected_values = sauce['Domicile DISTRICT'].replace(corrections)
corrected_values = corrected_values.dropna()
# strip spaces and make first letter capital
capitalized_values = [value.strip() for value in corrected_values if isinstance(value, str) and value.strip() and value.strip()[0].isupper()]
# list goes to series to use unique
capitalized_values_series = pd.Series(capitalized_values)
unique_values = capitalized_values_series.unique()
city_counts = capitalized_values_series.value_counts()

plt.figure(figsize=(12, 8))
ax = city_counts.plot(kind='barh', color='#e3e3e3')
ax.set_facecolor('#121212')
plt.gcf().set_facecolor('#e0e0e0')
plt.title('Number of CS Students from Different Cities Batch 2016-2024')
plt.xlabel('Number of Students')
plt.ylabel('Cities')
# plt.xticks(rotation=90, ha='right')
plt.subplots_adjust(bottom=0.25)

for container in ax.containers:
    ax.bar_label(container, label_type='edge', color='white')
plt.tight_layout()
plt.show()
print("Number of students from each city:")
for city, count in city_counts.items():
    print(f"{city} = {count}")