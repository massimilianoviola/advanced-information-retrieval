import json
import random
import argparse
from sentence_transformers import SentenceTransformer, InputExample, losses, datasets
from constants import *

parser = argparse.ArgumentParser()
parser.add_argument("-m","--model", type=str, help="Model name")
parser.add_argument("-d","--documents", type=str, help="Path to documents")
parser.add_argument("-f","--folder_model", type=str, help="Folder to save model to")
parser.add_argument("-e","--epochs", type=int, help="Number of epochs")
parser.add_argument("-w","--warmup_steps", type=int, help="Number of warmup steps")
parser.add_argument("-b","--batch_size", type=int, help="Batch size")
args = parser.parse_args()

model = SentenceTransformer(args.model, device="cuda")

# load documents
docs = []
with open(args.documents, "r") as docs_file:
    # get text from each doc
    for doc in docs_file:
        doc = json.loads(doc)

        # split doc into sentences
        # ? : ; ! are not included in split
        sentences = doc["TEXT"].split(".")

        # remove sentences with less than 4 words
        sentences = [sentence for sentence in sentences if len(sentence.split(" ")) > 4]
        docs.append(sentences)

# create anchor-positive pairs
# * Assumption:
# * sentences in same doc tend to be similar
# * sentences in same doc tend to become less similar as more sentences are between them
anchor_positive_pairs = []
for doc in docs:
    for i in range(len(doc)):
        for j in range(i + 1, len(doc)):
            # create anchor-positive pair
            anchor_positive_pairs.append(InputExample(texts=[doc[i], doc[j]]))
            # stop if sentences are more than 3 sentences apart
            if j - i > 3:
                break

# store shuffled pairs in dataloader - since a DataLoader is required for model.fit()
random.shuffle(anchor_positive_pairs)
# NoDuplicatesDataLoader removes duplicate pairs
# * removing duplicates not needed since there are no duplicates
# * however only dataloader in sentence_transformers
dataloader = datasets.NoDuplicatesDataLoader(anchor_positive_pairs, batch_size=args.batch_size)

# free up memory if needed
'''
# garbage collect docs
import torch
import gc 
del docs
del anchor_positive_pairs
torch.cuda.empty_cache()
gc.collect()
'''

# fine-tune model with anchor-positive pairs using MNR loss
loss = losses.MultipleNegativesRankingLoss(model=model)
model.fit(
    train_objectives=[(dataloader, loss)],
    epochs=args.epochs,
    warmup_steps=args.warmup_steps,  # use lower learning rate for first few steps
    output_path=args.folder_model,  # save model locally
    show_progress_bar=True)
