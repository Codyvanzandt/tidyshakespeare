import pandas
import glob
import pkg_resources


def load(*play_names):
    """Returns a pandas dataframe for one or more play

        Args:
            *play_names: one or more of the following play names: ['all', 'a-midsummer-nights-dream', 'alls-well-that-ends-well', 'antony-and-cleopatra', 'as-you-like-it', 'coriolanus', 'cymbeline', 'hamlet', 'henry-iv-part-1', 'henry-iv-part-2', 'henry-v', 'henry-vi-part-1', 'henry-vi-part-2', 'henry-vi-part-3', 'henry-viii', 'julius-caesar', 'king-john', 'king-lear', 'loves-labors-lost', 'macbeth', 'measure-for-measure', 'much-ado-about-nothing', 'othello', 'pericles', 'richard-ii', 'richard-iii', 'romeo-and-juliet', 'the-comedy-of-errors', 'the-merchant-of-venice', 'the-merry-wives-of-windsor', 'the-taming-of-the-shrew', 'the-tempest', 'the-two-gentlemen-of-verona', 'the-winters-tale', 'timon-of-athens', 'titus-andronicus', 'troilus-and-cressida', 'twelfth-night']

        Returns:
            A pandas dataframe with the lines for one or more plays

        Examples:
            >>> load("hamlet")
            >>> load("hamlet", "a-midsummer-nights-dream")
            >>> load("all")
     """
    play_data_frames = list()
    for play_name in _get_file_name(*play_names):
        play_file = play_name if play_name.endswith(".csv") else play_name + ".csv"
        with pkg_resources.resource_stream(
            "tidyshakespeare", f"data/{play_file}"
        ) as fp:
            play_data_frames.append(
                pandas.read_csv(
                    fp, delimiter="\t", quotechar="|", index_col=None, header=0
                )
            )
    return pandas.concat(play_data_frames, axis=0, ignore_index=True)


def _get_file_name(*play_names):
    if play_names == ["all",]:
        return pkg_resources.resource_listdir("tidyshakespeare", "data/")
    else:
        return list(play_names)

import os
print( sorted(list( play.rsplit(".",1)[0] for play in os.listdir("data/csv"))))