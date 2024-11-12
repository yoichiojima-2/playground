from subprocess import run
from pathlib import Path
import re
from datetime import datetime


openai_rust_bin = Path("~/Developer/repo/openai-rust/target/release/openai-rust")
history_dir = Path("./history")


def extract_python_code(stdout: str) -> str:
    if match := re.search(r"```python\n(.*)```", stdout, re.DOTALL):
        return match.group(1)
    else:
        return stdout


def improve_code(path: Path) -> None:
    print("improving code...")
    output = run(f"python {path}", shell = True, encoding="utf-8").stdout
    prompt = (
        "i will give you a result of a python script that you previously generated. "
        "please improve a code in a creative way that you can imagine. "
        "your response will be executed as it is. make sure it is executable. "
        "and please leave comments to let reader know what you tried to do. "
        f"result-output: {output}"
    )
    command = f"{openai_rust_bin} code \"{prompt}\""
    print(command)

    stdout = run(command, shell=True, capture_output=True, encoding="utf-8").stdout
    refined_file = history_dir / f"{datetime.now().strftime("%Y%m%d%H%M%S")}.py"
    refined_file.write_text(extract_python_code(stdout))
    print("saved improved code...")

    return refined_file


def main():
    first_prompt = (
        "i will let you use my python environment. "
        "write a code that does something impressive. i'll give you stdout when executed. "
        "make sure your response is a executable python code otherwise it does not work."
    )

    command = f"{openai_rust_bin} code \"{first_prompt}\""

    stdout = run(command, shell=True, capture_output=True, encoding="utf-8").stdout

    history_dir.mkdir(parents=True, exist_ok=True)
    path = history_dir / f"{datetime.now().strftime("%Y%m%d%H%M%S")}.py"
    path.write_text(extract_python_code(stdout))

    while True:
        path = improve_code(path)


main()