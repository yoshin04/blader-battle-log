import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# データベース接続設定
engine = create_engine('postgresql://bbl_user:local@db:5432/bbl_db')

# データの読み込み
df = pd.read_sql('SELECT * FROM matches', engine)

# データの分析
win_rate = df[df['result'] == 'win'].shape[0] / df.shape[0]

# データの可視化
plt.figure(figsize=(10, 6))
sns.countplot(x='player', hue='result', data=df)
plt.title('Player Win/Loss Count')
plt.show()

print(f'Win rate: {win_rate:.2f}')
