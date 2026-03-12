import pandas as pd

# Load all three files
dfs = [pd.read_csv(f'data/daily_sales_data_{i}.csv') for i in range(3)]
df = pd.concat(dfs)

# Filter for Pink Morsels only
df = df[df['product'] == 'pink morsel']

# Calculate sales (remove dollar sign from price first)
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = df['price'] * df['quantity']

# Keep only required columns
df = df[['sales', 'date', 'region']]

# Save output
df.to_csv('data/output.csv', index=False)
print('Done! Here is a preview:')
print(df.head())
print(f'Total rows: {len(df)}')
