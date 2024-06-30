from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'i love my dog',
    'I, love my cat',
    'You love my dog!',
    'i love rabbit',
    'He loves my dog',
    'Do you love my cat?',
    'We love our pets',
    'My dog loves to play fetch',
    'She loves her new kitten',
    'They love animals'
]

tokenizer = Tokenizer(num_words = 100)

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(word_index)

