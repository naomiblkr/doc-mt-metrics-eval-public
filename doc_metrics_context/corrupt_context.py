# Corruptions of context sentences

from typing import List
import random


def remove_context(context: List[str]) -> List[str]:
    """
    Remove all context sentences.
    :return: List of empty strings
    """
    # context sentences are replaced by empty string
    corrupted_context = ["" for sent in context]

    return corrupted_context


def shuffle_context(context: List[str]) -> List[str]:
    """
    Random permutation of context sentences.
    :return: List of sentences in random order
    """
    random.seed(50)
    corrupted_context = random.sample(context, len(context))

    return corrupted_context