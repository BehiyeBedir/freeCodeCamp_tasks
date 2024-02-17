import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Load the data
df = pd.read_csv('medical_examination.csv')

# Add overweight column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Create catplot
def draw_cat_plot():
    # Create DataFrame for cat plot using melt
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to get the counts
    df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    # Draw the catplot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # Do not modify the next two lines
    plt.savefig('catplot.png')
    return fig

# Clean the data
df = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

# Create correlation matrix
corr = df.corr()

# Generate a mask for the upper triangle
mask = (corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))).abs() >= 0.0

# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 8))

# Draw the heatmap with the mask
sns.heatmap(corr, annot=True, fmt='.1f', cmap='coolwarm', mask=mask, square=True, linewidths=.5, center=0, cbar_kws={"shrink": 0.75})

# Do not modify the next two lines
plt.savefig('heatmap.png')
plt.show()
