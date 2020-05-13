import sys
import pycrfsuite
import hw2_corpus_tool as tool


def create_n_gram(n_gram_pos, n_gram_token, feature, tag, word=None):
    if word:
        n_gram_pos.append(word.pos)
        n_gram_token.append(word.token)
    else:
        n_gram_pos.append("")
        n_gram_token.append("")
    feature.append(f"{tag[0]}={n_gram_pos}")
    feature.append(f"{tag[1]}={n_gram_token}")
    return n_gram_pos[1:], n_gram_token[1:]


def analyze_utterance(feature, utterance, previous_speaker):
    change_speaker = True if utterance.speaker != previous_speaker else False
    feature.append(f"u.change_speaker={change_speaker}")
    if utterance.pos:
        feature.append(f"utterance_length={len(utterance.pos)}")
        feature.append(f"first_pos={utterance.pos[0].pos}")
        bigram_pos = ['']
        bigram_token = ['']
        for index, word in enumerate(utterance.pos):
            feature.append(f"u.pos={word.pos}")
            feature.append(f"u.token={word.token}")
            bigram_pos, bigram_token = create_n_gram(bigram_pos, bigram_token, feature, ["u.bigram_pos", "u.bigram_token"], word)
    return feature, utterance.speaker


def analyze_dialog(dialog):
    previous_speaker = dialog[0].speaker
    features = []
    for index, utterance in enumerate(dialog):
        feature = [f"u.is_first={index == 0}", f"u.is_last={index == len(dialog) - 1}"]
        feature, previous_speaker = analyze_utterance(feature, utterance, previous_speaker)
        features.append(feature)
    return features


def get_labels(dialog):
    return [i.act_tag for i in dialog]


def train(input_dir):
    data = tool.get_data(input_dir)
    trainer = pycrfsuite.Trainer()
    for i in data:
        features = analyze_dialog(i)
        labels = get_labels(i)
        trainer.append(features, labels)
    trainer.set_params({"c1": 1.0, "c2": 1e-3, "max_iterations": 50, "feature.possible_transitions": True})
    trainer.train("model")


def test(test_dir, output_file):
    tagger = pycrfsuite.Tagger()
    tagger.open("model")
    data = tool.get_data(test_dir)
    with open(output_file, "w") as file:
        for i in data:
            features = analyze_dialog(i)
            predict_labels = tagger.tag(features)
            for tag in predict_labels:
                file.write(f"{tag}\n")
            file.write("\n")


def main():
    input_dir, test_dir, output_file = sys.argv[1:]
    train(input_dir)
    test(test_dir, output_file)


main()
