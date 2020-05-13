import os
import sys
import json
import math
from glob import glob


def main(input_path, mode=1):
    with open("nbmodel.txt", "r") as f:
        data = json.loads(f.readlines()[0])
        spam_token_prob_dict = data["spam_tokens"]
        ham_token_prob_dict = data["ham_tokens"]

    spam_token_prob_values = sorted(spam_token_prob_dict.values())
    lowest_spam_token_prob_value = min(spam_token_prob_values)
    index_lowest_spam_token_prob_value = spam_token_prob_values.index(lowest_spam_token_prob_value)
    ham_token_prob_values = sorted(ham_token_prob_dict.values())
    lowest_ham_token_prob_value = min(ham_token_prob_values)
    index_lowest_ham_token_prob_value = ham_token_prob_values.index(lowest_ham_token_prob_value)

    text_files = [y for x in os.walk(input_path) for y in glob(os.path.join(x[0], "*.txt"))]
    result = []
    for file in text_files:
        spam_prob, ham_prob = data["spam"], data["ham"]
        with open(file, "r", encoding="latin1") as f:
            for line in f.readlines():
                line = line.rstrip()
                for token in line.split():
                    token = modify_token(token, mode)
                    spam_token_prob = spam_token_prob_dict.get(token, 0)
                    ham_token_prob = ham_token_prob_dict.get(token, 0)

                    # Task 3: Experiment
                    is_existed = spam_token_prob and ham_token_prob
                    is_common = spam_token_prob > 0.001 and ham_token_prob > 0.001
                    if mode == 3:
                        if is_common:  # If the word is common, ignore it
                            spam_token_prob = 1
                            ham_token_prob = 1
                        if not is_existed:  # If the word does not exits in the training data, use Zipf's Laws to predict its probability
                            spam_token_prob = lowest_spam_token_prob_value * (index_lowest_spam_token_prob_value + 2.7) / (len(spam_token_prob_values) + 2.7)
                            ham_token_prob = lowest_ham_token_prob_value * (index_lowest_ham_token_prob_value + 2.7) / (len(ham_token_prob_values) + 2.7)

                    spam_prob += math.log10(spam_token_prob) if spam_token_prob > 0 else 0
                    ham_prob += math.log10(ham_token_prob) if ham_token_prob > 0 else 0
        result.append(("spam" if spam_prob > ham_prob else "ham", file))

    with open("nboutput.txt", "w") as f:
        for r in result:
            f.write(f"{r[0]}\t{r[1]}\n")


def modify_token(token, mode):
    new_token = token.lower()
    if mode == 3:  # Task 3: Experimenting removing punctuation
        import string
        new_token = new_token.translate(str.maketrans("", "", string.punctuation))
    return new_token


if __name__ == "__main__":
    main(sys.argv[1], mode=1)
