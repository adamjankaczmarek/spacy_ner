import argparse
from spacy import displacy
from spacy_ner import tag_with_spacy


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str, help="Model name eg. `en_core_web_sm`")
    parser.add_argument("text", type=str, help="Input text to be tagged")
    args = parser.parse_args()

    doc = tag_with_spacy(args.model, args.text)
    displacy.serve(doc, style="ent")

