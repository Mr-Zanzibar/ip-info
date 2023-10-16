@echo off
title IP-INFO
echo Upgrading setuptools...
pip install --upgrade setuptools
echo Default Pip
python -m ensurepip --default-pip


echo Installing required libraries...
pip install -r requirements.txt

echo Libraries installed. Running IP information script...
cls
python ip.py

pause
