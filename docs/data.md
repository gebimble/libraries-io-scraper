# This is how the Program Should Work

The input that we have is a dependencies/tools `.yaml`:

```yaml
dependencies:
  - python=3.8
  - numpy>1.2

tools:
  - black=1.24
  - ruff
```

This is parsed into a dictionary of type


```mermaid
  classDiagram
      Class01 <|-- AveryLongClass : Cool
      Class03 *-- Class04
      Class05 o-- Class06
      Class07 .. Class08
      Class09 --> C2 : Where am i?
      Class09 --* C3
      Class09 --|> Class07
      Class07 : equals()
      Class07 : Object[] elementData
      Class01 : size()
      Class01 : int chimp
      Class01 : int gorilla
      Class08 <--> C2: Cool label
```
