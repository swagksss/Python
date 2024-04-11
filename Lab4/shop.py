import MySQLdb
from config import url, databaseName, password
from productcategory import ProductCategory
from product import Product
import Pyro4


@Pyro4.expose
class Shop:
	def __init__(self):
		self.mProductCategories = dict()
		self.mProducts = dict()
		self.LoadDataOrNo = False

		#Connect to DB
		self.db = MySQLdb.connect(url, "root", password, databaseName)
		self.cursor = self.db.cursor()

	def Clean(self):
		self.mProductCategories = dict()
		self.mProducts = dict()

	def PrintData(self):
		try:
			returnReplyPrintData = "Y|"
			sql = "SELECT idCategory, nameCategory FROM ProductCategories"
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			for row in results:
				idCategory = row[0]
				nameCategory = row[1]
				returnReplyPrintData = returnReplyPrintData + "Category id: " + str(idCategory) + ", name: " + nameCategory + "\n"

			sql = "SELECT * FROM Products"
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			for row in results:
				idProduct = row[0]
				idCategory = row[1]
				nameProduct = row[2]
				priceProduct = row[3]
				amountProduct = row[4]
				returnReplyPrintData = returnReplyPrintData + "Product id: " + str(idProduct) + ", Category id: " + str(idCategory) + ", name: " + nameProduct + \
							  ", price: " + str(priceProduct) + ", amount: " + str(amountProduct) + "\n"
			return returnReplyPrintData
		except:
			return("R|ПОМИЛКА при отриманні списку категорій або продуктів")

	@Pyro4.expose
	def LoadData(self):
		self.Clean()
		returnReplyLoadData = ""

		sql = "SELECT * FROM ProductCategories"
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		for row in results:
			idCategory = row[0]
			nameCategory = row[1]
			productCategory = ProductCategory(idCategory, nameCategory)
			self.mProductCategories[idCategory] = productCategory

		sql = "SELECT * FROM Products"
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		for row in results:
			idProduct = row[0]
			idCategory = row[1]
			nameProduct = row[2]
			priceProduct = row[3]
			amountProduct = row[4]
			product = Product(idProduct, idCategory, nameProduct, priceProduct, amountProduct)
			self.mProducts[idProduct] = product

		self.LoadDataOrNo = True
		returnReplyLoadData = returnReplyLoadData + self.PrintData()
		return returnReplyLoadData

	@Pyro4.expose
	def CreateCategory(self, categoryName):
		returnReplyCreateCategory = ""
		if self.LoadDataOrNo == False:
			self.LoadData()
		if len(self.mProductCategories) == 0:
			key = 0
		else:
			key = max(self.mProductCategories.keys()) + 1
		productCategory = ProductCategory(key, categoryName)
		self.mProductCategories[key] = productCategory

		sql = "INSERT INTO ProductCategories (idCategory, nameCategory) VALUES (%d, '%s')" % (productCategory.id, productCategory.name)
		try:
			self.cursor.execute(sql)
			self.db.commit()
			returnReplyCreateCategory = returnReplyCreateCategory + "G|Категорія " + productCategory.name + " успішно додана!"
			return returnReplyCreateCategory
		except:
			self.db.rollback()
			return ("R|ПОМИЛКА! Категорія " + productCategory.name + " не додана !")

	@Pyro4.expose
	def CreateProduct(self, categoryId, productName, productPrice, productAmount):
		returnReplyCreateProduct = ""
		if self.LoadDataOrNo == False:
			self.LoadData()
		if len(self.mProducts) == 0:
			key = 0
		else:
			key = max(self.mProducts.keys()) + 1
		product = Product(key, categoryId, productName, productPrice, productAmount)
		self.mProducts[key] = product

		sql = "INSERT INTO Products (idProduct, idCategory, nameProduct, priceProduct, amountProduct) VALUES (%d, %d, '%s', %f, %d)" % (
		product.id, product.idCategory, product.name, product.price, product.amount)
		try:
			self.cursor.execute(sql)
			self.db.commit()
			returnReplyCreateProduct = returnReplyCreateProduct + "G|Продукт " + product.name + " успішно доданий!"
			return returnReplyCreateProduct
		except:
			self.db.rollback()
			return "R|ПОМИЛКА! Продукт " + product.name + " не доданий!"

	@Pyro4.expose
	def EditCategory(self, categoryId, newCategoryName):
		returnReplyEditCategory = ""
		if self.LoadDataOrNo == False:
			self.LoadData()

		if self.SearchCategory(categoryId, False)  == "":
			productCategory_copy = self.mProductCategories[categoryId]
			productCategory_copy.name = newCategoryName
			self.mProductCategories[categoryId] = productCategory_copy

			sql = "UPDATE ProductCategories SET nameCategory = '" + newCategoryName + "'"+ \
				  " WHERE idCategory = " + str(categoryId)
			try:
				self.cursor.execute(sql)
				self.db.commit()
				returnReplyEditCategory = returnReplyEditCategory + "G|Категорія id = " + str(categoryId)  + " успішно відредагована!"
				return returnReplyEditCategory
			except:
				self.db.rollback()
				return "R|ПОМИЛКА! Категорія id = " + str(categoryId) + " не відредагована!"

	@Pyro4.expose
	def EditProduct(self, productId, commandEditProduct, newCharacteristic):
		returnReplyEditProduct = ""
		if self.LoadDataOrNo == False:
			self.LoadData()
		if self.SearchProduct(productId, False) == "":
			product_copy = self.mProducts[productId]

			sql = "UPDATE Products SET "
			if commandEditProduct == 1:
				product_copy.name = newCharacteristic
				sql = sql + "nameProduct = '" + newCharacteristic + "'"
			elif commandEditProduct == 2:
				product_copy.price = newCharacteristic
				sql = sql + "priceProduct = " + str(newCharacteristic)
			elif commandEditProduct == 3:
				product_copy.amount = newCharacteristic
				sql = sql + "amountProduct = " + str(newCharacteristic)
			else :
				return
			sql = sql + " WHERE idProduct = " + str(productId)
			self.mProducts[productId] = product_copy
			try:
				self.cursor.execute(sql)
				self.db.commit()
				returnReplyEditProduct = returnReplyEditProduct + "G|Продукт id = " + str(productId) +" успішно відредагований!"
				return returnReplyEditProduct
			except:
				self.db.rollback()
				return "R|ПОМИЛКА! Продукт id = " + productId + " не відредагований!"

	@Pyro4.expose
	def DeleteCategory(self, сategoryId):
		returnReplyDeleteCategory = ""

		if self.SearchCategory(сategoryId, False) == "":
			productsIdSet = set()
			delname = self.mProductCategories[сategoryId].name
			for productId in self.mProducts:
				if self.mProducts[productId].idCategory == сategoryId:
					productsIdSet.add(productId)

			for productId in productsIdSet:
				self.DeleteProduct(self.mProducts[productId].id)
			del self.mProductCategories[сategoryId]

			sql = "DELETE FROM ProductCategories WHERE idCategory = %d" % сategoryId
			try:
				self.cursor.execute(sql)
				self.db.commit()
				returnReplyDeleteCategory = "G|Категорія " + delname +" успішно видалена!" + "\n"
				return returnReplyDeleteCategory
			except:
				self.db.rollback()
				return "R|ПОМИЛКА при видаленні категорії " + delname
		returnReplyDeleteCategory = returnReplyDeleteCategory + self.SearchCategory(сategoryId, False)
		return returnReplyDeleteCategory

	@Pyro4.expose
	def DeleteProduct(self, productId):
		returnReplyDeleteProduct = ""
		if self.SearchProduct(productId, False) == "":
			delname = self.mProducts[productId].name
			sql = "DELETE FROM Products WHERE idProduct = %d" % productId
			try:
				self.cursor.execute(sql)
				self.db.commit()
				del self.mProducts[productId]
				returnReplyDeleteProduct = returnReplyDeleteProduct + "G|Продукт" + delname + " успішно видалена!" + "\n"
				return returnReplyDeleteProduct
			except:
				self.db.rollback()
				return "ПОМИЛКА при видаленні продукту " + delname
		returnReplyDeleteProduct = returnReplyDeleteProduct + self.SearchProduct(productId, False)
		return returnReplyDeleteProduct

	@Pyro4.expose
	def SearchCategory(self, сategoryId, boolPrintOrNo):
		returnReplySearchCategory = ""
		try:
			sql = "SELECT * FROM ProductCategories WHERE idCategory = %d" % сategoryId
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			if len(results) == 0:
				returnReplySearchCategory = returnReplySearchCategory + "R|Немає категорії з таким id = " + str(сategoryId)
			for row in results:
				idCategory = row[0]
				nameCategory = row[1]
				if boolPrintOrNo:
					returnReplySearchCategory = returnReplySearchCategory + "Y|Category id: " + str(idCategory) + ", name: " + nameCategory  + "\n"
			return returnReplySearchCategory
		except:
			self.db.rollback()
			return "R|ПОМИЛКА при пошуку категорії " + сategoryId

	@Pyro4.expose
	def SearchProduct(self, productId, boolPrintOrNo):
		returnReplySearchProduct = ""
		try:
			sql = "SELECT * FROM Products WHERE idProduct = %d" % productId
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			if len(results) == 0:
				returnReplySearchProduct = returnReplySearchProduct + "R|Немає продукту з таким id = " + str(productId)
			for row in results:
				idProduct = row[0]
				idCategory = row[1]
				nameProduct = row[2]
				priceProduct = row[3]
				amountProduct = row[4]
				if boolPrintOrNo:
					returnReplySearchProduct = returnReplySearchProduct + "Y|Product id: " + str(idProduct) + ", Category id: " + str(idCategory) + ", name: " + nameProduct + \
											   ", price: " + str(priceProduct) + ", amount: " + str(amountProduct)  + "\n"
			return returnReplySearchProduct
		except:
			self.db.rollback()
			return "R|ПОМИЛКА при пошуку продукту " + productId

	@Pyro4.expose
	def PrintListOfCategories(self):
		returnReplyPrintListOfCategories = ""
		sql = "SELECT idCategory, nameCategory FROM ProductCategories"
		self.cursor.execute(sql)
		results = self.cursor.fetchall()
		if len(results) == 0:
			returnReplyPrintListOfCategories = returnReplyPrintListOfCategories + "R|Список порожній"

		returnReplyPrintListOfCategories = "Y|"
		for row in results:
			idCategory = row[0]
			nameCategory = row[1]
			returnReplyPrintListOfCategories = returnReplyPrintListOfCategories + "Category id: " + str(idCategory) + ", name: " + nameCategory + "\n"
		return returnReplyPrintListOfCategories

	@Pyro4.expose
	def PrintListOfProductsInCategory(self, categoryId):
		returnReplyPrintListOfProductsInCategory = ""
		returnReplyPrintListOfProductsInCategory = self.SearchCategory(categoryId, True)
		if returnReplyPrintListOfProductsInCategory[0] != "R":
			sql = "SELECT * FROM Products WHERE idCategory = %d" % categoryId
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
			if len(results) == 0:
				returnReplyPrintListOfProductsInCategory = returnReplyPrintListOfProductsInCategory + "R|Список порожній"
			for row in results:
				idProduct = row[0]
				idCategory = row[1]
				nameProduct = row[2]
				priceProduct = row[3]
				amountProduct = row[4]
				returnReplyPrintListOfProductsInCategory = returnReplyPrintListOfProductsInCategory + "	Product id: " + str(idProduct) + ", Category id: " + str(idCategory) + ", name: " + nameProduct + \
														   ", price: " + str(priceProduct) + ", amount: " + str(amountProduct) + "\n"
		return returnReplyPrintListOfProductsInCategory