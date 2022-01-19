from typing import Dict, List, Optional, Any
from typing import Callable, Mapping
import os
import sys
from .featurizing import *

# nltk package for featurizing
import nltk

# spacy package for featurizing
import spacy

# pretrained models
from .utils.util_model import *
# pre_model_basic_words = load_pre_model(os.path.join(os.path.dirname(__file__),
#                                                     './pre_models/basic_words.pkl'))
# pip install lexicalrichness
import lexicalrichness

# print(pre_model_basic_words)




@featurizing(name="get_length", contributor="datalab",
             task = "Any",description = "This function is used to calculate the length of a text")
def get_length(text:str) -> str:
    """
    Package: python
    Input:
        text:str
    Output:
        integer
    """
    # text = sample["text"]
    return len(text.split(" "))


@featurizing(name = "get_entities_spacy", contributor="spacy",
             task = "Any",description = "Extract entities of a given text by using spacy library.")
def get_entities_spacy(text:str) -> List[str]:

    nlp = spacy.load('en_core_web_sm') # this should be pre-reloaded
    doc = nlp(text)
    entities = [(ent.text,ent.label_) for ent in doc.ents]
    return entities


@featurizing(name = "get_postag_spacy", contributor="spacy",
             task="Any", description="Part-of-speech tagging of a given text by using spacy library.")
def get_postag_spacy(text:str) -> List[str]:

    nlp = spacy.load('en_core_web_sm') # this should be pre-reloaded
    doc = nlp(text)
    token_postags = [(token.text, token.tag_) for token in doc]
    return token_postags



@featurizing(name="get_postag_nltk", contributor="nltk",
             task="Any", description="Part-of-speech tagging of a given text by using NLTK library")
def get_postag_nltk(text:str) -> List:
    """
    Package: nltk.pos_tag
    Input:
        text:str
    Output:
        List
    """

    from nltk import pos_tag
    try:
        nltk.pos_tag([])
    except LookupError:
        nltk.download('averaged_perceptron_tagger')

    token_tag_tuples = pos_tag(text.split(" "))
    # pos_tags = [(res[0], res[1]) for res in token_tag_tuples]
    return token_tag_tuples




@featurizing(name="get_basic_words", contributor="datalab",
             task="Any", description="Calculate the ratio of basic words in a given text")
def get_basic_words(sentence:str):


    # the sentence must written in english
    # sample level
    # sentence : string  'XXX'



    if BASIC_WORDS is None:
        raise ValueError("basic word dictionary is none")

    value_list = sentence.split(' ')
    n_words = len(value_list)
    n_basic_words = 0

    for word in value_list:

        lower = word.lower()
        if lower in BASIC_WORDS:
            n_basic_words = n_basic_words + 1

    return n_basic_words*1.0/n_words




@featurizing(name="get_lexical_richness", contributor="lexicalrichness",
             task="Any", description="Calculate the lexical richness (i.e.lexical diversity) of a text")
def get_lexical_richness(sentence:str):
    # sample level
    # sentence : string  'XXX'


    from lexicalrichness import LexicalRichness

    # print(f"-------\n{sentence}\n")
    lex = LexicalRichness(sentence)
    results = 0

    try:
        results = lex.ttr
    except ZeroDivisionError:
        print(f'the sentence "{sentence}" contain no effective words, we will return 0 instead!')
    finally:
        return results


gendered_dic = load_gender_bias_data()

@featurizing(name="get_gender_bias", contributor="datalab",
             task="Any", description="Calculate the number of man/women tokens of a given text")
def get_gender_bias(sentence:str):


    # if gendered_dic is None:
    #     gendered_dic = load_gender_bias_data()

    one_words_results = get_gender_bias_one_word(
        gendered_dic['words']['male'],
        gendered_dic['words']['female'],
        gendered_dic['single_name']['male'],
        gendered_dic['single_name']['female'],
        sentence,
    )

    results = {
        'word': {
            'male': one_words_results['words_m'],
            'female': one_words_results['words_f']
        },
        'single_name': {
            'male': one_words_results['single_name_m'],
            'female': one_words_results['single_name_f']
        },
        # 'name': {
        #     'male': get_gender_bias_two_words(gendered_dic['real_name']['male'], sentence),
        #     'female': get_gender_bias_two_words(gendered_dic['real_name']['female'], sentence)
        # }
    }

    return results


def get_gender_bias_one_word(words_m, words_f, single_name_m, single_name_f, sentence):
    words_sentence = sentence.lower().split(' ')

    results = {
        'words_m': 0,
        'words_f': 0,
        'single_name_m': 0,
        'single_name_f': 0,
    }
    for value in words_sentence:
        if value in words_m:
            results['words_m'] += 1

        if value in words_f:
            results['words_f'] += 1

        if value in single_name_m:
            results['single_name_m'] += 1

        if value in single_name_f:
            results['single_name_f'] += 1

    return results


# def get_gender_bias_two_words(gender_dic, sentence):
#     sentence = ' ' + sentence.lower().strip() + ' '
#
#     results = 0
#     for value in gender_dic:
#         count = sentence.count(' ' + value + ' ')
#         results += count
#
#     return results