import constraint
import matplotlib.pyplot as plt
import networkx as nx

problem=constraint.Problem()
regions=['WA','NT','SA','Q','NSW','V','T']
colors=['Red','Green','Blue']
for region in regions:
    problem.addVariable(region,colors)
neighbors={
    'WA':['NT','SA'],
    'NT':['WA','SA','Q'],
    'SA':['WA','NT','Q','NSW','V'],
    'Q':['NT','SA','NSW'],
    'NSW':['SA','Q','V'],
    'V':['SA','NSW'],
    'T':[]
}

for region,adjacent in neighbors.items():
    for neighbor in adjacent:
        problem.addConstraint(constraint.AllDifferentConstraint(),(region,neighbor))
sol=problem.getSolution()
print(sol)        

grp=nx.Graph(neighbors)
nx.draw(grp,with_labels=True,node_color="white",font_color="black")
plt.show()
