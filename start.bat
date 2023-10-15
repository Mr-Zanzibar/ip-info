@echo off
title IP-INFO
echo Upgrading setuptools...
pip install --upgrade setuptools
echo Default Pip
python -m ensurepip --default-pip


echo Installing required libraries...
pip install requests
pip install pyfiglet
pip install folium

echo Libraries installed. Running IP information script...
python ip.py

pause
