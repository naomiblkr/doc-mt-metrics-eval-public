'''
Author: Naomi Bleiker

Script to save sentences with added translation errors in JSON file:
Perturbed reference (i.e. incorrect translation), correct translation, reference 
and source sentence along is added to file. Two preceding context sentences are also saved.

JSON file was created mainly for illustration purposes, it wasn't directly used for the experiments
'''

import json

# file names have to be changed manually to append to json file
with open ('data/perturbed_refs/corrupted_generaltest2022.refA.de', 'r', encoding='utf-8') as wrong_tr_f, \
    open('data/references/generaltest2022.en-de.ref.refA.de', 'r', encoding='utf-8') as correct_tr_f, \
    open('data/references/generaltest2022.en-de.ref.refB.de', 'r', encoding='utf-8') as ref_f, \
    open('data/sources/generaltest2022.en-de.src.en', 'r', encoding='utf-8') as src_f, \
    open('data/error_indices/idx_errors_generaltest2022_refA.txt', 'r', encoding='utf-8') as indices_f:

    wrong_tr = [line.strip() for line in wrong_tr_f]
    correct_tr = [line.strip() for line in correct_tr_f]
    src = [line.strip() for line in src_f]
    ref = [line.strip() for line in ref_f]
    idcs = [line.strip() for line in indices_f]

    wrong_tr_sents = []
    correct_tr_sents = []
    context = []
    ref_sents = []
    ref_context = []
    src_sents = []
    src_context = []

    # get sentences (and preceding two context sentences) where errors were added
    for idx in idcs:
        idx = int(idx)
        wrong_tr_sents.append(wrong_tr[idx])
        correct_tr_sents.append(correct_tr[idx])
        context.append(' '.join(wrong_tr[idx-2:idx]))
        ref_sents.append(ref[idx])
        ref_context.append(' '.join(ref[idx-2:idx]))
        src_sents.append(src[idx])
        src_context.append(' '.join(src[idx-2:idx]))

    # append dict for each extracted segment
    # context for wrong and correct translation is the same
    data = [{"wrong translation": i, "correct translation": j, "context": k, "reference": l, 
             "reference context": m, "source": n, "source context": o} \
            for i, j, k, l, m, n, o in zip(wrong_tr_sents, correct_tr_sents, context, ref_sents,
                                           ref_context, src_sents, src_context)]
    
    #with open('pro_errors.json', 'w', encoding='utf-8') as outf:
     #   json.dump(data, outf, ensure_ascii=False, indent=3)

    with open('pro_errors.json', 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        
    #for seg in data:
    #   file_data.append(seg)

    #with open('pro_errors.json', 'w', encoding='utf-8') as outf:
    #    json.dump(file_data, outf, ensure_ascii=False, indent=3)