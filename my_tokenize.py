from keras.preprocessing.text import Tokenizer

def tokenize(x):
    """
    Tokenize x
    :param x: List of sentences/strings to be tokenized
    :return: Tuple of (tokenized x data, tokenizer used to tokenize x)
    """
    tk = Tokenizer()
    tk.fit_on_texts(x)
    return tk.texts_to_sequences(x), tk
