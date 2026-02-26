# GROUPBY
import pandas as pd
df = pd.DataFrame()


df.groupby('col')['val'].sum()                    # Single group, single agg
df.groupby(['A', 'B'])['val'].mean()              # Multiple groups
df.groupby('col').agg(['sum', 'mean'])            # Multiple aggs
df.groupby('col').agg(new_name=('val', 'sum'))    # Named aggregation

# AGG
df['col'].agg('sum')                              # Single function
df['col'].agg(['sum', 'mean'])                    # Multiple functions
df.agg({'A': 'sum', 'B': 'mean'})                 # Per-column functions

# VALUE_COUNTS
df['col'].value_counts()                          # Count frequencies
df['col'].value_counts(normalize=True)            # Percentages
df[['A', 'B']].value_counts()                     # Multi-column counts

# PIVOT_TABLE
df.pivot_table(values='V', index='I', columns='C')       # Basic pivot
df.pivot_table(values='V', index='I', aggfunc='mean')    # Custom agg
df.pivot_table(..., margins=True)                        # With totals