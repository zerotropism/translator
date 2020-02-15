import torch
import fairseq
from flask import Flask
from flask import request
from flask_cors import CORS



app = Flask(__name__)

CORS(app)

app.config['DEBUG'] = True

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
#en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt16.en-de', tokenizer='moses', bpe='subword_nmt')

# Load a transformer trained on WMT'14 En-Fr
en2fr = torch.hub.load('pytorch/fairseq', 'transformer.wmt14.en-fr', tokenizer='moses', bpe='subword_nmt')


# The underlying model is available under the *models* attribute
assert isinstance(en2fr.models[0], fairseq.models.transformer.TransformerModel)

@app.route('/',methods=['POST'])

def home():
    txt2translate = request.form.get('text2translate')
    current_translate = en2fr.translate(txt2translate)

    return current_translate

app.run(host="0.0.0.0", port=8080)