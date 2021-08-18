import argparse
import spacy
from typing import List, Dict


def download_maybe(model_name: str):
    """
    Downloads spacy model if needed
    Args:
        - model_name (str): name of the model
    """
    if not spacy.util.is_package(model_name):
        spacy.cli.download(model_name)


def load_spacy_model(model_name: str):
    """
    Loads spacy model (downloads it if needed)
    Args:
        - model_name (str): name of the model
    Returns:
        - spacy.model.xx.XXXXXX
    """
    download_maybe(model_name)
    return spacy.load(model_name)


def tag_with_spacy(model_name: str, text: str) -> spacy.tokens.doc.Doc:
    """
    Tags text with spacy model
    Args:
        - model_name (str): name of the model
        - text (str): text to be tagged
    Returns:
        - spacy.tokens.doc.Doc
    """
    try:
        nlp = load_spacy_model(model_name)
    except OSError as e:
        print(f"Model: {model_name} not found")
        raise e

    return nlp(text)


def ent_to_dict(entity: spacy.tokens.span.Span) -> Dict:
    """
    Converts SpaCy entity to dictionary
    Args:
        - entity (spacy.tokens.span.Span): entity
    Returns:
        - dict
    """
    return {
        "text": entity.text,
        "type": entity.label_,
        "start_pos": entity.start_char,
        "end_pos": entity.end_char
    }
    

def ner_to_text(tagged_text: spacy.tokens.doc.Doc) -> List[Dict]:
    """
    Converts tagged text to list of dictionary-encoded entities
    """
    return [ent_to_dict(ent) for ent in tagged_text.ents]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str, help="Model name eg. `en_core_web_sm`")
    parser.add_argument("text", type=str, help="Input text to be tagged")
    args = parser.parse_args()

    print(ner_to_text(tag_with_spacy(args.model, args.text)))
