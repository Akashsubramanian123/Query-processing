import pandas as pd
import numpy as np

# Create 10x4 DataFrame with random values
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# Function to define colors
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply styling
styled_df = df.style.map(color_negative_red)

print("DataFrame (Original):")
print(df)
print("\nStyling has been applied. If running in a script, use styled_df.to_html('output.html') to view colors.")