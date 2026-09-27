from sklearn.datasets import fetch_california_housing

# Download California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Get the complete dataset
df = housing.frame

# Save as CSV
df.to_csv("california_housing.csv", index=False)

print("California Housing dataset downloaded successfully!")
print("Dataset shape:", df.shape)
print(df.head())