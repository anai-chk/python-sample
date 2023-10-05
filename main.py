import pandas as pd
from  features.read_and_write import read_query, save_query
from features.replace_functions import update_query_translator

# file path and lgcode settings
# 以下の三つのファイルパスを指定してください。
# - 変換したいファイルのパス
# - ルールを適用するexcelのファイルパス
# - 出力先のファイルパス
# 
# また、対象自治体のlgcodeを設定してください。

READ_FILE_PATH        = 'IO/mifune_mapinfo.txt'
EXCEL_RULES_FILE_PATH = 'translator_rules.xlsx'
OUTPUT_FILE_PATH      = 'IO/UPDATE_mapinfos_mifune-output.txt'
LGCODE = 434418

# 実際の処理が走ります。
querys = read_query(READ_FILE_PATH)
rules = pd.read_excel(EXCEL_RULES_FILE_PATH)
output_filename = OUTPUT_FILE_PATH

# 変換の処理
updated_query = update_query_translator(querys, rules, lgcode=LGCODE)

# 返還後のファイルの保存
save_query(updated_query, output_filename)