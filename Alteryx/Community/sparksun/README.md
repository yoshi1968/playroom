# Question
I've created 30 excel files in a workflow,each file has a worksheet with formated tables, I want to know how to consolidate all the worksheets into a single excel file.I learned from Chatgpt that VBS or Python code can do it, but I'm not a coding man,anyone know how to run VBS or Python code in Alteryx? Or any other no-code solution?  

I've attached three sample files and my expected result file for clarification of my requirement.

You can see three worksheets in three excel files have been consolided into one excel file while the original worksheet formatting is kept well (I use Visual Basic codes to generate the file).What I want to know is how to use Alteryx workflow to make it happen with Python,Run Command or any other tools or solutions.

[Alteryx\Community\sparksun\1.xlsx]
[Alteryx\Community\sparksun\2.xlsx]
[Alteryx\Community\sparksun\3.xlsx]
[Alteryx\Community\sparksun\output\expected result.xlsx]

# Geminiへの質問

## Q1

from ayx import Package
Package.installPackages(['openpyxl'])
from ayx import Alteryx
import pandas as pd

input_paths = Alteryx.read("#1")
output_path = Alteryx.read("#2")['outputPath'][0]

df_all = pd.DataFrame()

for path in input_paths['FullPath']:
    # Open Excel files
    with pd.ExcelFile(path) as xlsx:
        # Read each sheet to DataFrame and consolidate to empty DataFrame
        for sheet_name in xlsx.sheet_names:
            df_temp = pd.read_excel(xlsx, sheet_name=sheet_name)
            df_all = pd.concat([df_all, df_temp], ignore_index=True)

df_all.to_excel(output_path, index=False)
