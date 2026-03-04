import pandas as pd

# Load the data
df = pd.read_csv('random_data.csv')

# Highlight NaN values
def highlight_nan(val):
    color = 'red' if pd.isna(val) else ''
    return f'background-color: {color}'

# Apply styling (View in Jupyter or export to HTML)
styled_df = df.style.applymap(highlight_nan)

print("DataFrame loaded. NaN values have been styled.")
print(df)
# To view with colors, use: styled_df.to_html('highlight_nan.html')