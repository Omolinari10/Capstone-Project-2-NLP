from nlp_helper_functions import my_tokenize, my_pad

def preprocess(x, y):
    """
    Preprocess x and y
    :param x: List of English sentences
    :param y: List of French sentences
    :return: Tuple of (Preprocessed x, Preprocessed y, x tokenizer, y tokenizer)
    """
    preprocess_x, x_tk = my_tokenize.tokenize(x)
    preprocess_y, y_tk = my_tokenize.tokenize(y)

    preprocess_x = my_pad.pad(preprocess_x)
    preprocess_y = my_pad.pad(preprocess_y)

    # Keras's sparse_categorical_crossentropy function requires the labels to be in 3 dimensions
    preprocess_y = preprocess_y.reshape(*preprocess_y.shape, 1)

    return preprocess_x, preprocess_y, x_tk, y_tk
