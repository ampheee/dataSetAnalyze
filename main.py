import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')


# plt.style.use('dark_background')

df = pd.read_csv('/kaggle/input/diabetes-dataset/diabetes.csv')
df.head()

df.describe()

# df['Outcome'].value_counts()

# df.groupby('Outcome').mean()

# X = df.drop(columns = 'Outcome', axis=1)
# Y = df['Outcome']

# print(X)
# print(Y)

def plots(df, variable):
    plt.figure(figsize=(22, 4), dpi=200)

    # histogram
    ax = plt.subplot(1, 3, 1)
    sns.kdeplot(df[variable], color='Red', fill=True)
    ax.set_title("Density Plot", fontsize=15, fontweight='normal', fontfamily='serif')
    plt.ylabel('Density', fontfamily='serif')
    plt.xlabel(variable, fontfamily='serif')
    for s in ['top', 'left', 'right']:
        ax.spines[s].set_visible(False)

plots(df, 'BloodPressure')

plt.figure(figsize=(20, 5))
sns.kdeplot('BloodPressure', hue='Outcome', data=df, palette='Set2')
plt.show()

print('\n')

plots(df, 'Glucose')

plt.figure(figsize=(20, 5))
sns.kdeplot('Glucose', hue='Outcome', data=df, palette='Set2')
plt.show()

print('\n')

plots(df, 'SkinThickness')

plt.figure(figsize=(20, 5))
sns.kdeplot('SkinThickness', hue='Outcome', data=df, palette='Accent')
plt.show()

print('\n')

plots(df, 'Insulin')

plt.figure(figsize=(20, 5))
sns.kdeplot('Insulin', hue='Outcome', data=df, palette='Accent')
plt.show()

print('\n')

plots(df, 'BMI')def plots(df, variable):
    plt.figure(figsize=(22, 4), dpi=200)

    # histogram
    ax = plt.subplot(1, 3, 1)
    sns.kdeplot(df[variable], color='Red', fill=True)
    ax.set_title("Density Plot", fontsize=15, fontweight='normal', fontfamily='serif')
    plt.ylabel('Density', fontfamily='serif')
    plt.xlabel(variable, fontfamily='serif')
    for s in ['top', 'left', 'right']:
        ax.spines[s].set_visible(False)

plots(df, 'BloodPressure')

plt.figure(figsize=(20, 5))
sns.kdeplot('BloodPressure', hue='Outcome', data=df, palette='Set2')
plt.show()

print('\n')

plots(df, 'Glucose')

plt.figure(figsize=(20, 5))

plt.figure(figsize=(20, 5))
sns.kdeplot('BMI', hue='Outcome', data=df, palette='Accent')
plt.show()

print('\n')

plots(df, 'Age')

plt.figure(figsize=(20, 5))
sns.kdeplot('Age', hue='Outcome', data=df, palette='Accent')
plt.show()

