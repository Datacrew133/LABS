import pandas
import numpy as np
def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    # Your code here 
    results = []
    numeric_df = df.select_dtypes(include="number")

    for col in numeric_df.columns:
        if numeric_df[col].nunique() <= 2:
            continue  # skip binary/flag columns

        skew_val = numeric_df[col].skew()
        min_val = numeric_df[col].min()

        # Direction
        direction = 'Right' if skew_val > 0 else 'Left'

        # Degree
        if abs(skew_val) <= 0.5:
            degree = 'Normal'
        elif abs(skew_val) <= 1:
            degree = 'Moderately Skewed'
        else:
            degree = 'Highly Skewed'

        # Recommended transformation
        if degree == 'Normal':
            recommendation = 'None'
        elif min_val > 0:
            recommendation = 'Box-Cox'
        elif min_val == 0:
            recommendation = 'Log Plus One'
        else:
            recommendation = 'Yeo-Johnson'

        results.append({
            'Feature': col,
            'Skewness': skew_val,
            'Degree': degree,
            'Direction': direction,
            'Recommended Transformation': recommendation
        })

    skew_table= pandas.DataFrame(results)
    return skew_table

