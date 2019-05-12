

```python
# The usual preamble
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)
```


```python
# the number of rows and columns
df = pd.read_csv('countries.csv')
print("Cols", len(df.columns))
print("Rows", len(df.index))
```

    Cols 5
    Rows 5



```python
# for every column: the min
df.min(axis=0)
```




    Name        Brazilia
    People      36503097
    Area          301338
    BIP             1529
    Currency         CAD
    dtype: object




```python
# for every column: the max
df.max(axis=0)
```




    Name            Japan
    People      208360000
    Area          9984670
    BIP              4938
    Currency          YEN
    dtype: object




```python
# for every column: the mean
df.mean(axis=0)
```




    People    102786293.6
    Area        3907399.6
    BIP            2716.2
    dtype: float64




```python
# Show the last 4 rows of the data frame.
df.tail(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Show all the row of countries who have "EUR" as currency.
df[df['Currency'] == "EUR"]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Show only "Name" and "Currency" in a new data frame.
new_df = df.copy()[['Name', 'Currency']]
new_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Show only the rows/countries that have more than 2000 BIP
df[df['BIP'] > 2000]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Select all countries with inhabitants between 50 and 150 Mio
df[(df['People'] > 50000000) & (df['People'] < 150000000)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Change the column name "BIP" to "Bip".
df.rename(columns={'BIP': 'Bip'}, inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate the "Bip" sum over all rows
df[['Bip']].aggregate(sum)

```




    Bip    13581
    dtype: int64




```python
# Calculate the average people of all countries.
df[['People']].mean(axis=0)
```




    People    102786293.6
    dtype: float64




```python
# Sort by "Name" alphabetically.
df.sort_values('Name', inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a new data frame from the original where the area is changed as follows: 
#  all countries with > 1000000 get "BIG" and <= 1000000 get "SMALL" in the cell replaced
df2 = df.copy()

df2.loc[df2['Area'].astype(int) <= 1000000, 'Area'] = "1"
df2.loc[df2['Area'].astype(int) > 1000000,  'Area'] = "0"

df2.loc[df2['Area'] == "0",  'Area'] = "BIG"
df2.loc[df2['Area'] == "1", 'Area']  = "SMALL"

df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>BIG</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>BIG</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>SMALL</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>SMALL</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>SMALL</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
