# analyze_survey_data.py
# Simple analysis of survey responses about coffee preferences
# Author: Your Name
# Date: September 2025

import pandas as pd
import matplotlib.pyplot as plt

# Load the survey data
data = pd.read_csv('coffee_survey_responses.csv')

# Basic descriptive statistics
print("Survey Response Summary:")
print(f"Total responses: {len(data)}")
print(f"Average cups per day: {data['cups_per_day'].mean():.1f}")
print(f"Most popular brewing method: {data['brewing_method'].mode()[0]}")

# Create a simple visualization
plt.figure(figsize=(8, 6))
data['brewing_method'].value_counts().plot(kind='bar')
plt.title('Coffee Brewing Method Preferences')
plt.xlabel('Brewing Method')
plt.ylabel('Number of Responses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('brewing_methods.png', dpi=300)
plt.show()

# Test for correlation between cups per day and satisfaction
correlation = data['cups_per_day'].corr(data['satisfaction_score'])
print(f"\nCorrelation between daily cups and satisfaction: {correlation:.3f}")

# Save results to a summary file
results = {
    'total_responses': len(data),
    'avg_cups_per_day': data['cups_per_day'].mean(),
    'most_popular_method': data['brewing_method'].mode()[0],
    'cups_satisfaction_correlation': correlation
}

with open('analysis_results.txt', 'w') as f:
    f.write("Coffee Survey Analysis Results\n")
    f.write("="*30 + "\n")
    for key, value in results.items():
        f.write(f"{key}: {value}\n")

print("\nAnalysis complete! Results saved to analysis_results.txt")
print("Chart saved as brewing_methods.png")
