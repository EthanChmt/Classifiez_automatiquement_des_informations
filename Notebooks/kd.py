import matplotlib.pyplot as plt

labels = ['Non', 'Oui']
sizes = [1233, 237]
colors = ['blue', 'red']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("A quitté l'entreprise")
plt.show()