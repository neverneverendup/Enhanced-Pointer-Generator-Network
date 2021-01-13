export PYTHONPATH=`pwd`
nohup CUDA_VISIBLE_DEVICES=1 python -u training_ptr_gen/train.py > ../log/training_log 2>&1 &

