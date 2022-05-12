import pandas as pd


authors = pd.read_csv('assets/author_genders.csv')
locations = pd.read_csv('assets/locations.csv')
merged = pd.merge(locations,
                  authors[['pmid', 'first_authors_gender', 'last_authors_gender']],
                  on='pmid', how='inner')

gender_ratio_data_year = []
for country in merged.country.unique():
    for year in merged.query('country==@country').year.unique():
        data_slice = merged.query('country==@country and year==@year')
        data = {
            'country': country,
            'year': year,
            'iso': data_slice.iso3.values[0],
            'total_papers': data_slice.shape[0],
            'sum_male_first_authors': sum(data_slice.first_authors_gender=='male'),
            'sum_female_first_authors': sum(data_slice.first_authors_gender=='female')
        }
        gender_ratio_data_year.append(data)
gender_ratio_year_table = pd.DataFrame(gender_ratio_data_year)
gender_ratio_year_table['ratio'] = (gender_ratio_year_table.sum_female_first_authors /
                                    gender_ratio_year_table.sum_male_first_authors)
gender_ratio_year_table['ratio'].fillna(0, inplace=True)

gender_ratio_year_table.to_csv('assets/gender_ratio_table.csv', index=False)