'''
Author: Naomi Bleiker
Filter sentences with anaphoric "it" to produce pronoun translations mistakes
'''

from argparse import ArgumentParser
from typing import List, Tuple
from sacremoses import MosesTokenizer
from simalign import SentenceAligner


de_prons = ["Er", "Sie", "Es", "er", "sie", "es"]
en_prons = ['it', 'It']


def tokenize(filename: str, lang_code: str) -> List[List[str]]:
    with open(filename, 'r') as f:
        mt = MosesTokenizer(lang=lang_code)
        tokens = [mt.tokenize(line) for line in f]
    return tokens


def filter_sent_it(src_tokens: List[List], ref_tokens: List[List]) -> List[int]:
    '''
    Find instances where source sent contains pronoun "it" and respective
    reference sentence contains one of the German pronouns "es", "sie" or "er".
    :return: List of indices of the respective sentences
    '''
    indices = []
    for idx, sent in enumerate(src_tokens):
        if ("It" in sent) or ("it" in sent):
            for pron in de_prons:
                if pron in ref_tokens[idx]:
                    if idx not in indices:
                        indices.append(idx)
    return indices


def get_alignment(src_tokens: List[List], ref_tokens: List[List], sent_idx_pron: List) -> List[List[Tuple]]:
    '''
    Get word alignments (only for the extracted sentences)
    :return: List of tuples containing alignments (i.e. token indices) per sentence
    '''
    myaligner = SentenceAligner(model="bert", token_type="bpe")
    alignments = []
    # only get alignments for sents containing translation of "it"
    for i in range(len(src_tokens)):
        if i in sent_idx_pron:
            results = myaligner.get_word_aligns(src_tokens[i], ref_tokens[i])
            alignments.append(results["mwmf"])
        else:
            alignments.append([])
    return alignments


def filter_pron(src_tokens: List[List], ref_tokens: List[List], alignments: List[List[Tuple]]):
    '''
    Check whether "it" and German pronoun are aligned and extract the respective sentences.
    :return: Index of the respective sentence, along with the alignment and the German pronoun.
    '''
    pronouns = []
    line = 0
    for src_sent, ref_sent, al_sent in zip(src_tokens, ref_tokens, alignments):
        line += 1
        for en_pron in en_prons:
            if en_pron in src_sent:
                # get index of English pronoun
                en_idx = src_sent.index(en_pron)
                for de_pron in de_prons:
                    if de_pron in ref_sent:
                        # get index of German pronoun
                        de_idx = ref_sent.index(de_pron)
                        # check if English and German pronouns are aligned
                        for al in al_sent:
                            if (en_idx == al[0]) and (de_idx == al[1]):
                                pronouns.append((line, al, de_pron))

    return pronouns


def main():
    parser = ArgumentParser(description='Extract sentences containing pronoun translations')
    parser.add_argument('reference')
    parser.add_argument('source')
    args = parser.parse_args()

    de_tokens = tokenize(args.reference, 'de')
    en_tokens = tokenize(args.source, 'en')
    indices = filter_sent_it(en_tokens, de_tokens)
    alignments = get_alignment(en_tokens, de_tokens, indices)
    prons = filter_pron(en_tokens, de_tokens, alignments)
    for i in prons:
        print(f'Sentence index: {i[0]}')
        print(f'Alignment: {i[1]}')
        print(f'German pronoun to be changed: {i[2]}\n\n')


if __name__ == '__main__':
    main()