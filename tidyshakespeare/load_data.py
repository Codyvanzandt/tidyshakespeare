import pandas
import glob
import pkg_resources

def load(play_name):
    play_data_frames = list()
    for play_name in _get_file_name(play_name):
        play_file = play_name if play_name.endswith(".csv") else play_name + ".csv"
        with pkg_resources.resource_stream("tidyshakespeare", f"data/{play_file}") as fp:
            play_data_frames.append(pandas.read_csv(fp, delimiter="\t", quotechar="|", index_col=None, header=0))
    return pandas.concat(play_data_frames, axis=0, ignore_index=True)
    
def _get_file_name(play_name):
    if play_name == "all":
        return pkg_resources.resource_listdir("tidyshakespeare", "data/")
    else:
        return [ play_name, ]