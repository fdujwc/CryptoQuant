# /bin/bash
# 程序启动脚本
WORK_DIR=`pwd`
LOG_DIR=$WORK_DIR/log
mkdir $LOG_DIR
logfile=$LOG_DIR/log_start_sh.txt
cd ~ && source .bashrc && cd $WORK_DIR
export PYTHONPATH="${PYTHONPATH}:$WORK_DIR"
nohup pip3 install -r $WORK_DIR/requirements.txt > $logfile 2>&1 &
nohup python3 $WORK_DIR/src/main.py > $logfile 2>&1 &