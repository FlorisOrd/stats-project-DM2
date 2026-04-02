import pandas as pd
import matplotlib.pyplot as plt


data=pd.read_csv("data/raw/physical_wimp_50GeV.csv")

energy=data.iloc[:,0]
rate=data.iloc[:,1]

plt.figure(figsize=(7,5))
plt.plot(energy,rate,marker="o")
plt.xlabel("Recoil energy")
plt.ylabel("Differential rate")
plt.title("Test recoil spectrum")
plt.grid(True)
plt.tight_layout()

plt.savefig("plots/test_spectrum_test.png",dpi=300)

print("Plot saved to plots/test_spectrum.png")

plt.show()