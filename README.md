# **Napalm Project**

## Concepts

The main idea of Napalm is to be a micro framework for constructing APIs and web applications with speed and ease. It's mainly inspired by **flask** and it's in constant development.

## **Todo**

* Add support for HTML templates
* Add built-in ORM for relational databases
* Improve the code structure
* Add more configurations and utilities to build more complex applications.

## How to Use

To test this project by yourself, you need to first clone this repo locally and go to the root folder by command line. After that, you can do this:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd napalm
gunicorn main:app
```
