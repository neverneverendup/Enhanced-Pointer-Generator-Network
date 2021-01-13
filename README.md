pytorch implementation and enforcement of pointer-generator network

1. [Train with pointer generation and coverage loss enabled](#train-with-pointer-generation-and-coverage-loss-enabled)
2. [Training with pointer generation enabled](#training-with-pointer-generation-enabled)
3. [How to run training](#how-to-run-training)4. [Papers using this code]a(#papers-using-this-code)




## How to run training:
1) Follow data generation instruction from https://github.com/abisee/cnn-dailymail
2) Run start_train.sh, you might need to change some path and parameters in data_util/config.py
3) For training run start_train.sh, for decoding run start_decode.sh, and for evaluating run run_eval.sh

Note:

* In decode mode beam search batch should have only one example replicated to batch size
https://github.com/atulkum/pointer_summarizer/blob/master/training_ptr_gen/decode.py#L109
https://github.com/atulkum/pointer_summarizer/blob/master/data_util/batcher.py#L226

* It is tested on pytorch 0.4 with python 2.7
* You need to setup [pyrouge](https://github.com/andersjo/pyrouge) to get the rouge score


## Reference
[1]See A, Liu P J, Manning C D. Get To The Point: Summarization with Pointer-Generator Networks[C]//Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2017: 1073-1083.
[2]Chung T L, Xu B, Liu Y, et al. Main Point Generator: Summarizing with a Focus[C]//International Conference on Database Systems for Advanced Applications. Springer, Cham, 2018: 924-932.
