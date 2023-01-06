import os


class Config:
    dataset = "Reddit"
    #dataset = "iSarcasm"
    
    if dataset == "Reddit":
        input_file_path = os.path.join("..", "data", dataset, "train-balanced-sarcasm.csv")
        test_file_path = os.path.join("..", "data", dataset, "test-balanced.csv")
        comment_col_name = "comment"
        label_col_name = "label"
        preprocessed_file_path = os.path.join("..", "data", dataset, "preprocessed.csv")
    elif dataset == "iSarcasm":
        input_file_path = os.path.join("..", "data", dataset + "Eval", "train.csv")
        test_file_path = os.path.join("..", "data", dataset + "Eval", "test.csv")
        comment_col_name = "tweet"
        label_col_name = "sarcastic"
        preprocessed_file_path = os.path.join("..", "data", dataset + "Eval", "preprocessed.csv")
