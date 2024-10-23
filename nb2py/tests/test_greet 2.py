import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from converted import greet_2


def test_greet():
    assert greet_2.greet() == "hello"
