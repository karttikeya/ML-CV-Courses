This is a solution to the Programming Assignment #2 that scores 100% on the test.

It is for training a word embedding model on the sentences provided in data.mat. The implementation uses Momentum based mini-batch SGD from scratch
and thus allows a lot of experimentation and tinkering with batch size, lerning rate, momentum coefficient, number of epochs etc.

The model calculates the Cross-Entropy loss after every few matches as specified by a global parameter and the average CE loss on the whole data 
after each epoch. After completion, it reports the CE loss on all training data, validation and test data.
