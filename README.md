# mechaSVG
mechaSVG is a python application for creating good-looking energy profile diagrams as *Scalable Vector Graphics* or **'.svg'** files with various aesthetic options. The produced graphics can also be easily edited afterwards via an svg editor like Inkscape. Extra analysis for catalytic cycle diagrams include: Finding energy span, Turn Over Frequency (TOF) estimation from both energy span and *catalytic-flux law*, and estimating degree of TOF control of both intermediates and transition states.¹\
[Watch on Youtube](https://youtu.be/0FfNRQJCJAs)

## Latest updates
Find energy span of catalytic cycles\
Find the degree of TOF control for intermediates and transition states for catalytic cycles\
Calculate TOF as *catalytic-flux law*

## Preview

The following pictures ilustrate the usage of the graphical user interface and the corresponding output

### Graphical interface

![Interface](/image.png)

### Output graphs

#### Example 1
![Graph 1](/example_1.svg)

#### Example 2
![Graph 2](/example_2.svg)

## Running
The program can ben run directly with python 3.5+ without installation.

```bash
py ./mechaSVG.pyw
```
```bash
python3 ./mechaSVG.pyw
```
```bash
python ./mechaSVG.pyw
```
Alternatively, a windons 10 executable can be downloaded on the following link:
[mechaSVG-v002.exe](https://github.com/ricalmang/mechaSVG/releases/download/v0.0.2/mechaSVG-v002.exe)


## References

¹Kozuch, S. & Shaik, S. *Acc. Chem. Res.* **2011**, *44*, 101. [(Paper)](https://pubs.acs.org/doi/10.1021/ar1000956)