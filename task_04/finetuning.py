import json
import random
from sentence_transformers import SentenceTransformer, InputExample, losses, datasets
from constants import *

model = SentenceTransformer(MODEL, device="cuda")

# load documents for each data set
docs = []
for data_set in DATA_SETS:
    input_docs_file = f"./data/{data_set}/{data_set}.json"
    with open(input_docs_file, "r") as input_docs:
        # get text from each doc
        for input_doc in input_docs:
            input_doc = json.loads(input_doc)
            doc = input_doc["TEXT"]

            # split doc into sentences
            # ? : ; ! are not included in split
            sentences = doc.split(".")

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
dataloader = datasets.NoDuplicatesDataLoader(anchor_positive_pairs, batch_size=BATCH_SIZE)

# garbage collect docs
import torch
torch.cuda.empty_cache()
import gc
del docs
del anchor_positive_pairs
gc.collect()
#print(torch.cuda.memory_summary(device=None, abbreviated=False))

# fine-tune model with anchor-positive pairs using MNR loss
loss = losses.MultipleNegativesRankingLoss(model=model)
model.fit(
    train_objectives=[(dataloader, loss)],
    epochs=EPOCHS,
    warmup_steps=WARMUP_STEPS,  # use lower learning rate for first few steps
    output_path=MODEL_PATH,  # save model locally
    show_progress_bar=True)
