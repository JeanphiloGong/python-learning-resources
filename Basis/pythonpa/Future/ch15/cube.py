import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

#设置相关参数和线条粗细
plt.scatter(x_values, y_values,c=y_values, cmap= plt.cm.Reds,
    edgecolor = 'none',s=4)

#设置标题和标题尺寸
plt.title('Cube Numbers', fontsize=14)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Cube of Valuel', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which = 'major', labelsize = 14)

#设置刻度的大小
plt.axis = (0,5000,0,10**11)

plt.show()
plt.savefig('cube_plot.png', bbox_inches='tight')
