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

    sql = "Select ProductID, ProductName, ProductPrice, ProductImage from Product" # selecting the first name...
    cursor.execute(sql) # and the executing them

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    product_list = []
    for product in result_set:
        product_list.append({'productid': product[0], 'productname': product[1], 'productprice': product[2], 'productimage': product[3]})
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
        sql = "SELECT UserID, Email, Password FROM User WHERE Email = %s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        if user:
            user_id, stored_email, stored_password = user
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return {"success": True, "message": "Login successful", "email": stored_email, "user_id": user_id}
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

    sql = ("""
            SELECT 
                    e.ExperienceID,
                    e.ExperienceName,
                    e.ExperiencePrice,
                    e.ExperienceImage,
                    e.ExperienceDescription,
                    e.ExperienceDuration,
                    el.ExperienceLevelKey,
                    e.ExperienceMinAge,
                    e.ExperienceGroupSize,
                    GROUP_CONCAT(be.ReviewText SEPARATOR '||'),
                    GROUP_CONCAT(be.Rating SEPARATOR '||')
                FROM Experiences e
                JOIN ExperienceLevel el ON e.ExperienceLevelID = el.ExperienceLevelID
                LEFT JOIN BookingExperience be ON be.ExperienceID = e.ExperienceID AND be.ReviewText IS NOT NULL
                GROUP BY e.ExperienceID
            """)
    cursor.execute(sql) # and the executing them

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    experience_list = []
    for row in result_set:
        reviews = []
        if row[9]:
            texts = row[9].split('||')
            ratings = row[10].split('||') if row[10] else []
            reviews = [{"text": t, "author": "Guest", "rating": r} for t, r in zip(texts, ratings)]

        experience_list.append({
            "experienceid": row[0],
            "experiencename": row[1],
            "experienceprice": row[2],
            "experienceimage": row[3],
            "experiencedescription": row[4],
            "experienceduration": row[5],
            "experiencelevelkey": row[6],
            "experienceminage": row[7],
            "experiencegroupsize": row[8],
            "reviews": reviews
        })
    return experience_list

def get_first_name_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT FirstName FROM User WHERE Email = %s", (email,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0].capitalize() if result else "Traveller"

def get_first_name_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT first_name FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else "Traveller"

def get_product_details(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ProductName, ProductPrice, ProductImage FROM Product WHERE ProductID = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product


def insert_experience_booking(experience_id, booking_date, booking_time, user_id, guests):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO BookingExperience (ExperienceID, BookingDate, BookingTime, UserID, Guests)
        VALUES (%s, %s, %s, %s, %s)
    """, (experience_id, booking_date, booking_time, user_id, guests))
    conn.commit()
    cursor.close()
    conn.close()

def delete_latest_booking(experience_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM BookingExperience
        WHERE ExperienceID = %s
        ORDER BY BookingID DESC
        LIMIT 1
    """, (experience_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_remaining_spots(experience_id, booking_date):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT IFNULL(SUM(Guests), 0) 
            FROM BookingExperience 
            WHERE ExperienceID = %s AND BookingDate = %s
        """, (experience_id, booking_date))
    total_booked_guests = cursor.fetchone()[0]

    cursor.execute("""
            SELECT ExperienceGroupSize 
            FROM Experiences 
            WHERE ExperienceID = %s
        """, (experience_id,))
    max_group_size = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    remaining = max_group_size - total_booked_guests
    return max(remaining, 0)



