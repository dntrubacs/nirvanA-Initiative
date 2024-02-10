""" Moudles used to clean data from the aviation quiz."""


import pandas as pd


def return_question(data_path: str, index: int) -> str:
    """

    Args:
        data_path:
        index:

    Returns:

    """
    dataframe = pd.read_csv(data_path)
    print(dataframe)


if __name__ == '__main__':
    import os
    os.chdir('C/Users/Dani/Documents/pythonProject/nirvanA Initiative/')

    # Point to the local server
    return_question(data_path='Aviation Quiz.csv', index=0)