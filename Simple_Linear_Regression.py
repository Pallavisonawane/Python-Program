#Simple Linear Regression
import matplotlib.pyplot as plt
import pandas as pd
slr_df=pd.read_csv("C:\\Users\\I-Net Computer\\Desktop\\DATA SCI ASS\\student_scores.csv")
print("Columns of Dataset:\n:" ,slr_df.columns)
#Display First 5 Records
print(slr_df.head())
#Size of dataset
print(slr_df.shape)
#Get the statistics
print(slr_df.describe())
#scatter plot for complete dataset
plt.scatter(slr_df['Hours'],slr_df['Scores'])
plt.show()

