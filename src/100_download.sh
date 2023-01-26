set -e
flg=False
python 001_download.py items --isInitOutputDir $flg
python 001_download.py item_sets --isInitOutputDir $flg
python 001_download.py properties --isInitOutputDir $flg
python 001_download.py resource_templates --isInitOutputDir $flg
python 001_download.py sites --isInitOutputDir $flg
python 001_download.py users --isInitOutputDir $flg
python 001_download.py media --isInitOutputDir $flg