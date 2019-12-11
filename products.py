products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)
# print(products[0][0]) #弄懂每一個層次的意涵（例：第一層中括弧切點是品項、第二層是名稱與價格）

for p in products:
	print (p) #列印所有組合（所有第一層）
	print(p[0]) #列印組合內的第一格（第二層的第一格，就是名稱）

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + '，' + p[1] + '\n')
