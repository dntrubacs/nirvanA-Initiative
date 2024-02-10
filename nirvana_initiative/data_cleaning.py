""" Moudles used to clean data from the aviation quiz."""

import pandas as pd


def return_question(data_path: str, index: int) -> str:
    """

    Args:
        data_path: Path to data file.
        index: Number of question wanted.

    Returns:

    """
    dataframe = pd.read_csv(data_path)
    return dataframe['question'][index]


if __name__ == '__main__':
    import os
    os.chdir('C:/Users/Dani/Documents/pythonProject/nirvanA Initiative/')

    # Point to the local server
    debug_answer = return_question(data_path='Aviation Quiz.csv', index=99)
    print(debug_answer)
