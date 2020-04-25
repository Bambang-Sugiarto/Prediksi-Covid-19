import eksponen as eks
import matplotlib.pyplot as plt
plt.scatter(eks.x,eks.Nx,color='black')
plt.plot(eks.x,eks.Nx,color='blue',linewidth=3)
plt.title('Positif Covid-19 VS Hari')
plt.ylabel('Positif Covid-19')
plt.xlabel('Hari')
plt.show()