import itertools
import random

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))
from edit.editing import *

"""
Class for creating augmentations by insterting filler words and phrases in English.

Author: Venelin Kovatchev

"""


def filler_word(text, prob=0.166, sp_p=True, unc_p=True, fill_p=True, seed=0, max_outputs=1):

    # Speaker opinion/mental state phrases
    # Taken from Kovatchev et al. (2021)
    speaker_phrases = ["I think", "I believe", "I mean", "I guess", "that is", 
                       "I assume", "I feel", "In my opinion", "I would say"]

    # Words and phrases indicating uncertainty
    # Taken from Kovatchev et al. (2021)
    uncertain_phrases = ["maybe", "perhaps", "probably", "possibly", "most likely"]

    # Filler words that should preserve the meaning of the phrase
    # Taken from Laserna et al. (2014)
    fill_phrases=["uhm", "umm", "ahh", "err", "actually", "obviously", "naturally", "like", "you know"]

    # Initialize the list of all augmentation phrases
    all_fill = []

    # Add speaker phrases, if enabled
    if sp_p: 
      all_fill += speaker_phrases
    
    # Add uncertain phrases, if enabled
    if unc_p:
      all_fill += uncertain_phrases

    # Add filler phrases, if enabled
    if fill_p:
      all_fill += fill_phrases
        
    # Initialize random seed
    random.seed(seed)

    # Calculate probability of insertion, default is 16.6 (one in 6 words)
    prob_of_insertion = int(prob * 100)

    # Initialize output
    augmented_texts = []
    
    # Iterate over number of outputs to generate
    for _ in itertools.repeat(None, max_outputs):
        
        out_list = []
        
        # Split the input
        # Original transformation is for english, so .split() is sufficient
        # If this transformation is adapted for other languages, a proper
        # tokenization could be required in place of .split()
        for cur_word in text.split():
            # Based on the random choice, insert a phrase before current word
            if random.choice(range(0, 100)) <= prob_of_insertion:
                # To avoid always inserting the same word at the same location
                # when running the script on single examples, I update the 
                # random seed based on the current word and its position
                seed = len(cur_word) + len(out_list)
                random.seed(seed)
                
                # Select the word or phrase to insert
                random_filler = random.choice(all_fill)
                out_list.append(random_filler)
                
            # Always add the original word
            out_list.append(cur_word)
            
            # Convert back into string
            out_text = " ".join(out_list)
        
        # Add augmented example to the output
        augmented_texts.append(out_text)
    
    return(augmented_texts)

"""
Class for implementing filler words addition
"""
@editing(name = "add_filler_words", contributor = "xl_augmenter",
         task = "Any", description="this function inserts filler words and phrases (ehh, urr, perhaps, you know) in the text.")
def add_filler_words(text:str, max_outputs = 1, seed = 0, in_prob = 0.166,
                 speaker_ph=True, uncertain_ph=True, fill_ph=True):
    augmented_texts = filler_word(
        text=text,
        prob=in_prob,
        sp_p=speaker_ph,
        unc_p=uncertain_ph,
        fill_p=fill_ph,
        seed=seed,
        max_outputs=max_outputs,
    )
    # return augmented_texts
    return {"text_add_filler_words":augmented_texts[0]}

# sentence = "Andrew finally returned the French book to Chris that I bought last week"
# perturbed = add_filler_words(text=sentence)
# print(perturbed)