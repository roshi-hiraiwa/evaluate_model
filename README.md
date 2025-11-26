# 評価指標算出ツール
ゼミの`b3_practice2`フォルダを使って、モデルの評価指標（混同行列、正解率、適合率、再現率、F1値）を算出するプログラムです。

## ファイルの配置場所
GitHubからダウンロードしたファイルを、自分のPCの以下の場所に配置してください。

1. プログラムの配置
   GitHubの`src`フォルダ内にある`evaluate_model.py`を、`b3_practice2/src/`に入れてください。

2. バッチファイルの配置
   `3_evaluate_model.bat`を、`b3_practice2`フォルダの直下に入れてください。

> 配置後のフォルダ構成イメージ
> ```text
> b3_practice2/
>  ├── 2_classification_loo.bat
>  ├── 3_evaluate_model.bat  <-- ここに配置
>  ├── train_data.csv
>  ├── target/
>  │    └── result.csv
>  └── src/
>       └── evaluate_model.py  <-- ここに配置
> ```

## 設定（バッチファイルの書き換え）
ダウンロードした`3_evaluate_model.bat`をそのまま実行するとエラーになるため、自分の環境に合わせて書き換える必要があります。

1. `3_evaluate_model.bat`を右クリックして「メモ帳で編集」を選びます。

2. Anacondaのパスにあるユーザー名を修正し、保存してください。

   ```bat
   REM 修正前
   call C:\Users\hogehoge\anaconda3\Scripts\activate.bat keras_env_loo

   REM 修正後（例：ユーザー名がtanakaの場合）
   call C:\Users\tanaka\anaconda3\Scripts\activate.bat keras_env_loo
   ```

## 使い方（実行手順）
このツールは、モデルの学習・予測が終わった後に使用します。必ず以下の順番で実行してください。

1. 学習・予測を実行する
   `2_classification_loo.bat`を実行して、計算を完了させてください。（これによって`target/result.csv`が生成されます）

2. 評価を実行する
   `3_evaluate_model.bat`をダブルクリックして実行してください。コマンドプロンプトが立ち上がり、モデルの評価指標（混同行列、正解率、適合率、再現率、F1値）が表示されます。
   ※画面の結果は、スクリーンショットを撮るかメモ帳にコピペして保存してください。

## 注意事項
以下のファイルは、評価算出の元データとして使用します。内容を書き換えると正しい結果が得られません。
また、文字コードをShift-JISから変更しないでください。

- `b3_practice2/train_data.csv`（正解ラベルなどが入っています）
- `b3_practice2/target/result.csv`（2_classification_loo.batで生成される予測結果です）
