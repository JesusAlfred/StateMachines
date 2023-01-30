# StateMachines

```mermaid
stateDiagram-v2;
0-->1;
1-down->2: d;
2-up->1: ε;
2-->3: •;
3-down->4: d;
2-->4: ε;
4-up->3: ε;
```
