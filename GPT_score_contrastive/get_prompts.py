from typing import List, Dict


lang_codes = {'en': 'English', 'de': 'German'}

prompts = {'doc_DA': 'Score the last sentence of the following translation from {source_lang} to {target_lang} with respect to human reference on a continuous scale 0 to 100 where score of zero means "no meaning preserved, not fluent" and score of one hundred means "perfect fluency, meaning and grammar".\n\n{source_lang} source: "{src_seg}"\n{target_lang} human reference: {ref_seg}\n{target_lang} machine translation: "{trg_seg}"\nScore: ', \
        'doc_SQM': 'Score the last sentence of the following machine translation from {source_lang} to {target_lang} with respect to the human reference on a continuous scale from 0 to 100 that starts with "No meaning preserved, not fluent", goes through "Some meaning preserved, lacking fluency", then "Most meaning preserved, mostly fluent", up to "Perfect fluency, meaning and grammar".\n\n{source_lang} source: "{src_seg}"\n{target_lang} human reference: "{ref_seg}"\n{target_lang} machine translation: "{trg_seg}"\nScore (0-100): '}


def get_trans_data(src:str, hyp:str, ref:str, indices:str) -> Dict[str, List[str]]:
    '''Get source, hypothesis and reference text and add context sentences'''
    with open(indices, 'r', encoding='utf-8') as idx_f, open(src, 'r', encoding='utf-8') as src_f, \
        open(hyp, 'r', encoding='utf-8') as hyp_f, open(ref, 'r', encoding='utf-8') as ref_f:
        idcs = [line.strip() for line in idx_f]
        src_text = [line.strip() for line in src_f]
        hyp_text = [line.strip() for line in hyp_f]
        ref_text = [line.strip() for line in ref_f]
        
        trans_data = {'src': [], 'hyp': [], 'ref': []}

        # add src, hyp and ref sentences with two previous context sentences
        # only for sentences where errors were added
        for idx in idcs:
            idx = int(idx)
            trans_data['src'].append(' '.join(src_text[idx-2:idx+1]))
            trans_data['hyp'].append(' '.join(hyp_text[idx-2:idx+1]))
            trans_data['ref'].append(' '.join(ref_text[idx-2:idx+1]))

    return trans_data


def get_prompt(data:Dict[str, List[str]], src_lang:str, trg_lang:str, prompt_type:str) -> List[List]:
    """Get the respective prompt type and add ref, src and trg sentences to the prompt"""
    messages = []
    for src_seg, trg_seg, ref_seg in zip(data['src'], data['hyp'], data['ref']):
        prompt_input = {'src_seg': src_seg, 'trg_seg': trg_seg,
                    'ref_seg': ref_seg, 'source_lang': lang_codes[src_lang],
                    'target_lang': lang_codes[trg_lang]}
        prompt = prompts[prompt_type].format(**prompt_input)
        message = [
        {"role": "system", "content": "You are an assistant that evaluates machine translation quality."},
        {"role": "user", "content": prompt}
        ]
        messages.append(message)
    return  messages