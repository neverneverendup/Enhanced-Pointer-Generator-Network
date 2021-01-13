from data_utils.utils import rouge_eval, write_for_rouge, rouge_log
import sys

if __name__ == '__main__':
    # rouge_ref_dir = sys.argv[1]
    # rouge_dec_dir =  sys.argv[2]
    decode_dir = sys.argv[1]
    results_dict = rouge_eval(decode_dir+"/rouge_ref", decode_dir+"/rouge_dec_dir")
    rouge_log(results_dict, decode_dir)