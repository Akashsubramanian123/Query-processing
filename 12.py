import pandas as pd

# Load the data
df = pd.read_csv('random_data.csv')

# Apply background and font colors
styled_df = df.style.set_properties(**{
    'background-color': 'black',
    'color': 'yellow'
})

print("Color theme applied.")
print(df)
# To view with colors, use: styled_df.to_html('styled_theme.html')