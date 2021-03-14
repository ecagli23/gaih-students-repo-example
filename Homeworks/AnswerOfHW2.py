#Answer of homework2
CV1 = {
  "name": "Tom",
	"age": 30,
	"expertise": "data analytics"
}
CV2 = {
  "name": "Maria",
	"age": 35,
	"expertise": "artificial intelligence"
}
CV3 = {
  "name": "Cem",
	"age": 25,
	"expertise": "frontend developer"
}

CV4 = {
  "name": "Zeynep",
	"age": 37,
	"expertise": "backend developer"
}

CV5 = {
  "name": "Ali",
	"age": 23,
	"expertise": "database admin"
}

list_CVs = [CV1, CV2, CV3, CV4, CV5]
print(list_CVs[1])
print(list_CVs[2])
for i in range(len(list_CVs)):
  print("CV of : %s" %  list_CVs[i].get('name'), "his/her age is %s" % CV1.get('age'), "his/her expertise is %s" % CV1.get('expertise'))