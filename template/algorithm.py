from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

HERE = Path(__file__).resolve().parent


def simulate(n_steps=120, dt=0.05):
    t = np.arange(n_steps) * dt
    return np.column_stack([np.cos(t), np.sin(t)])


def save_plot(xy, path):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(xy[:, 0], xy[:, 1])
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    fig.savefig(path, dpi=120, bbox_inches="tight")
    plt.close(fig)


def save_gif(xy, path, fps=20):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    (trail,) = ax.plot([], [], lw=1.5)
    (dot,) = ax.plot([], [], "o")

    def update(i):
        trail.set_data(xy[: i + 1, 0], xy[: i + 1, 1])
        dot.set_data([xy[i, 0]], [xy[i, 1]])
        return trail, dot

    anim = FuncAnimation(fig, update, frames=len(xy), blit=True)
    anim.save(path, writer=PillowWriter(fps=fps))
    plt.close(fig)


if __name__ == "__main__":
    xy = simulate()
    save_plot(xy, HERE / "plot.png")
    save_gif(xy, HERE / "demo.gif")
