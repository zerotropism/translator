import torch
import fairseq

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
#en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt16.en-de', tokenizer='moses', bpe='subword_nmt')

# Load a transformer trained on WMT'14 En-Fr
en2fr = torch.hub.load('pytorch/fairseq', 'transformer.wmt14.en-fr', tokenizer='moses', bpe='subword_nmt')


# The underlying model is available under the *models* attribute
assert isinstance(en2fr.models[0], fairseq.models.transformer.TransformerModel)

# Translate a sentence
print(en2fr.translate("The Polish nobility enjoyed many rights that were not available to the noble classes of other countries and, typically, each new monarch conceded them further privileges. Those privileges became the basis of the Golden Liberty in the Polish–Lithuanian Commonwealth. Despite having a king, Poland was called the nobility's Commonwealth because the king was elected by all interested members of hereditary nobility and Poland was considered to be the property of this class, not of the king or the ruling dynasty. This state of affairs grew up in part because of the extinction of the male-line descendants of the old royal dynasty (first the Piasts, then the Jagiellons), and the selection by the nobility of the Polish king from among the dynasty's female-line descendants."))
# 'Hallo Welt!'