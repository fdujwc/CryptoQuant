# 程序启动脚本
pip3 install -r requirements.txt
export WORK_DIR=/root/CryptoQuant
export PYTHONPATH="${PYTHONPATH}:$WORK_DIR"
nohup python3 $WORK_DIR/src/main.py > ./log.txt 2>&1 &