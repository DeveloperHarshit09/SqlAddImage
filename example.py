import SqlAddImage as im


# First make a connection with your database
checker = im.make_connection(host="localhost", user="root",
                         password="", database='image bank')


# Insert image in this way
im.insert_image(status=checker,img_path="YT-01.png",tablename="image",
                correspond_field="SerialNo",correspond_value="1")

# Retrieve already stored image in this way in the working directory
im.get_image(status=checker,tablename="image",
                correspond_field="SerialNo",correspond_value="8")




