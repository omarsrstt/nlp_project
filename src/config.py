import os


class Config:
    dataset = "Reddit"
    # dataset = "iSarcasm"
    if dataset == "iSarcasm":
        dataset = "iSarcasmEval"

    file_dir = os.path.join("..", "data", dataset)

    if dataset == "Reddit":
        input_file_path = os.path.join(file_dir, "train-balanced-sarcasm.csv")
        test_file_path = os.path.join(file_dir, "test-balanced.csv")
        comment_col_name = "comment"
        label_col_name = "label"
    else:
        input_file_path = os.path.join(file_dir, "train.csv")
        test_file_path = os.path.join(file_dir, "test.csv")
        comment_col_name = "tweet"
        label_col_name = "sarcastic"

    preprocessed_file_path = os.path.join(file_dir, "preprocessed.csv")
