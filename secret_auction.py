programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Retrieving Items from dictionary
#print(programming_dictionary["Bug"])

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A flaw in a program that prevents the program from running as expected."
#print(programming_dictionary)

######################################

#Nesting  dictionary

travel_log = {
  "France": ["Lille", "Dijon", "Paris"]
}
#print(travel_log["France"][1])

#Nesting dictionary in a dictionary

'''travel_log = {
  "France": {"cities_visited": ["Lille", "Dijon", "Paris"]},"total_visits": 12,
  "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits":15}}'''

#Nesting dictionary in a list

travel_log = [
  {"country": "France", "cities_visited": ["Lille", "Dijon", "Paris"], "total_visits": 12},
  {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":15}
]