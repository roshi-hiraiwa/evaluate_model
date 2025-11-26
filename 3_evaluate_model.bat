@echo off

PAUSE

rem 仮想環境（anaconda）の有効化、keras_env_looは事前に用意した仮想環境
call C:\Users\hogehoge\anaconda3\Scripts\activate.bat keras_env_loo
cd .\src
python evaluate_model.py

PAUSE
