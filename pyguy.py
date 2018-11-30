#Created by: developermind405@gmail.com

#Pyguy
import datetime
class guy:
	def __init__(self,name,older,gender,eye_color,size,language):
			self.name = name
			self.first_name = ""
			for i in self.name:
				if i != " ":
					self.first_name += i
				else:
					break 
			self.second_name = name.split(self.first_name+" ")[1]
				
			self.older = older
			self.gender = gender
			self.eye_color = eye_color
			self.size = size
			self.language = language
			self.values = {"name" : self.name,"first_name" : self.first_name,"second_name" : self.second_name, "older" : self.older, "gender" : self.gender, "eye_color" : self.eye_color, "size" : self.size,"language" : self.language}

	def get_values(self):	
		return self.values
	

	def get_birthday(self):
		now = int(datetime.datetime.now().year)
		older = self.older
		if not isinstance(older,int):
			try:
				older = int(older)
			except:
				raise TypeError("Older must be int")
		delta = now-older
		return delta
	def add_extra(self,theme,index):
		self.values[theme] = index







