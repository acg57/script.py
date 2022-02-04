#!/usr/bin/python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

print ('Number of arguments: %i arguments' % len(sys.argv))
print ('Argument List:' + str(sys.argv))

data = pd.read_csv(sys.argv[1],delimiter=',')

intervalos = range(round(min(data['y'])), round(max(data['y'])))
sb.displot(data['y'], color='#F2AB6D', bins=intervalos, kde=True) #creamos el gráfico en Seaborn

#configuramos en Matplotlib
plt.xticks(intervalos)
plt.ylabel('Dias acumulados')
plt.xlabel('Lluvia (mm)')
plt.title('Histograma de lluvia')
