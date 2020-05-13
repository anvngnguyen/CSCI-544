import os
import sys
import json
import random


def main(input_path, mode=1):
    total_ham, total_spam = 0, 0
    ham_tokens, spam_tokens = {}, {}
    for root, dirs, files in os.walk(input_path):
        sample_size_multiplier = 0.1 if mode == 2 else 1
        files = random.sample(files, int(sample_size_multiplier * len(files)))

        if "ham" in root:
            total_ham += process_tokens(root, files, ham_tokens, mode)
        if "spam" in root:
            total_spam += process_tokens(root, files, spam_tokens, mode)

    probability = {"spam": total_spam / (total_spam + total_ham), "ham": total_ham / (total_spam + total_ham)}
    spam_tokens = add_one_smoothing(ham_tokens, spam_tokens)
    ham_tokens = add_one_smoothing(spam_tokens, ham_tokens)
    calculate_token_probability(probability, spam_tokens, "spam_tokens")
    calculate_token_probability(probability, ham_tokens, "ham_tokens")

    with open("nbmodel.txt", "w") as f:
        json.dump(probability, f)


def process_tokens(root, files, tokens, mode):
    number_of_files = len(files)
    for file in files:
        with open(os.path.join(root, file), "r", encoding="latin1") as f:
            for line in f.readlines():
                line = line.rstrip()
                for token in line.split():
                    token = modify_token(token, mode)
                    if token not in tokens:
                        tokens[token] = 0
                    tokens[token] += 1
    return number_of_files


def add_one_smoothing(giving_token_dict, receiving_token_dict):
    copy_dict = receiving_token_dict.copy()
    for k in giving_token_dict.keys():
        if k not in receiving_token_dict.keys():
            copy_dict[k] = 0
    for key in copy_dict.keys():
        copy_dict[key] += 1
    return copy_dict


def calculate_token_probability(probability, tokens, key):
    total_token_values = sum(tokens.values())
    probability[key] = {k: v / total_token_values for k, v in tokens.items()}


def modify_token(token, mode):
    new_token = token.lower()
    if mode == 3:  # Task 3: Experimenting removing punctuation
        import string
        new_token = new_token.translate(str.maketrans("", "", string.punctuation))
    return new_token


if __name__ == "__main__":
    main(sys.argv[1], mode=1)
