from src.postprocessing import (
    replace_title_single_quote,
    split_directions_by_who,
    parse_name,
    parse_names,
    add_throughline_numbers,
    remove_empty_text,
    postprocess_play,
)


def test_replace_title_single_quote():
    play_data = [{"title": "Dream’s"}]
    expected = [{"title": "Dream's"}]
    assert list(replace_title_single_quote(play_data)) == expected


def test_split_directions_by_who():
    play_data = [
        {"title": "title", "who": "Person1,Person2"},
        {"title": "title", "who": "Person3"},
    ]
    expected = [
        {"title": "title", "who": "Person1"},
        {"title": "title", "who": "Person2"},
        {"title": "title", "who": "Person3"},
    ]
    assert list(split_directions_by_who(play_data)) == expected


def test_parse_name():
    assert parse_name("#name") == "name"
    assert parse_name("name") == "name"


def test_parse_names():
    play_data = [{"who": "Person1 Person2 Person3"}, {"who": "Person4"}]
    expected = [{"who": "Person1,Person2,Person3"}, {"who": "Person4"}]
    assert list(parse_names(play_data)) == expected


def test_add_throughline_numbers():
    play_data = [{"number": -1}, {"number": -1}, {"number": -1}]
    expected = [{"number": 1}, {"number": 2}, {"number": 3}]
    assert list(add_throughline_numbers(play_data)) == expected


def test_remove_empty_text():
    play_data = [{"text": "not empty"}, {"text": ""}]
    expected = [{"text": "not empty"}]
    assert list(remove_empty_text(play_data)) == expected


def test_postprocess_play():
    play_data = [
        {"title": "title", "text": ""},
        {
            "title": "Dream’s",
            "who": "#Person1 #Person2",
            "number": -1,
            "text": "not empty",
        },
    ]
    expected = [
        {"title": "Dream's", "who": "Person1", "number": 1, "text": "not empty"},
        {"title": "Dream's", "who": "Person2", "number": 1, "text": "not empty"},
    ]
    assert list(postprocess_play(play_data)) == expected
