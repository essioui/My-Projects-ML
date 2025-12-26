#!/usr/bin/env python3
"""
"""
import numpy as np
from transformers import BertTokenizer, BertModel
import torch


class BertEncoder:
    """
    Encode text into vectors using BERT (pytorch).
    """

    def __init__(self, model_name='bert-base-uncased'):
        """
        Initialize the BERT encoder with a specified model.
        """
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.model.eval()
        
    
    def encode(self, texts):
        """
        Encode a list of texts into BERT embeddings.
        Args:
            texts (list of str): List of input texts to encode.
        """
        inputs = self.tokenizer(
            texts,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=512
        )
        
        with torch.no_grad():
            outputs = self.model(**inputs)

        sentence_embeddings = outputs.last_hidden_state.mean(dim=1)
        return sentence_embeddings.detach().cpu().numpy()
