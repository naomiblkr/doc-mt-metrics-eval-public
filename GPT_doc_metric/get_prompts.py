from typing import List, Dict

lang_codes = {'en': 'English', 'de': 'German'}


prompts = {'DA_doc': 'Score the last sentence of the following translation from {source_lang} to {target_lang} with respect to the human reference on a continuous scale 0 to 100 where score of zero means "no meaning preserved, not fluent" and score of one hundred means "perfect fluency, meaning and grammar".\n\n{source_lang} source: "{src_seg}"\n{target_lang} human reference: {ref_seg}\n{target_lang} machine translation: "{trg_seg}"\nScore: ', \
            'SQM_doc': 'Score the last sentence of the following machine translation from {source_lang} to {target_lang} with respect to the human reference on a continuous scale from 0 to 100 that starts with "No meaning preserved, not fluent", goes through "Some meaning preserved, lacking fluency", then "Most meaning preserved, mostly fluent", up to "Perfect fluency, meaning and grammar".\n\n{source_lang} source: "{src_seg}"\n{target_lang} human reference: "{ref_seg}"\n{target_lang} machine translation: "{trg_seg}"\nScore (0-100): '}


def add_context(orig_txt: List[str], context: List[str], doc_ids: List[str], window: int) -> List[str]:
    '''Add n preceeding context sentences to each sentence.'''
    assert len(orig_txt) == len(context)
    i, n = 0, 0
    augm_txt = []
    doc_id = doc_ids[0]
    while i < len(orig_txt):
        if doc_ids[i] == doc_id:
            context_window = context[i - min(n, window):i]
            augm_txt.append(' '.join(context_window + [orig_txt[i]]))
            i += 1
        else:
            doc_id = doc_ids[i]
            # add last two sentences and last sentence again, as not to weight them less
            # this makes augmented text longer than the original
            #augm_txt.append(context[i-2] + ' ' + orig_txt[i-1])
            #augm_txt.append(orig_txt[i-1])
            n = -1
        n += 1
    return augm_txt


def get_trans_data(src:str, hyp:str, ref:str, doc_ids:str) -> Dict[str, List[str]]:
    '''Get source, hypothesis and reference text and add context sentences'''
    with open(src, 'r', encoding='utf-8') as src_f, \
         open(hyp, 'r', encoding='utf-8') as hyp_f, open(ref, 'r', encoding='utf-8') as ref_f, \
        open(doc_ids, 'r', encoding='utf-8') as doc_id_f:
        src_text = [line.strip() for line in src_f]
        hyp_text = [line.strip() for line in hyp_f]
        ref_text = [line.strip() for line in ref_f]
        ids = [line.strip() for line in doc_id_f]

        trans_data = {'src': [], 'hyp': [], 'ref': []}
        trans_data['src'] = add_context(src_text, src_text, ids, window=2)
        trans_data['hyp'] = add_context(hyp_text, hyp_text, ids, window=2)
        trans_data['ref'] = add_context(ref_text, ref_text, ids, window=2)

    return trans_data


def get_prompt(data:Dict[str, List[str]], src_lang:str, trg_lang:str, prompt_type:str) -> List[List]:
    """Get the respective prompt type and add ref, src and trg sentences to the prompt"""
    messages = []
    for src_seg, trg_seg, ref_seg in zip(data['src'], data['hyp'], data['ref']):
        prompt_input = {'src_seg': src_seg, 'trg_seg': trg_seg,
                    'ref_seg': ref_seg, 'source_lang': lang_codes[src_lang],
                    'target_lang': lang_codes[trg_lang]}
        prompt = prompts[prompt_type].format(**prompt_input)
        messages.append(prompt)
    return  messages