'''
Script to score reference translations containing added pronoun mistranslations
against a second reference, using document-level version of COMET
'''

from comet import download_model, load_from_checkpoint
from add_context import add_context
from argparse import ArgumentParser


def get_data(src, hyp, ref, indices, sep_token):
    '''
    Get source, hypothesis and reference sents and concatenate with context sents
    :param indices: File containing indices of sents where errors were added
    :return: Dictionary with lists of src, hyp and ref sentences
    '''
    with open(src, 'r', encoding='utf-8') as src_f, open(hyp, 'r', encoding='utf-8') as hyp_f, \
        open(ref, 'r', encoding='utf-8') as ref_f, open(indices, 'r', encoding='utf-8') as idx_f:
        src_text = [line.strip() for line in src_f]
        hyp_text = [line.strip() for line in hyp_f]
        ref_text = [line.strip() for line in ref_f]
        idcs = [line.strip() for line in idx_f]

    src = []
    hyp = []
    ref = []

    # concatenate src, hyp and ref sentences with two previous context sentences
    # only for sentences where mistakes were added
    for idx in idcs:
        idx = int(idx)
        src.append(" {} ".format(sep_token).join(src_text[idx-2:idx+1]))
        hyp.append(" {} ".format(sep_token).join(hyp_text[idx-2:idx+1]))
        ref.append(" {} ".format(sep_token).join(ref_text[idx-2:idx+1]))

    data = [{"src": x, "mt": y, "ref": z} for x, y, z in zip(src, hyp, ref)]
    return data


def main():
    parser = get_argument_parser()
    args = parser.parse_args()

    # load comet model
    model_path = download_model("wmt21-comet-mqm")
    model = load_from_checkpoint(model_path)

    # enable document-level evaluation
    model.set_document_level()

    sep_token = model.encoder.tokenizer.sep_token

    data = get_data(args.src, args.hyp, args.ref, args.indices, sep_token)
    seg_scores, sys_score = model.predict(data, batch_size=8, gpus=1)
    print(f'Score: {sys_score}')


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Score translations with added mistakes.")
    parser.add_argument('--src', type=str, required = True, help="File containing source text.")
    parser.add_argument('--hyp', type=str, required = True, help="File containing hypothesis.")
    parser.add_argument('--ref', type=str, required = True, help="File containing human reference.")
    parser.add_argument('--indices', type=str, required = True, help="File containing indices of corrupted sentences.")
    return parser


if __name__ == '__main__':
    main()