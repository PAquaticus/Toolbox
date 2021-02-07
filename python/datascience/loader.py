import pandas as pd
import numpy as np
import datatable as dt

"""
This is about 20 times faster for really big (~5 GB) .csv files
https://www.kaggle.com/pabawid/jane-street-eda-of-day-0-and-feature-importance/edit
"""
def load_huge_csv(filepath: string) -> pd.Series:
  table = dt.fread(filepath)
  df: pd.Series = table.to_pandas()
  return df