# StateMachines

```mermaid
graph TD;
stateDiagram-v2;
0-->1;
1-->2: d;
2-->1: ε;
2-->3: •;
3-->4: d;
2-->4: ε;
4-->3: ε;
```
