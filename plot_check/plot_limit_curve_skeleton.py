from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

input=Path("data/processed/TEST_NUMBERS_FOR_PLOT.csv")
output=Path("plots/limit_curve_test.png")

if not input.exists():
    print(f"Missing input file: {input}")
    print("insert in (input) actual csv pls, then run this script again.")
    raise SystemExit

data=pd.read_csv(input,comment="#")
mass=data["mass"]
upper_limit=data["upper_limit"]

plt.figure(figsize=(7.5,5.5))
plt.plot(mass,upper_limit,marker="o",linewidth=1.8,markersize=5)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("WIMP mass [GeV/C^2?]")
plt.ylabel("90% upper limit on cross section")
plt.title("Test limit curve")
plt.grid(True,which="both",alpha=0.35)
plt.tight_layout()
plt.savefig(output,dpi=300)

print(f"Plot saved to {output}")
plt.show()