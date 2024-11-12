import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from converted import greet


def test_greet():
    assert greet.greet() == "hello"
