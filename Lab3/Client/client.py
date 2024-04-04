import socket
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
	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.connect((host, port))

	while True:
		doWeNeedCatch = True
		PrintCommands()
		PrintGREEN("Введіть команду:")
		command = int(input())
		query = str(command)

		if command == Command.LoadData.value:
			s.send(query.encode())
		elif command == Command.NewCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть назву категорії: ")
				categoryName = input()
				query = query + "|1|" + categoryName
				s.send(query.encode())
			else:
				PrintYELLOW("Введіть id категорії, до якої потрібно додати продукт:")
				categoryId = int(input())
				query = query + "|2|" + str(categoryId)
				s.send(query.encode())
				result = s.recv(1024).decode().split('|')
				doWeNeedCatch = False
				if result[0] == "True":
					PrintYELLOW("Введіть назву продукта: ")
					productName = input()
					PrintYELLOW("Введіть ціну товару " + productName + ": ")
					productPrice = float(input())
					PrintYELLOW("Введіть кількість продукту " + productName + ": ")
					productAmount = int(input())
					query = "2|2|" + str(categoryId) + "|" + productName + "|" + str(productPrice) + "|" + str(productAmount)
					s.send(query.encode())
					doWeNeedCatch = True

		elif command == Command.EditCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно змінити:")
				сategoryId = int(input())
				query = query + "|1|" + str(сategoryId)
				s.send(query.encode())
				result = s.recv(1024).decode().split('|')
				doWeNeedCatch = False
				if result[0] == "True":
					PrintYELLOW("Введіть нову назву категорії (categoryName): ")
					newCategoryName = input()
					query = "3|1|" + str(сategoryId) + "|" + newCategoryName
					s.send(query.encode())
					doWeNeedCatch = True
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно змінити:")
				productId = int(input())
				query = query + "|2|" + str(productId)
				s.send(query.encode())
				result = s.recv(1024).decode().split('|')
				doWeNeedCatch = False
				if result[0] == "True":
					PrintYELLOW("Щоб ви хотіли змінити? \n" +
								"1 - назва продукту \n" +
								"2 - ціну товару \n" +
								"3 - кількість продукту на складі")
					commandEditProduct = int(input())
					isCorrectCommand = True
					query = "3|1|" + str(productId) + "|" + str(commandEditProduct) + "|"
					if commandEditProduct == 1:
						PrintYELLOW("Введіть нове ім'я продукту: ")
						productName = input()
						query = query + productName
					elif commandEditProduct == 2:
						PrintYELLOW("Введіть нову ціну товару: ")
						productPrice = input()
						query = query + productPrice
					elif commandEditProduct == 3:
						PrintYELLOW("Введіть нову кількість продукту на складі: ")
						productAmount = input()
						query = query + productAmount
					else:
						PrintRED("Unknown command")
						isCorrectCommand = False
					if isCorrectCommand:
						s.send(query.encode())
						doWeNeedCatch = True
						doWeNeedCatch = True
		elif command == Command.DeleteCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно видалити: ")
				сategoryId = int(input())
				query = query + "|1|" + str(сategoryId)
				s.send(query.encode())
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно видалити: ")
				productId = int(input())
				query = query + "|2|" + str(productId)
				s.send(query.encode())
		elif command == Command.SearchCategoryOrProduct.value:
			if CategoryOrProduct():
				PrintYELLOW("Введіть id категорії, яку потрібно знайти:")
				categoryId = int(input())
				query = query + "|1|" + str(categoryId)
				s.send(query.encode())
			else:
				PrintYELLOW("Введіть ID продукту, який потрібно знайти:")
				productId = int(input())
				query = query + "|2|" + str(productId)
				s.send(query.encode())
		elif command == Command.ListOfCategoriesOrProducts.value:
			if CategoryOrProduct():
				query = query + "|1"
				s.send(query.encode())
			else:
				PrintYELLOW("Введіть id категорії: ")
				categoryId = int(input())
				query = query + "|2|" + str(categoryId)
				s.send(query.encode())
		elif command == Command.Exit.value:
			s.send(query.encode())
			exit()

		if doWeNeedCatch:
			result = s.recv(1024).decode().split('|')
		PrintResult(result)