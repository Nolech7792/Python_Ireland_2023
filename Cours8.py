#Dictionnaires

country_capitals = {
    "Italy" : "Rome",
    "France" : "Paris",
    "England" : "London",
    "Japan" : "Tokyo"}

#print(f"The capital of Italy is : {country_capitals['Italy']}")
#print(country_capitals)
country_capitals["Germany"] = "Berlin"
#print(country_capitals)

        #delete#

#del country_capitals["Germany"]
#print(country_capitals)

#country_capitals.clear()##DELETE ALL#

#important method

#country_capitals.get(key, default = none)# #return the value or none# #no error if no value#

#country_capitals.items()# return the items of the dictionnairy (key and values)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10,20,30]

nombres = dict(zip(keys, values))
print(nombres)