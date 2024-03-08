#!/bin/bash

GLOVE_FILENAME="glove.zip"
curl -Lo $GLOVE_FILENAME https://huggingface.co/stanfordnlp/glove/resolve/main/glove.840B.300d.zip
unzip $GLOVE_FILENAME
rm $GLOVE_FILENAME
