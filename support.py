import wbgapi as wb
import pandas as pd

for lame in wb.data.fetch('EG.ELC.ACCS.ZS','BEN'):
    print(lame)