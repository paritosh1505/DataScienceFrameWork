## Steps to create a project

1. Create virtual env here virtual env name is myvenv

```
conda create -p myvenv python==3.11 -y

```

2. Crtea a setup.py file

Setup.py file is used for setting up he project as we have added "-e ." in requirements.txt so when we will run command
```
pip install -r requirements.txt
```
it will pick setup.py file also and establish the project