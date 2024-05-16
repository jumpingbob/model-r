import pandas as pd
from pycaret.classification import load_model
model = load_model('path_to_your_model.pkl')
feature_importance = model.feature_importances_
df_feature_importance = pd.DataFrame({'Feature': model.feature_names_, 'Importance': feature_importance})
