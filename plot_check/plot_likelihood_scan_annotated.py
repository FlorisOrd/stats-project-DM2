import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("data/processed/likelihood_scan.csv")

signal_strength=data["signal_strength"]
llr=data["llr"]

min_index=llr.idxmin()
x_min=signal_strength[min_index]
y_min=llr[min_index]

plt.figure(figsize=(8,5))
plt.plot(signal_strength,llr,marker="o",markersize=4,label="Likelihood scan")
plt.scatter(x_min,y_min,s=80,label="Minimum")

plt.xlabel("Signal strength")
plt.ylabel("LLR")
plt.title("Likelihood scan with minimum")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("plots/likelihood_scan_annotated.png",dpi=300)

print("Minimum signal strength =",x_min)
print("Minimum LLR =",y_min)
print("Plot saved to plots/likelihood_scan_annotated_test.png")

plt.show()