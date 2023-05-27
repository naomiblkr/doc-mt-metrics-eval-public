from CREDENTIALS import credentials
from get_prompts import get_prompt, get_trans_data
from parse_gpt_answer import validate_number
from gpt_api import GptApi
from cache import Cache
from argparse import ArgumentParser
import os
import csv
import numpy as np


def get_sys_score(scores):
    sys_score = np.mean(scores)
    return sys_score


def save_scores(scores, f_name):
    header = ['score']
    
    #if not os.path.exists(out_path):
     #   os.makedirs(out_path)
    PATH = os.path.join("doc_scores", 'line_' + f_name + ".csv")
    with open(PATH, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for score in scores:
            writer.writerow([score])


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Score MT based on source and human reference.")
    parser.add_argument('--src', type=str, required = True, help="File containing source text.")
    parser.add_argument('--hyp', type=str, required = True, help="File containing MT hypothesis.")
    parser.add_argument('--ref', type=str, required = True, help="File containing human reference.")
    parser.add_argument('--docids', type=str, required = True, help="File containing document IDs.")
    parser.add_argument('--lp', type=str, choices=['en-de'], default='en-de',
                        help='Language pair (source language and target language)')
    parser.add_argument('--prompt-type', type=str, choices=['DA_doc', 'SQM_doc'], 
                        default='DA_doc', help='Type of prompt')
    #parser.add_argument('--save', type=str, help="Path to save scores in csv file.")
    return parser


def main():

    parser = get_argument_parser()
    args = parser.parse_args()
    data = get_trans_data(args.src, args.hyp, args.ref, args.docids)
    src_lang = args.lp.split("-")[0]
    trg_lang = args.lp.split("-")[-1]
    messages = get_prompt(data, src_lang, trg_lang, args.prompt_type)
    validate_answer = lambda x: validate_number(x)

    gptapi = GptApi(credentials)
    use_model = "gpt-3.5-turbo"
    annotation = args.prompt_type
    cache = Cache(f"{use_model}_{annotation}.jsonl")

    scoring_name = f"{annotation}_{use_model}"

    if use_model not in credentials["deployments"].keys():
        print(f"Model {use_model} not supported by credentials")

    msg_n = 0
    total = len(messages)
    scores = []
    for msg in messages:
        msg_n += 1

        print(f"Processing prompt {msg_n}/{total}")

        parsed_answers = gptapi.request(msg, use_model, validate_answer, cache=cache)

        score = parsed_answers[0]['answer']
        if (score is not None) and (type(score) == int):
            scores.append(score)


    save_scores(scores, scoring_name)
    sys_score = get_sys_score(scores)
    print(f'System score: {sys_score}')


if __name__ == '__main__':
  main()
