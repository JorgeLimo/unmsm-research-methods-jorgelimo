import pandas as pd
import numpy as np
 
np.random.seed(42)
n = 500
n_blocks = 10  # simulates 10 districts
 
block_id = np.repeat(np.arange(n_blocks), n // n_blocks)
np.random.shuffle(block_id)
 
block_center_lat = np.random.uniform(-18.0, -0.5, n_blocks)
block_center_lon = np.random.uniform(-81.0, -69.0, n_blocks)
lat = block_center_lat[block_id] + np.random.normal(0, 0.05, n)
lon = block_center_lon[block_id] + np.random.normal(0, 0.05, n)
 
df = pd.DataFrame({
    'block_id':        block_id,
    'lat':             lat,
    'lon':             lon,
    'ndvi':            np.random.uniform(0.1, 0.9, n),
    'temperature':     np.random.uniform(18, 32, n),
    'precipitation':   np.random.uniform(50, 400, n),
    'forest_loss':     np.random.uniform(0, 1, n),
    'bat_occurrence':  np.random.randint(0, 10, n),
    'population_density': np.random.uniform(1, 500, n),
    'dist_to_forest':  np.random.uniform(0, 50, n),
    'target':          np.random.randint(0, 2, n)  # 1=riesgo alto, 0=riesgo bajo
})
 
df.to_csv('data/rabies_data.csv', index=False)
print(f"Dataset created: {len(df)} records, {df['target'].sum()} positive cases, {n_blocks} spatial blocks")