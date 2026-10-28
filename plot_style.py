# Defining plot_style.py
# Why?: To keep the plotting variables separate and not clutter the main code
from pathlib import Path
import matplotlib.pyplot as plt

COLORS = {
    "Realized":    "#52514e",
    "HAR":         "#2a78d6",
    "GJR-GARCH":   "#eb6834",
    "LightGBM":    "#1baf7a",
    "Blend":       "#eda100",
    "EWMA":        "#e87ba4",
    "Rolling 22d": "#008300",
}

STYLES = {"HAR": "-", "GJR-GARCH": "--", "LightGBM": "-.", "Blend": ":",
          "EWMA": (0, (5, 1)), "Rolling 22d": (0, (1, 2))}

def use_style():
    plt.style.use(Path(__file__).with_name("volatility.mplstyle"))