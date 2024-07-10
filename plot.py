import matplotlib.pyplot as plt


imagens = ['img_13.jpg', 'img_09.jpeg', 'img_05.jpg', 'img_04.jpg', 'img_11.jpg', 'img_12.jpg']
acuracias = [50.00, 0.00, 100.00, 83.33, 0.00, 20.00]
saliências = [6.15, 12.22, 10.45, 4.76, 22.43, 5.21]


plt.figure(figsize=(12, 12))

#plt.subplot(1, 2, 1)
#plt.bar(imagens, acuracias, color='skyblue')
plt.scatter(imagens,acuracias,color='blue')
plt.xlabel('Imagens de entrada')
plt.ylabel('Acurácia (%)')
plt.title('Acurácia das Legendas Geradas pela IA')
plt.xticks(rotation=90)


#plt.subplot(1, 2, 2)
#plt.bar(imagens, saliências, color='salmon')
plt.bar(imagens,acuracias,color='red')
plt.xlabel('Imagens de entrada')
plt.ylabel('Saliência (%)')
plt.title('Porcentagem de Saliência')
plt.xticks(rotation=90)


plt.show()