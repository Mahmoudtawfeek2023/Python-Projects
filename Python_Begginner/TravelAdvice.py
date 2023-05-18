import tkinter as tk
from tkinter import ttk

# Destinations and attractions data
destinations = {"Paris, France": ["Eiffel Tower", "Louvre Museum", "Champs-Élysées"], "Shanghai, China": ["The Bund", "Yu Garden", "Shanghai Tower"], "Los Angeles, USA": ["Hollywood Walk of Fame", "Venice Beach", "Universal Studios"], "São Paulo, Brazil": ["São Paulo Museum of Art", "Ibirapuera Park", "Mercado Municipal"], "Cairo, Egypt": ["Pyramids of Giza", "Khan el-Khalili", "Egyptian Museum"]}
interests = ["art", "beaches", "history", "museums", "nightlife", "shopping"]

# Functions
def get_destination_index(destination):
    destination_index = -1
    for i in range(len(destinations)):
        if list(destinations.keys())[i] == destination:
            destination_index = i
            break
    return destination_index

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = destinations[list(destinations.keys())[destination_index]]
    attractions_for_destination.append(attraction)
    return

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = destinations[list(destinations.keys())[destination_index]]
    attractions_with_interest = []
    
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = []
        for word in possible_attraction.split():
            if word.lower() in interests:
                attraction_tags.append(word.lower())
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction)
                
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    
    for i in range(len(traveler_attractions)):
        if i == 0:
            interests_string += traveler_attractions[i]
        else:
            interests_string += ", " + traveler_attractions[i]
    
    return interests_string

def get_recommendations():
    traveler_name = name_var.get()
    traveler_destination = destination_var.get()
    traveler_interests = [interest_var.get()]
    
    traveler_data = [traveler_name, traveler_destination, traveler_interests]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    if len(traveler_attractions) == 0:
        recommendations_label.config(text="Sorry, we don't have any recommendations for that destination and interests.")
    else:
        recommendations = get_attractions_for_traveler(traveler_data)
        recommendations_label.config(text=recommendations)

# GUI
root = tk.Tk()
root.title("Travel Recommendations Program")

# Name entry
name_label = ttk.Label(root, text="Name:")
name_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.grid(column=1, row=0, padx=5, pady=5)

# Destination dropdown
destination_label = ttk.Label(root, text="Destination:")
destination_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
destination_var = tk.StringVar()
destination_dropdown = ttk.Combobox(root, textvariable=destination_var, values=list(destinations.keys()))
destination_dropdown.grid(column=1, row=1, padx=5, pady=5)
destination_dropdown.current(0)

# Interests dropdown
interest_label = ttk.Label(root, text="Interests:")
interest_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
interest_var = tk.StringVar()
interest_dropdown = ttk.Combobox(root, textvariable=interest_var, values=interests)
interest_dropdown.grid(column=1, row=2, padx=5, pady=5)
interest_dropdown.current(0)

# Recommendations button
recommendations_button = ttk.Button(root, text="Get Recommendations", command=get_recommendations)
recommendations_button.grid(column=1, row=3, padx=5, pady=5)

# Recommendations label
recommendations_label = ttk.Label(root, text="")
recommendations_label.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

root.mainloop()