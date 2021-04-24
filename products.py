products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # quit
		break
	
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
# p = [name, price] 9-14行 第一種簡寫方式
# products.append([name, price]) 9-14行 更進階簡寫方式
	products.append(p)

print(products)

for p in products:
	print(p[0], '的價格是', p[1])