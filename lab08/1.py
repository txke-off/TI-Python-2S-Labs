import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Revenue'] = df['Quantity']*df['Price']
rev_per_date = df.groupby('Date')['Revenue'].sum().reset_index()
max_rev_date = rev_per_date.loc[
    rev_per_date['Revenue'].idxmax(), 'Date'
]
top = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(3).index.tolist()
filtered = df[df['Quantity']>10]

print(f'Дата с наибольшей выручкой: {max_rev_date}')
print(f'Топ-3 продуктов по количеству продаж: {', '.join(top)}')
print('Отфильтрованные строки:')
print(filtered.to_string(index=False))