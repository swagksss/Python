import socket
from colorprint import PrintGREEN, PrintRED, PrintCYAN, PrintYELLOW
from commands import Command, PrintCommands, CategoryOrProduct
import pika
import threading


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


def startConsumer():
	def callback(ch, method, properties, body):
		if body.decode() == "7":
			exit()
		result = body.decode().split('|')
		PrintResult(result)

	channel.basic_consume(queue='client_queue', on_message_callback=callback, auto_ack=True)
	channel.start_consuming()

if __name__ == '__main__':

	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='client_queue')
	channel.queue_declare(queue='server_queue')


	PrintGREEN("1 -отримати інформацію із сервера \n" +
			   "2 - надіслати запити на сервер")
	PrintGREEN("Введіть команду:")
	command = int(input())
	if(command == 1):
		startConsumer()
	elif command == 2:
		while True:
			doWeNeedCatch = True
			PrintCommands()
			PrintGREEN("Введіть команду:")
			command = int(input())
			query = str(command)

			if command == Command.LoadData.value:
				channel.basic_publish(exchange='', routing_key='server_queue', body=query)
			elif command == Command.NewCategoryOrProduct.value:
				if CategoryOrProduct():
					PrintYELLOW("Введіть назву категорії:")
					categoryName = input()
					query = query + "|1|" + categoryName
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
				else:
					PrintYELLOW("Введіть id категорії, до якої потрібно додати продукт: ")
					categoryId = int(input())
					query = query + "|2|" + str(categoryId)

					PrintYELLOW("Введіть назву продукта: ")
					productName = input()
					PrintYELLOW("Введіть ціну товару " + productName + ": ")
					productPrice = float(input())
					PrintYELLOW("Введіть кількість продукту" + productName + ": ")
					productAmount = int(input())
					query = query + "|" + productName + "|" + str(productPrice) + "|" + str(productAmount)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
			elif command == Command.DeleteCategoryOrProduct.value:
				if CategoryOrProduct():
					PrintYELLOW("Введіть id категорії, яку потрібно видалити: ")
					сategoryId = int(input())
					query = query + "|1|" + str(сategoryId)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
				else:
					PrintYELLOW("Введіть id продукту, який потрібно видалити:")
					productId = int(input())
					query = query + "|2|" + str(productId)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
			elif command == Command.SearchCategoryOrProduct.value:
				if CategoryOrProduct():
					PrintYELLOW("Введіть id категорії, яку потрібно знайти: ")
					categoryId = int(input())
					query = query + "|1|" + str(categoryId)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
				else:
					PrintYELLOW("Введіть ID продукту, який потрібно знайти: ")
					productId = int(input())
					query = query + "|2|" + str(productId)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
			elif command == Command.ListOfCategoriesOrProducts.value:
				if CategoryOrProduct():
					query = query + "|1"
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
				else:
					PrintYELLOW("Введіть id категорії: ")
					categoryId = int(input())
					query = query + "|2|" + str(categoryId)
					channel.basic_publish(exchange='', routing_key='server_queue', body=query)
			elif command == Command.Exit.value:
				channel.basic_publish(exchange='', routing_key='server_queue', body=query)
				exit()
			else:
				PrintRED("Unknown command")

			'''
			if doWeNeedCatch:
				result = s.recv(1024).decode().split('|')
			PrintResult(result)'''