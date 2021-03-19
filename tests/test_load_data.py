import pandas
import os
from tidyshakespeare.load_data import load


def test_load_single():
    expected = pandas.read_csv(
        "data/csv/hamlet.csv", delimiter="\t", quotechar="|", index_col=None, header=0
    )
    assert load("hamlet").equals(expected)


def test_load_multiple():
    hamlet = pandas.read_csv(
        "data/csv/hamlet.csv", delimiter="\t", quotechar="|", index_col=None, header=0
    )
    dream = pandas.read_csv(
        "data/csv/a-midsummer-nights-dream.csv",
        delimiter="\t",
        quotechar="|",
        index_col=None,
        header=0,
    )
    expected = pandas.concat([hamlet, dream], axis=0, ignore_index=True)
    assert load("hamlet", "a-midsummer-nights-dream").equals(expected)


def test_load_all():
    file_names = list(os.listdir("data/csv/"))
    play_names = [file_name.split(".")[0] for file_name in file_names]
    dataframes = [
        pandas.read_csv(
            f"data/csv/{play_name}.csv",
            delimiter="\t",
            quotechar="|",
            index_col=None,
            header=0,
        )
        for play_name in play_names
    ]
    expected = pandas.concat(dataframes, axis=0, ignore_index=True)
    assert load("all").equals(expected)
