from src.data_classes import Play, Act, Scene, Line


# Play

# Act 

# Scene

# Line

def test_line_init(line_root):
    line = Line(line_root)
    assert line.root_node == line_root

def test_line_repr(line_direction, line):
    assert repr(line_direction) == f"Line({line_direction.text})"
    assert repr(line) == f"Line({line.text})"
    

def test_line_kind(line_direction, line):
    assert line_direction.kind == "direction"
    assert line.kind == "speech"
    

def test_line_who(line_direction, line):
    assert line_direction.who == "#Theseus_MND #Hippolyta_MND #Philostrate_MND #ATTENDANTS_MND"
    assert line.who == "#Theseus_MND"

def test_line_number(line_direction, line):
    assert line_direction.number == None
    assert line.number == 1
    

def test_line_text(line_direction, line):
    assert line_direction.text == "Enter Theseus, Hippolyta, and Philostrate, with others."
    assert line.text == "Now, fair Hippolyta, our nuptial hour"
    