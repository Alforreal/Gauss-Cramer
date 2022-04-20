# Gauss-Krammer

This is an app for solving systems of equations like this:
```
Ax + By = C
Dx + Ey = F
```
**and**
```
Ax + By + Cz = D
Ex + Fy + Gz = H
Ix + Jy + Kz = L
```
*where* A, B, C, D, E, F, G, H, I, J, K and L are rational numbers, meaning they are **not imaginary**

## Installation from source
### Linux
At the moment the only way you can use the app is by cloning the repository. Before doing that you have to install **[Python 3.8](https://www.python.org/downloads/release/python-380/)***(as of writing this, the code supports only python 3.9 or lower([link to the github issue](https://github.com/kivymd/KivyMD/issues/1166#issuecomment-1018337569)), I've used Python 3.8 and everything worked fine. Maybe Python 3.10 will be added later, but only time will tell)*, **[Kivy](https://kivy.org/doc/stable/gettingstarted/installation.html)**, **[Ctypes](https://pypi.org/project/ctypes-callable/)** and **[webbrowser](https://docs.python.org/3/library/webbrowser.html)**. 
You also have to install **[Caviar Dreams font](https://www.dafont.com/caviar-dreams.font)**.
After you have installed everything, clone the github repo:
```
git clone https://github.com/Alforreal/Gauss-Cramer
```
Then, compile C++ libraries:
```
g++ library.cpp -o library.so -shared -fPIC
```
Right after that, you are ready to run the python file:
```
python38 main.py
```
### macOS
The process should be similar, but I'm not sure if running the last command will do the trick. Just run ```main.py``` using Python 3.8 or lower
### Windows
Sorry, try doing the steps above, but I don't know how that is going to work out for you
