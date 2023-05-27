from argparse import ArgumentParser
from get_prompts import get_trans_data, get_prompt
from api import generate_answer
from parse_gpt_answer import parse_answer
import csv
import os


def get_score(responses):
    '''Parse responses and extract the score'''
    scores = []
    for response in responses:
        score = parse_answer(response)
        if score is not None:
            scores.append(score)
    return scores


def get_doc_score(scores):
    '''Get average score per doc (i.e. reference)'''
    doc_score = sum(scores)/len(scores)
    return doc_score


def save_scores(out_path, responses, prompt_type, ref_name, perturbed_vers):
    header = ['prompt type', 'score', 'response']
    scores = [parse_answer(response) for response in responses]
    
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    if perturbed_vers == True:
        filename = f'{prompt_type}_perturbed_{ref_name}.csv'
    else:
        filename = f'{prompt_type}_{ref_name}.csv'
    out_fh = os.path.join(out_path, filename)

    with open(out_fh, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for score, response in zip(scores, responses):
            writer.writerow([prompt_type, score, response])


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Score MT based on source and human reference.")
    parser.add_argument('--src', type=str, required = True, help="File containing source text.")
    parser.add_argument('--hyp', type=str, required = True, help="File containing MT hypothesis.")
    parser.add_argument('--ref', type=str, required = True, help="File containing human reference.")
    parser.add_argument('--indices', type=str, required = True, help="File containing indices of corrupted sentences.")
    parser.add_argument('--lp', type=str, choices=['en-de'], default='en-de',
                        help='Language pair (source language and target language)')
    parser.add_argument('--prompt-type', type=str, choices=['doc_DA', 'doc_SQM'], 
                        default='doc_DA', help='Type of prompt')
    parser.add_argument('--save', type=str, default='gpt_responses', help="Path to save responses in csv file.")
    return parser


def main():
    parser = get_argument_parser()
    args = parser.parse_args()

    # get source, hypotheis and reference with the added context sentences
    data = get_trans_data(args.src, args.hyp, args.ref, args.indices)

    src_lang = args.lp.split("-")[0]
    trg_lang = args.lp.split("-")[-1]
    ref_name = args.ref.split(".")[-2]

    # version with or without added errors
    errors = False
    if args.hyp.split('_')[0] ==  'corrupted':
        errors = True

    # format data and get list of prompts
    messages = get_prompt(data, src_lang, trg_lang, args.prompt_type)
    # generate response for each prompt/message
    responses = [generate_answer(msg) for msg in messages]
    # parse responses to extract scores
    scores = get_score(responses)
    doc_score = get_doc_score(scores)

    print(f'\nScore {doc_score}\n')

    if args.save:
        save_scores(args.save, responses, args.prompt_type, ref_name, errors)


if __name__ == '__main__':
    main()