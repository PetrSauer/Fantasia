"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str): 
    pref = 'un' + word
    return pref
    
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    pass


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return ' :: '.join([prefix]+[prefix + word for word in vocab_words[1:]])

    
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    pass


def remove_suffix_ness(word):
    if not word.endswith("ness"):
        return word 
    
    root = word[:-4]
    
    if root.endswith('i'):
        return root[:-1] + 'y'
    
    return root
        
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    pass


def adjective_to_verb(sentence, index):
    words = sentence.split()
    target_word = words[index]
    clean_word = target_word.strip(".,!")
    return clean_word + "en"

