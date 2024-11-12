import subprocess
import time
from pathlib import Path
import re
from datetime import datetime


openai_rust_bin = Path("~/Developer/repo/openai-rust/target/release/openai-rust")
history_dir = Path(__file__).parent / "history"


def extract_python_code(stdout: str) -> str:
    if match := re.search(r"```python\n(.*)```", stdout, re.DOTALL):
        return match.group(1)
    else:
        return stdout

def run_command(command):
    print(command)
    return subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8").stdout


def improve_code(path: Path) -> None:
    print("improving code...")

    output = run_command(f"python {path}")
    print("output", output)
    prompt = (
        "i will give you a python script that you previously generated and its stdout. "
        "please improve a code in a creative way that you can imagine. "
        "your response will be executed as it is. make sure it is executable. "
        "and please leave comments to let reader know what you tried to do.\n"
        "[your-code]\n"
        f"{path.read_text()}\n"
        "[result-output]\n"
        f"{output}\n"
    )
    command = f"{openai_rust_bin} code \"{prompt}\""
    output = run_command(command)

    refined_file = history_dir / f"{datetime.now().strftime("%Y%m%d%H%M%S")}.py"
    refined_file.write_text(extract_python_code(output))

    print(f"saved improved code: {refined_file}")
    return refined_file


def main():
    first_prompt = (
        "i will let you use my python environment. "
        "write a code that does something impressive. i'll give you stdout when executed. "
        "make sure your response is a executable python code otherwise it does not work."
    )

    command = f"{openai_rust_bin} code \"{first_prompt}\""

    stdout = run_command(command)

    history_dir.mkdir(parents=True, exist_ok=True)
    path = history_dir / f"{datetime.now().strftime("%Y%m%d%H%M%S")}.py"
    path.write_text(extract_python_code(stdout))

    while True:
        path = improve_code(path)
        time.sleep(10)


main()