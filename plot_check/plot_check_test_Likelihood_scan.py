import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/processed/likelihood_scan.csv")

x=data["signal_strength"]
y = data["llr"]

plt.figure(figsize=(7, 5))
plt.plot(x, y, marker="o")
plt.xlabel("Signal strength")
plt.ylabel("LLR")
plt.title("Likelihood scan")
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/likelihood_scan_test.png",dpi=300)
print("Plot saved to plots/TEST/likelihood_scan_test.png")

plt.show()