import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
import pandas as pd


df_inifian = pd.read_excel(r'data/test.xlsx')
print(df_inifian)
fig,ax = plt.subplots(figsize=(10,6))
ax.plot (df_inifian['data'],df_inifian['time'], '-.' , color='red')
plt.legend(["This is my work"], fontsize="x-large")
plt.show ()