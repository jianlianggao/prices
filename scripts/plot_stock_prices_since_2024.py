"""Plot the three stock prices in this repository since 2024."""

from pathlib import Path

import matplotlib.pyplot as plt

from prices import TICKERS, load_prices


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "figures"


def plot_prices() -> None:
    """Plot each stock's value relative to its first observed 2024 close."""
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

    fig, ax = plt.subplots(figsize=(12, 7))

    for ticker in TICKERS:
        prices = load_prices(ticker)
        start_value = prices["Adj Close"].iloc[0]
        relative = prices["Adj Close"].div(start_value).mul(100)
        ax.plot(relative.index, relative.values, label=ticker)

    ax.set_title("Stock prices since 2024 (indexed to first observed value = 100)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Index")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    png_path = OUTPUT_DIR / "stock_prices_since_2024.png"
    svg_path = OUTPUT_DIR / "stock_prices_since_2024.svg"
    fig.savefig(png_path, dpi=200)
    fig.savefig(svg_path)
    plt.close(fig)

    print(f"Saved {png_path}")
    print(f"Saved {svg_path}")


if __name__ == "__main__":
    plot_prices()
