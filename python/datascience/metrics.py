import pandas as pd
import numpy as np

#Returns number of cells in dataframe that are missing in percent
def calc_missing_values(df: pd.Series) -> float:
  missing_per_column: pd.Series = df.isnull().sum()
  total_missing: int = missing_per_column.sum()
  total_number_cells = np.product(df.shape)
  return total_missing / total_number_cells
