import matplotlib.pyplot as plt

# Definisci le coordinate dei 2 punti (diagonali)
x0, y0 = 0.572, 0.55
x1, y1 = 0.474, 0.119
# Calcola le coordinate dei vertici del rettangolo
x2, y2 = x0, y1  # Angolo in alto a sinistra
x3, y3 = x1, y0  # Angolo in basso a destra

# Crea il grafico
plt.figure(figsize=(10, 6))

# Disegna il rettangolo
plt.plot([x0, x2, x1, x3, x0], [y0, y2, y1, y3, y0], color='blue')

# Disegna i punti
plt.scatter([x0, x1], [y0, y1], color='red')
plt.text(x0, y0, 'x0', fontsize=8, ha='left')
plt.text(x1, y1, 'x1', fontsize=8, ha='left')

# Imposta i limiti degli assi
plt.xlim(0, 1)
plt.ylim(0, 1)

# Titolo e label degli assi
plt.title('Rappresentazione Coordinate e Calcolo Bounding_Box')
plt.xlabel('Asse X')
plt.ylabel('Asse Y')

# Mostra il grafico
plt.grid(True)
plt.show()





