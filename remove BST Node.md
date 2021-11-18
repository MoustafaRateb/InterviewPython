# Remove Node

## leaf node

- Just delete node

## node has left child only

- connect his child to his parent instead of him

## node has right only

- connect his child to his parent instead of him

## node has both child

- Go to right element and get most left child
- if most left has right child connect it directly to most left child parent
- replace deleted element value by most left child value
