import os


class Config:

    def __init__(self, dataset):
        """
        Parameters
        ----------
        dataset     Select the dataset ["Reddit", "iSarcasm"]
        """
        if dataset == "iSarcasm" or dataset == "iSarcasmEval":
            self.dataset = "iSarcasmEval"
        elif dataset == "Reddit":
            self.dataset = "Reddit"
        else:
            assert "Invalid dataset selected, Valid = [Reddit, iSarcasm]"
        
        # Path to datasets
        file_dir = os.path.join("..", "data", self.dataset)

        # Store dataset specific attributes
        if self.dataset == "Reddit":
            self.input_file_path = os.path.join(file_dir, "train-balanced-sarcasm.csv")
            self.test_file_path = os.path.join(file_dir, "test-balanced.csv")
            self.comment_col_name = "comment"
            self.label_col_name = "label"
        else:
            self.input_file_path = os.path.join(file_dir, "train.csv")
            self.test_file_path = os.path.join(file_dir, "test.csv")
            self.comment_col_name = "tweet"
            self.label_col_name = "sarcastic"

        self.preprocessed_file_path = os.path.join(file_dir, "preprocessed.csv")
