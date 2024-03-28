from colorprint import PrintGREEN, PrintRED, PrintCYAN, PrintYELLOW
from productcategory import ProductCategory
from product import Product
from commands import Command, PrintCommands, CategoryOrProduct
from shop import Shop

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

	shop = Shop()

	while True:
		PrintCommands()
		PrintGREEN("Введіть команду:")
		command = int(input())

		if command == Command.LoadData.value:
			shop.LoadData()
		elif command == Command.NewCategoryOrProduct.value:
			if CategoryOrProduct() :
				PrintYELLOW("Введіть назву категорії: ")
				categoryName = input()
				productCategory = ProductCategory(0, categoryName)
				shop.CreateCategory(productCategory)
			else:
				PrintYELLOW("Введіть id категорії, до якої потрібно додати продукт: ")
				categoryId = int(input())
				if shop.SearchCategory(categoryId, False):
					PrintYELLOW("Введіть назву продукту: ")
					productName = input()
					PrintYELLOW("Введіть ціну товару" + productName + ": ")
					productPrice = float(input())
					PrintYELLOW("Введіть кількість продукту" + productName + ": ")
					productAmount = int(input())
					newProduct = Product(0, categoryId, productName, productPrice, productAmount)
					shop.CreateProduct(newProduct)
		elif command == Command.EditCategoryOrProduct.value:
			if CategoryOrProduct() :
				PrintYELLOW("Введіть id категорії, яку потрібно змінити: ")
				categoryId = int(input())
				shop.EditCategory(categoryId)
			else:
				PrintYELLOW("Введіть id продукту, який потрібно змінити: ")
				productId = int(input())
				shop.EditProduct(productId)
		elif command == Command.DeleteCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно видалити: ")
				categoryId = int(input())
				shop.DeleteCategory(categoryId)
			else:
				PrintYELLOW("Введіть id продукту, який потрібно видалити: ")
				productId = int(input())
				shop.DeleteProduct(productId)
		elif command == Command.SearchCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно знайти: ")
				categoryId = int(input())
				shop.SearchCategory(categoryId, True)
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно знайти: ")
				productId = int(input())
				shop.SearchProduct(productId, True)
		elif command == Command.ListOfCategoriesOrProducts.value:
			if CategoryOrProduct():
				shop.PrintListOfCategories()
			else:
				PrintYELLOW("Введіть id категорії: ")
				categoryId = int(input())
				shop.PrintListOfProductsInCategory(categoryId)
		elif command == Command.Exit.value:
			exit()
		else:
			PrintRED("Unknown command")