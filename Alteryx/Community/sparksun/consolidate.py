from ayx import Package
from ayx import Alteryx
import pandas as pd

# 入力データの取得
input_paths = Alteryx.read("#1")
output_path = Alteryx.read("#2")['OutputPath'][0]

# 空の DataFrame を作成
df_all = pd.DataFrame()

# 各ファイルの各シートを読み込み、DataFrame に追加
for path in input_paths['FullPath']:
    # Excel ファイルを開く
    with pd.ExcelFile(path) as xlsx:
        # 各シートを DataFrame に読み込み、空の DataFrame に結合
        for sheet_name in xlsx.sheet_names:
            df_temp = pd.read_excel(xlsx, sheet_name=sheet_name)
            df_all = pd.concat([df_all, df_temp], ignore_index=True)

# 出力ファイルに書き込み
df_all.to_excel(output_path, index=False)