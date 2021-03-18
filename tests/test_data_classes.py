from src.data_classes import Play, Act, Scene, Line


# Play


def test_play_init(play_root):
    play = Play(play_root)
    assert play.root_node == play_root


def test_play_repr(play):
    assert repr(play) == f"Play({play.title})"


def test_play_title(play):
    assert play.title == "A Midsummer Night’s Dream"


def test_play_acts(play):
    act_numbers = [act.number for act in play.acts]
    assert act_numbers == list(range(1, 6))


# Act


def test_act_init(act_root):
    act = Act(act_root)
    assert act.root_node == act_root


def test_act_repr(act):
    assert repr(act) == f"Act({act.number})"


def test_act_number(act):
    assert act.number == 1


def test_act_scenes(act):
    scene_numbers = [scene.number for scene in act.scenes]
    assert scene_numbers == [1, 2]


# Scene


def test_scene_init(scene_root):
    scene = Scene(scene_root)
    assert scene.root_node == scene_root


def test_scene_repr(scene):
    assert repr(scene) == f"Scene({scene.number})"


def test_scene_number(scene):
    assert scene.number == 1


def test_lines(scene):
    line_numbers = [line.number for line in scene.lines if line.line_type == "speech"]
    expected_line_numbers = set(range(1, 258)) - {
        193,
        200,
    }  # in the original text, lines 193 and 200 spill over until a newline, thus folger's xml does not consider them to be true new lines
    assert set(line_numbers) == expected_line_numbers


# Line


def test_line_init(line_root):
    line = Line(line_root)
    assert line.root_node == line_root


def test_line_repr(line_direction, line):
    assert repr(line_direction) == f"Line({line_direction.text})"
    assert repr(line) == f"Line({line.text})"


def test_line_type(line_direction, line):
    assert line_direction.line_type == "direction"
    assert line.line_type == "speech"


def test_line_subtype(line_direction, line):
    assert line_direction.line_subtype == "entrance"
    assert line.line_subtype == "verse"


def test_line_who(line_direction, line):
    assert (
        line_direction.who
        == "#Theseus_MND #Hippolyta_MND #Philostrate_MND #ATTENDANTS_MND"
    )
    assert line.who == "#Theseus_MND"


def test_line_number(line_direction, line):
    assert line_direction.number == "SD 1.1.0"
    assert line.number == 1


def test_line_text(line_direction, line):
    assert (
        line_direction.text == "Enter Theseus, Hippolyta, and Philostrate, with others."
    )
    assert line.text == "Now, fair Hippolyta, our nuptial hour"
