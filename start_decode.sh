export PYTHONPATH=`pwd`
MODEL=$1
python training_ptr_gen/decode.py $MODEL

# nohup bash start_decode.sh log/cov/model_ > log/cov_450k_decode 2>&1 &