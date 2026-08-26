import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# 1. Create a dummy dataset (Square Footage, Number of Bedrooms -> Price)
data = {
    'sqft': [1500, 2000, 2500, 1200, 3000, 1800, 2200],
    'beds': [3, 4, 4, 2, 5, 3, 4],
    'price': [300000, 450000, 500000, 250000, 600000, 360000, 480000]
}

df = pd.DataFrame(data)

# 2. Separate Features (X) and Target (y)
X = df[['sqft', 'beds']]
y = df['price']

# 3. Train the Model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully.")

# 4. Save the Model
# We save it in the parent directory so the backend can easily access it, or just in the current dir.
# Let's save it in the backend folder so the API can load it directly.
backend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backend')
os.makedirs(backend_dir, exist_ok=True)
model_path = os.path.join(backend_dir, 'model.pkl')

joblib.dump(model, model_path)
print(f"Model saved to {model_path}")
