# SqlAddImage

SqlAddImage is a Python Package which helps user to insert and retrieve image in mysql database for particular field by creating image column. 

## Installation

pip install SqlAddImage

## Usage

import SqlAddImage as im


<p>&num; First make a connection with your database</p>

checker = im.make_connection(host="localhost", user="your username",
                         password="your password", database='your database')

<p>&num; Insert image in this way</p>

<span style="color: #4CAF50;">
im.insert_image(status=checker,img_path="your imagefile",tablename="table of database",
                correspond_field="field in table",correspond_value="value of field")
</span>

<br>
<p>&num; Retrieve already stored image in this way in the working directory</p>

<span style="color: darkred;">
im.get_image(status=checker,tablename="table of database",
                correspond_field="field in table",correspond_value="value of field")
</span>





## Contributing

Contribute in this package on GitHub
https://github.com/DeveloperHarshit09/SqlAddImage

## License

MIT License