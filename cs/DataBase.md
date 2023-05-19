Remove repeating groups of data
Remove partial key dependencies
Remove non-key Dependencies

Structured and organised collection of related data
Table(Field1,Field2)
Record: collection of items
- Flat model - consists of a single, two-dimensional array of data elements, where all members of a given column are assumed to be similar values, and all members of a row are assumed to be related to one another.
- Hierarchical model  - data is organised into a tree-like structure, implying a single upward link in each record to describe the nesting, and a sort field to keep the records in a particular order in each same-level list.
- Network model - stores records with links to other records. Associations are tracked via "pointers". These pointers can be node numbers or disk addresses. Most network databases tend to also include some form of hierarchical model.
- Relational model - tables are related to each other through a common attribute/column/field
## Graph schema
explore relationship between connected entities
```
Graph -record→ relationship
Graph -record fact in→ Nodes
Relationship -organised→ Nodes
Relationship -Have→ Properties
Nodes -Have→ Properties
```
Social network
Node 
Edge
Degree of seperation