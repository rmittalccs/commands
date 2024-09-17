The RFECV object itself doesn't directly expose feature_importances_, but since you're using XGBRegressor as the estimator, 
you can access the feature importance of the model (after fitting) via the underlying model stored in the estimator_ attribute of RFECV.
Here’s how you can retrieve the feature importance after performing RFE using XGBRegressor:

# Assuming you have completed the RFE process
# Access the fitted estimator (XGBRegressor) from RFECV
xgb_model = rfe.estimator_

# Now you can get the feature importances
importances = xgb_model.feature_importances_

# If you want to associate these importance scores with the selected features:
selected_features = X_train.columns[rfe.get_support()]

# Create a DataFrame to view feature names alongside their importance scores
import pandas as pd
importance_df = pd.DataFrame({
    'Feature': selected_features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Display the DataFrame
print(importance_df)
