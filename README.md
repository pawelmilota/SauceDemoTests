# SauceDemo Practical Task
> This is quasi test framework for [_SauceDemo_](https://www.saucedemo.com/) service - it was created for interview process purposes.

## Table of Contents
* [Technologies used](#technologies-used)
* [Project setup on Windows 10](#project-setup-on-windows-10)
* [Contact](#contact)

## Technologies used
+ Python 3.8 & pytest 7.4
+ Selenium 4.10
+ Make command

## Project setup on Windows 10


### 1. Prerequisites:
+ Install [_Python_](https://www.python.org/) for Windows OS platform
+ Install [_Chocolatey_](https://chocolatey.org/install) package manager for Windows OS platform - it's necessary to install [_make_](https://community.chocolatey.org/packages/make) command

### 2. Install required libraries
In Windows OS cmd, in root directory fo the project, execute:
```bash
make install
```

### 3. Run test(s)
In Windows OS cmd, in root directory fo the project, execute:
```bash
make run_all
```
to run all tests, or
```bash
make run_specific TEST_NAME=<test_name>
```
to run one particular test

### 4. Utility commands.
Please check [`Makefile`](./Makefile)

## Contact
pawel.milota@wp.pl