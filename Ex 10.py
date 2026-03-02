import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4))

def color(val):
    return 'color:red' if val < 0 else 'color:black'

styled = df.style.applymap(color)

styled