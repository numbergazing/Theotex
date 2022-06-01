from theotex import SeptuagintBook, NewTestamentBook
from navigation import nb_chapters_for


def test_nb_chapters_for():
    expected_result = [50, 28]
    data = [nb_chapters_for(SeptuagintBook.GENESIS), nb_chapters_for(NewTestamentBook.MATTHEW)]
    assert data == expected_result
