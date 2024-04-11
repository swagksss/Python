import Pyro4
from colorprint import PrintGREEN, PrintRED, PrintCYAN, PrintYELLOW
from commands import Command, PrintCommands, CategoryOrProduct

def PrintResult (result) :
	if result[0] == 'G':
		PrintGREEN(result[1])
	elif result[0] == 'Y':
		PrintYELLOW(result[1])
	elif result[0] == 'R':
		PrintRED(result[1])
	elif result[0] == 'C':
		PrintCYAN(result[1])
	else:
		print("Помилка під час передачі даних")


if __name__ == '__main__':

	ns = Pyro4.locateNS()
	uri = ns.lookup('shop')
	shop = Pyro4.Proxy(uri)

	while True:
		doWeNeedCatch = True
		PrintCommands()
		PrintGREEN("Введіть команду:")
		command = int(input())
		query = str(command)

		if command == Command.LoadData.value:
			result = shop.LoadData()

		elif command == Command.NewCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть назву категорії: ")
				categoryName = input()
				result = shop.CreateCategory(categoryName)
			else:
				PrintYELLOW("Введіть id категорії, до якої потрібно додати продукт: ")
				categoryId = int(input())
				result = shop.SearchCategory(categoryId, False)
				if result == "":
					PrintYELLOW("Введіть назву продукта: ")
					productName = input()
					PrintYELLOW("Введіть ціну товару" + productName + ": ")
					productPrice = float(input())
					PrintYELLOW("Введіть кількість продукту " + productName + ": ")
					productAmount = int(input())
					result = shop.CreateProduct(categoryId, productName, productPrice, productAmount)
		elif command == Command.EditCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно змінити: ")
				сategoryId = int(input())
				result = shop.SearchCategory(сategoryId, False)
				if result == "":
					PrintYELLOW("Введіть нове ім'я категорії (categoryName): ")
					newCategoryName = input()
					result = shop.EditCategory(сategoryId, newCategoryName)
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно змінити: ")
				productId = int(input())
				result = shop.SearchProduct(productId, False)
				if result == "":
					PrintYELLOW("Щоб ви хотіли змінити? \n" +
								"1 -назва продукту \n" +
								"2 - ціну товару \n" +
								"3 - кількість продукту на складі")
					commandEditProduct = int(input())
					if commandEditProduct == 1:
						PrintYELLOW("Введіть нове ім'я продукту:")
						productName = input()
						result 	= shop.EditProduct(productId, commandEditProduct, productName)
					elif commandEditProduct == 2:
						PrintYELLOW("Введіть нову ціну товару:")
						productPrice = input()
						result 	= shop.EditProduct(productId, commandEditProduct, productPrice)
					elif commandEditProduct == 3:
						PrintYELLOW("Введіть нову кількість продукту на складі: ")
						productAmount = input()
						result 	= shop.EditProduct(productId, commandEditProduct, productAmount)
					else:
						PrintRED("Unknown command")
		elif command == Command.DeleteCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно видалити: ")
				сategoryId = int(input())
				result = shop.DeleteCategory(сategoryId)
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно видалити: ")
				productId = int(input())
				result = shop.DeleteProduct(productId)
		elif command == Command.SearchCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно знайти:")
				categoryId = int(input())
				result = shop.SearchCategory(categoryId, True)
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно знайти: ")
				productId = int(input())
				result = shop.SearchProduct(productId, True)
		elif command == Command.ListOfCategoriesOrProducts.value:
			if CategoryOrProduct():
				result = shop.PrintListOfCategories()
			else:
				PrintYELLOW("Введіть id категорії: ")
				categoryId = int(input())
				result = shop.PrintListOfProductsInCategory(categoryId)
		elif command == Command.Exit.value:
			exit()

		PrintResult(result.split('|'))