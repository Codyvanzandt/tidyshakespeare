from csv import DictReader, DictWriter
from src.constants import CSV_FIELD_NAMES


def read_play_csv(path):
    with open(path, "r") as play_csv_file:
        reader = DictReader(play_csv_file, delimiter="\t", quotechar="|")
        return list(reader)


def write_play_csv(list_of_dicts, path):
    with open(path, "w") as play_csv_file:
        writer = DictWriter(
            play_csv_file, fieldnames=CSV_FIELD_NAMES, delimiter="\t", quotechar="|"
        )
        writer.writeheader()
        writer.writerows(list_of_dicts)


def get_play_data(play):
    def _get_play_data(play):
        for act in play.acts:
            for scene in act.scenes:
                for line in scene.lines:
                    yield {
                        "title": play.title,
                        "act": act.number,
                        "scene": scene.number,
                        "number": line.number,
                        "type": line.line_type,
                        "subtype": line.line_subtype,
                        "who": line.who,
                        "text": line.text,
                    }

    return list(_get_play_data(play))
