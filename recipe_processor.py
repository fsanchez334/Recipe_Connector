import networkx as nx
import pandas as pd
import sys
import matplotlib.pyplot as plt
from pyvis.network import Network
from collections import defaultdict
def process_recipe(filename):
  f = open(filename, "r")
  updated_recipes  = defaultdict(lambda: [])
  checker = "Ingredients:"
  tracker = []
  for line in f:
    if line == "\n":
      continue 
    updated_line = list(line.rstrip().split(" "));
    if not checker in updated_line:
      tracker.append(updated_line)
    else:
      meal = tracker.pop()
      updated_line.remove("Ingredients:")
      updated_recipes[meal[0]].extend(updated_line)

  return updated_recipes

def make_Graph(recipe_container):
  G = nx.Graph()
  for recipes, ingredients in recipe_container.items():
    G.add_node(recipes, title = ingredients)
  
  grander = Network()
  grander.from_nx(G)
  return grander

def make_edges(G, recipe_container):
  container = []
  for keys in recipe_container.keys():
    container.append(keys)
  for i in range(len(container)):
    for j in range(i + 1, len(container)):
      first = container[i]
      second = container[j]
      ingredients_1 = set(recipe_container[first])
      ingredients_2 = set(recipe_container[second])
      cross = ingredients_1.intersection(ingredients_2)
      if len(cross) > 0:
        G.add_edge(first, second)
  
  return

recipe = print("Hello - We are going to process a recipe")
formatted_recipe = process_recipe("/content/Recipes.txt")
G = make_Graph(formatted_recipe)
make_edges(G, formatted_recipe)

G.show("Recipe_Network.html")
