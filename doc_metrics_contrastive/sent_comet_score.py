'''
Script to score reference translations containing added pronoun mistranslations
against a second reference, using sentence-level version of COMET
'''

from comet import load_from_checkpoint
#from comet import download_model
from argparse import ArgumentParser


def get_data(src, hyp, ref, indices):
    '''
    Get lists of source, hypothesis and reference sents for instances where
    pronoun mistranslations were added
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

    # only get sentences where mistakes were added
    for idx in idcs:
        idx = int(idx)
        src.append(src_text[idx])
        hyp.append(hyp_text[idx])
        ref.append(ref_text[idx])

    data = [{"src": x, "mt": y, "ref": z} for x, y, z in zip(src, hyp, ref)]
    return data


def main():
    parser = get_argument_parser()
    args = parser.parse_args()

    model_path = "wmt21-comet-mqm/checkpoints/model.ckpt"
    #model_path = download_model("wmt21-comet-mqm")
    model = load_from_checkpoint(model_path)

    data = get_data(args.src, args.hyp, args.ref, args.indices)
    model_output = model.predict(data, batch_size=8, gpus=1)
    print(model_output)


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Score translations with added mistakes.")
    parser.add_argument('--src', type=str, required = True, help="File containing source text.")
    parser.add_argument('--hyp', type=str, required = True, help="File containing hypothesis.")
    parser.add_argument('--ref', type=str, required = True, help="File containing human reference.")
    parser.add_argument('--indices', type=str, required = True, help="File containing indices of corrupted sentences.")
    return parser


if __name__ == '__main__':
    main()