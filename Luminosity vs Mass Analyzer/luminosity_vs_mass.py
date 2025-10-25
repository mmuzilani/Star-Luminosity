#!/usr/bin/env python3
"""
Luminosity vs Mass Analyzer
Author: Md. Mahiuddin Zilani (example)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def read_csv(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)
    required = {"Mass_solar", "Luminosity_solar"}
    if not required.issubset(df.columns):
        print(f"Error: CSV must contain columns: {required}")
        print("Your columns:", list(df.columns))
        sys.exit(1)
    # drop rows with missing or non-positive values
    df = df.dropna(subset=["Mass_solar", "Luminosity_solar"])
    df = df[(df["Mass_solar"] > 0) & (df["Luminosity_solar"] > 0)]
    return df

def power_law_fit(masses, luminosities):
   
    logM = np.log10(masses)
    logL = np.log10(luminosities)
    a, A = np.polyfit(logM, logL, 1)   # slope a and intercept A
    k = 10**A
    return k, a

def plot_data_and_fit(masses, luminosities, k, a, output_prefix="luminosity_mass"):
    # Linear plot (L vs M)
    plt.figure(figsize=(7,5))
    plt.scatter(masses, luminosities)
    # plot theoretical fit curve for visualization
    m_fit = np.linspace(min(masses)*0.9, max(masses)*1.1, 200)
    l_fit = k * m_fit**a
    plt.plot(m_fit, l_fit, label=f"Fit: L = {k:.2g} * M^{a:.2f}")
    plt.xlabel("Mass (M / M☉)")
    plt.ylabel("Luminosity (L / L☉)")
    plt.title("Luminosity vs Mass (linear)")
    plt.legend()
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.tight_layout()
    plt.savefig(output_prefix + "_linear.png", dpi=150)
    print(f"Saved: {output_prefix + '_linear.png'}")
    plt.close()

    # Log-Log plot
    plt.figure(figsize=(7,5))
    plt.scatter(masses, luminosities)
    plt.plot(m_fit, l_fit, label=f"Fit: L = {k:.2g} * M^{a:.2f}")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Mass (M / M☉) [log scale]")
    plt.ylabel("Luminosity (L / L☉) [log scale]")
    plt.title("Luminosity vs Mass (log-log)")
    plt.legend()
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.tight_layout()
    plt.savefig(output_prefix + "_loglog.png", dpi=150)
    print(f"Saved: {output_prefix + '_loglog.png'}")
    plt.close()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Luminosity vs Mass analyzer")
    parser.add_argument("--csv", default="stars_data.csv", help="CSV file with columns Mass_solar,Luminosity_solar")
    args = parser.parse_args()

    df = read_csv(args.csv)
    masses = df["Mass_solar"].values
    luminosities = df["Luminosity_solar"].values

    k, a = power_law_fit(masses, luminosities)
    print(f"Fitted power-law: L ≈ {k:.3g} * M^{a:.3f}")

    # For comparison show theoretical 3.5
    print("Compare theoretical exponent a = 3.5 (main-sequence approximation).")

    # Save plots
    plot_data_and_fit(masses, luminosities, k, a)

    # Optionally show the plot (uncomment the next lines if you want an interactive window)
    # import matplotlib.pyplot as plt
    # plt.show()

if __name__ == "__main__":
    main()
