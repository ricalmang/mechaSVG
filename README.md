# mechaSVG
mechaSVG is a python application for creating good-looking energy profile diagrams as *Scalable Vector Graphics* or **'.svg'** files with various aesthetic options. Extra analysis for catalytic cycle diagrams include: Finding energy span, Turn Over Frequency (TOF) estimation from both energy span and *catalytic-flux law*, and estimating degree of TOF control of both intermediates and transition states.¹

## Latest updates
Find energy span of catalytic cycles\
Find the degree of TOF control for intermediates and transition states for catalytic cycles\
Calculate TOF as *catalytic-flux law*

## Preview

The following pictures ilustrate the usage of the graphical user interface and the corresponding output

### Graphical interface

![Interface](/image.png)

### Output graph

![Graph](/teste.svg)

## Running
The program can ben run directly with python 3.5+ without installation.

```bash
py ./mechaSVG.pyw
```
```bash
python3 ./mechaSVG.pyw
```
```bash
pip3 ./mechaSVG.pyw
```
```bash
python ./mechaSVG.pyw
```

## References

¹Kozuch, S. & Shaik, S. *Acc. Chem. Res.* **2011**, *44*, 101. [(Paper)](https://pubs.acs.org/doi/10.1021/ar1000956)