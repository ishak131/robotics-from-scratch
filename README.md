# robotics-from-scratch

[![check](https://github.com/ishak131/robotics-from-scratch/actions/workflows/check.yml/badge.svg)](https://github.com/ishak131/robotics-from-scratch/actions/workflows/check.yml)

Core robotics algorithms written from first principles in Python, using only NumPy and Matplotlib. Each one comes with a short write-up and a GIF or plot of it running.

| Topic | What's in it |
|---|---|
| [math](math/) | Rotations, rigid-body transforms, quaternions: the geometry everything else is built on |
| [kinematics](kinematics/) | Forward and inverse kinematics for arms and mobile robots |
| [planning](planning/) | Graph search, sampling-based planners, trajectory generation |
| [estimation](estimation/) | Kalman filters, particle filters, localization, mapping, SLAM |
| [control](control/) | PID, LQR, path tracking, MPC |

## Layout

Each algorithm gets its own folder inside its topic:

```
planning/
├── README.md         index of every algorithm in this topic
└── a_star/
    ├── README.md     what it solves, how it works, how to run it
    ├── a_star.py     the implementation; running it regenerates the demo
    └── demo.gif      or plot.png
```

Every algorithm folder is self-contained: no shared library, so each one can be read on its own.

## Running

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python <topic>/<algorithm>/<algorithm>.py
```

## Adding an algorithm

1. `cp -r template <topic>/<algorithm>` and rename `algorithm.py` to `<algorithm>.py`.
2. Implement it and have the script save `demo.gif` or `plot.png` next to itself.
3. Fill in the README and add a row to `<topic>/README.md`.
4. Run `python scripts/check_repo.py`. CI runs the same check on every push: each algorithm folder needs a README, a GIF or image, and a link from its topic index.
