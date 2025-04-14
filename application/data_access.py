import mysql.connector
import sys
import bcrypt

if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="login"
    )
    return mydb

def get_products():
    conn = get_db_connection() # establish connection with DB server and DB called ""

    cursor = conn.cursor()  # call its cursor method, which gives it the abilities to send commands

    sql = "Select ProductName, ProductPrice, ProductImage from Product" # selecting the first name...
    cursor.execute(sql) # and the executing them

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    product_list = []
    for product in result_set:
        product_list.append({'productname': product[0], 'productprice': product[1], 'productimage': product[2]})
    # print(product_list)
    return product_list


def register_person(fname, lname, email, password):
    conn = None
    try:

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the email already exists
        sql_check_email = "SELECT email FROM User WHERE email = %s"
        cursor.execute(sql_check_email, (email,))
        email_result = cursor.fetchone()

        if email_result:
            return {"success": False, "message": "User already exists"}

        # Hash the password and insert new user
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        sql_insert_user = """
                    INSERT INTO User (firstname, lastname, email, password)
                    VALUES (%s, %s, %s, %s)
                """
        val = (fname, lname, email, hashed_password)
        cursor.execute(sql_insert_user, val)
        conn.commit()

        return {"success": True, "message": "User registered successfully", "email" : email}

    except Exception as e:
        return {"success": False, "message": f"Unexpected error: {str(e)}"}

    finally:
        if conn:
            conn.close()

def authenticate_user(email, password):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Look up user by email
        sql = "SELECT email, password FROM User WHERE email = %s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        if user:
            stored_email, stored_password = user
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return {"success": True, "message": "Login successful", "email": stored_email}
            else:
                return {"success": False, "message": "Incorrect password"}
        else:
            return {"success": False, "message": "User not found"}

    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}

    finally:
        if conn:
            conn.close()


def get_experience():
    conn = get_db_connection() # establish connection with DB server and DB called ""

    cursor = conn.cursor()  # call its cursor method, which gives it the abilities to send commands

    sql = "Select ExperienceName, ExperiencePrice, ExperienceImage from Experiences" # selecting the first name...
    cursor.execute(sql) # and the executing them

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    experience_list = []
    for experience in result_set:
        experience_list.append({'experiencename': experience[0], 'experienceprice': experience[1], 'experienceimage': experience[2]})
        print(experience_list)
    return experience_list


