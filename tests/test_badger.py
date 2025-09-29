import pathlib
import tempfile

from badger import add_badges, BADGES

def test_add_badges_inserts_badges(tmp_path: pathlib.Path):
    readme = tmp_path / "README.md"
    readme.write_text("Hello", encoding="utf-8")

    add_badges(readme)

    lines = readme.read_text(encoding="utf-8").splitlines()
    assert lines[:len(BADGES)] == BADGES
    assert "Hello" in lines
