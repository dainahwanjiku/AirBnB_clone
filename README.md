0x00. AirBnB clone - The console

General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function



🧐 About
This is a Airbnb clone projects that will be build with the aim to learn and apply concepts of high level programming and software engineering in general

🏁 Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python3

Installing
Clone this repository

git clone https://github.com/dainahwanjiku/AirBnB_clone.git
cd AirBnB_clone
./console.py
🔧 Running the tests
This project uses the python unittest model for automated tests

Run all unit tests
python3 -m unittest discover tests

Run a test from a specific file
python3 -m unittest tests/tespytestt_models/test_base_model.py

🎈 Usage
You can run the schell (in an interactive or non-interactive mode) to manipulate your models. You can start it from running the console.py file:

$ ./console.py
The following commands are supported:

create:
Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex:

$ create BaseModel
show:
Prints the string representation of an instance based on the class name and id. Ex:

$ show BaseModel 1234-1234-1234.
destroy:
Deletes an instance based on the class name and id (save the change into the JSON file). Ex:

$ destroy BaseModel 1234-1234-1234.
all:
Prints all string representation of all instances based or not on the class name. Example to show all instances

$ all
Example to show all instances of BaseModel only

$ all BaseModel
update:
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex:

$ update BaseModel 1234-1234-1234
quit:
Quit the shell

⛏️ Built Using
Python - Programming language
