import sys


def main(output_file):
    label_as_spam, label_as_ham = 0, 0
    belong_in_spam, belong_in_ham = 0, 0
    correct_spam, correct_ham = 0, 0
    with open(output_file, "r") as f:
        for line in f.readlines():
            label, filename = line.split("\t")

            if label == "spam":
                label_as_spam += 1
            elif label == "ham":
                label_as_ham += 1

            if "spam" in filename.lower():
                true_label = "spam"
                belong_in_spam += 1
            elif "ham" in filename.lower():
                true_label = "ham"
                belong_in_ham += 1
            else:
                continue

            if label == true_label == "spam":
                correct_spam += 1
            elif label == true_label == "ham":
                correct_ham += 1

    precision_spam = correct_spam / label_as_spam if label_as_spam > 0 else 0
    precision_ham = correct_ham / label_as_ham if label_as_ham > 0 else 0
    recall_spam = correct_spam / belong_in_spam if label_as_spam > 0 else 0
    recall_ham = correct_ham / belong_in_ham if label_as_ham > 0 else 0
    f1_spam = 2 * precision_spam * recall_spam / (precision_spam + recall_spam) if precision_spam + recall_spam > 0 else 0
    f1_ham = 2 * precision_ham * recall_ham / (precision_ham + recall_ham) if precision_ham + recall_ham > 0 else 0
    print(f"spam precision: {precision_spam}")
    print(f"spam recall: {recall_spam}")
    print(f"spam F1 score: {f1_spam}")
    print(f"ham precision: {precision_ham}")
    print(f"ham recall: {recall_ham}")
    print(f"ham F1 score: {f1_ham}")


if __name__ == "__main__":
    main(sys.argv[1])
