import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

pd.set_option("display.unicode.east_asian_width", True)

# CSVファイルの相対パス
train_path = "../train_data.csv"
result_path = "../target/result.csv"

# 文字コードはcp932(Shift-JIS)を指定
train_encoding = "cp932"
result_encoding = "cp932"

# CSVファイルのカラム名を定義
train_column = ["name", "label"]
result_column = ["name", "label_zero", "label_one"]

try:
    # CSVファイルの読み込み
    df_train = pd.read_csv(
        train_path,
        encoding=train_encoding,
        header=None,
        names=train_column,
        usecols=[0, 1],
    )
    df_result = pd.read_csv(
        result_path,
        encoding=result_encoding,
        header=None,
        names=result_column,
        usecols=[0, 1, 2],
    )

    # エラー処理
    if len(df_train) != len(df_result):
        raise ValueError("行数が一致していません。")

    if df_train.isnull().values.any() or df_result.isnull().values.any():
        raise ValueError("データに空欄(NaN)が含まれています。")

    if not (df_train["name"] == df_result["name"]).all():
        raise ValueError("データの並び順が一致していません。")

    # 正解のラベル
    y_true = df_train["label"]

    # 予測のラベル
    y_pred = (df_result["label_one"] > df_result["label_zero"]).astype(int)

    # 混同行列を作成
    cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
    cm_df = pd.DataFrame(
        cm, index=["正解(1)", "正解(0)"], columns=["予測(1)", "予測(0)"]
    )

    # 正解率、適合率、再現率、F1値を計算
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    recall = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    f1 = f1_score(y_true, y_pred, pos_label=1, zero_division=0)

    print("-" * 26)
    print("[混同行列]")
    print(cm_df)
    print("-" * 26)
    print("[評価指標]")
    print(f"正解率：{accuracy:.3f}")
    print(f"適合率：{precision:.3f}")
    print(f"再現率：{recall:.3f}")
    print(f"F1値  ：{f1:.3f}")
    print("-" * 26)

except FileNotFoundError:
    print("エラー：ファイルが見つかりませんでした。")
except UnicodeDecodeError:
    print("エラー：ファイルの文字コードをShift-JISにしてください。")
except ValueError as e:
    print(f"エラー：{e}")
except Exception as e:
    print(f"予期せぬエラーが発生しました：{e}")
