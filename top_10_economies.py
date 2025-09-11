!pip install pandas numpy 
!pip install lxml
import numpy as np
import pandas as pd

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

#Extracts the required GDP data from the given URL using Web Scraping.

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables = pd.read_html(URL)
df = tables[3]
# Replaces the column headers with column numbers
df.columns = range(df.shape[1])

# Retains columns with index 0 and 2
df = df[[0,2]]
# Retains the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[0:10,:]
# Assigns column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)']

# Modifys the GDP column of the DataFrame, converting the value available in Million USD to Billion USD.

df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']],2)
df.rename(columns={'GDP(Billion USD)': 'GDP (Million USD)'})
