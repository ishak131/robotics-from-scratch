import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ["math", "kinematics", "planning", "estimation", "control"]
MEDIA = {".gif", ".png", ".jpg", ".jpeg", ".svg", ".webp"}


def check_algorithm(algo_dir, index_text):
    name = f"{algo_dir.parent.name}/{algo_dir.name}"
    problems = []
    if not (algo_dir / "README.md").is_file():
        problems.append(f"{name}: missing README.md")
    if not any(p.suffix.lower() in MEDIA for p in algo_dir.iterdir()):
        problems.append(f"{name}: no GIF or plot ({', '.join(sorted(MEDIA))})")
    if f"({algo_dir.name}/" not in index_text:
        problems.append(f"{name}: not linked from {algo_dir.parent.name}/README.md")
    return problems


def main():
    problems = []
    checked = 0
    for topic in TOPICS:
        topic_dir = ROOT / topic
        index = topic_dir / "README.md"
        if not index.is_file():
            problems.append(f"{topic}: missing README.md")
            continue
        index_text = "\n".join(
            line for line in index.read_text().splitlines() if not line.lstrip().startswith("<!--")
        )
        for algo_dir in sorted(topic_dir.iterdir()):
            if algo_dir.is_dir() and not algo_dir.name.startswith((".", "_")):
                checked += 1
                problems += check_algorithm(algo_dir, index_text)
    for problem in problems:
        print(problem)
    print(f"{checked} algorithm(s) checked, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
