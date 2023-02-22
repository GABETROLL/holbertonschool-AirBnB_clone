<head>
<h1><center>AirBnB clone project</center></h1>
<img src="https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67">
</head>
<body>
<h3>In this project we will deploy on our own server a copy of the AirBnb website. We will work on creating a console in which we will create a data model. In this data model we will create, update, destroy, etc, objects via the console and we will store and persist objects to a file. When finished we will have a functioning copy with the popular and most useful features of the of the AirBnb website.</h3>
<ul><h2>We will also work on these tasks throughout the project:</h2>
<h3>
<li>Webstatic(HTML/CSS)</li>
<li>MySQL storage</li>
<li>Web framewok</li>
<li>RESTful API</li>
<li>Web dynamic</li>
</h3>
</ul>
<h1><center>Files</center></h1>
<ul><h3>
<li>base_model.py</li>
<li>__init__.py</li>
<li>file_storage.py</li>
<li>console.py</li>
<li>user.py</li>
<li>state.py</li>
<li>city.py</li>
<li>amenity.py</li>
<li>place</li>
<li>review.py</li>
</ul></h3>
<br>
<h1><center>The console</center></h1>
<ul>
<h3>
<li>Creating a data model</li>
<li>Manage the objects (users, place, states, cities, etc)
<li>Storing the objects into a file</li>
</h3>
</ul>
<img src="https://www.spaceotechnologies.com/wp-content/uploads/2020/06/web-application-architecture-1.png">
<br>
<h1><center>Examples</center></h1>
<h2>Interactive mode:</h2>
<h3>
$ ./console.py
<br>
(hbnb) help
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
</h3>
<br>
<h2>Non-interactive mode:</h2>
<h3>
$ echo "help" | ./console.py
<br>
(hbnb)
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
<br>
(hbnb)
<br>
$
<br>
$ cat test_help
<br>
help
<br>
$
<br>
$ cat test_help | ./console.py
<br>
(hbnb)
<br>
Documented commands (type help <topic>):
<br>
========================================
<br>
EOF  help  quit
<br>
(hbnb)
<br>
$
</h3>
<br>
<h2>Installation</h2>
<h3>To use the console you need to have
<ul>
<li>Linux Ubuntu 20.04 LTS or higher</li>
<li>Python 3.8.5 or higher</li>
</h3>
</ul>
<h2>Authors</h2>
<ul>
<h3>
<li>Norman T. Padovani</li>
<li>Gabriel Fernandez</li>
</h3>
</ul>
</body>
