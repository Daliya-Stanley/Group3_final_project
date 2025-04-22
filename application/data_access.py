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

    sql = "Select ProductID, ProductName, ProductPrice, ProductImage, ProductDescription from Product WHERE ProductStatusID < 3" # selecting the first name...#added where clause so it doesn't show the free products
    cursor.execute(sql) # and the executing them

    result_set = cursor.fetchall() #cursor object, to fetch all that info
    product_list = []
    for product in result_set:
        product_list.append({'productid': product[0], 'productname': product[1], 'productprice': product[2], 'productimage': product[3], 'productdescription':product[4]}) #used to fetch the ...
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
    cursor.execute("SELECT FirstName FROM User WHERE UserId = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else "Traveller"

def get_product_details(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ProductName, ProductPrice, ProductImage, ProductDescription FROM Product WHERE ProductID = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product


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

def get_remaining_spots(experience_id, booking_date, booking_time):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT IFNULL(SUM(Guests), 0) 
            FROM BookingExperience 
            WHERE ExperienceID = %s AND BookingDate = %s AND BookingTime =  %s 
        """, (experience_id, booking_date, booking_time))
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


def process_order_items(order_id, product_cart, experience_cart, destination_cart, default_user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Insert products
        for item in product_cart:
            product_id = item.get('productid')
            user_id = item.get('user_id') or default_user_id
            quantity = item.get('quantity')
            if not all([product_id, user_id, quantity]):
                continue
            cursor.execute("""
                INSERT INTO ProductOrders (ProductID, UserID, Quantity, OrderID)
                VALUES (%s, %s, %s, %s)
            """, (product_id, user_id, quantity, order_id))

        # Insert experiences
        for item in experience_cart:
            experience_id = item.get('experience_id')
            user_id = item.get('user_id') or default_user_id
            booking_date = item.get('booking_date')
            booking_time = item.get('booking_time')
            guests = item.get('guests')
            if not all([experience_id, user_id, booking_date, booking_time, guests]):
                continue
            cursor.execute("""
                INSERT INTO BookingExperience (ExperienceID, BookingDate, BookingTime, UserID, Guests, OrderID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (experience_id, booking_date, booking_time, user_id, guests, order_id))

            # Insert destination
        for item in destination_cart:
            destination_id = item.get('destination_id')
            user_id = item.get('user_id') or default_user_id
            booking_startdate = item.get('booking_startdate')
            booking_enddate = item.get('booking_enddate')
            guests = item.get('guests')
            if not all([destination_id, user_id, booking_startdate, booking_enddate, guests]):
                continue
            cursor.execute("""
                INSERT INTO BookingDestination (DestinationID, BookingStartDate, BookingEndDate, UserID, Guests, OrderID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (destination_id, booking_startdate, booking_enddate, user_id, guests, order_id))

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_order_info(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT OrderDate FROM Orders WHERE OrderID = %s", (order_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_ordered_products(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.ProductName, po.Quantity, p.ProductPrice, p.ProductImage, p.ProductDescription
        FROM ProductOrders po
        JOIN Product p ON p.ProductID = po.ProductID
        WHERE po.OrderID = %s
    """, (order_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            'productname': row[0],
            'quantity': row[1],
            'productprice': row[2],
            'productimage': row[3],
            'productdescription' :row[4]
        } for row in rows
    ]

def get_promotional_products():
    conn = get_db_connection()  # establish connection with DB server and DB called ""

    cursor = conn.cursor()  # call its cursor method, which gives it the abilities to send commands

    sql = "Select ProductID, ProductName, ProductPrice, ProductImage from Product WHERE ProductStatusID = 3" #added where clause so it shows the free products only.
    cursor.execute(sql)  # and the executing them

    result_set = cursor.fetchall()  # cursor object, to fetch all that info
    product_list = []
    for product in result_set:
        product_list.append({'productid': product[0], 'productname': product[1], 'productprice': product[2],
                             'productimage': product[3]})
    # print(product_list)
    return product_list

def get_ordered_experiences(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.ExperienceName, b.BookingDate, b.BookingTime, b.Guests, e.ExperiencePrice, e.ExperienceImage
        FROM BookingExperience b
        JOIN Experiences e ON e.ExperienceID = b.ExperienceID
        WHERE b.OrderID = %s
    """, (order_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            'experiencename': row[0],
            'bookingdate': row[1],
            'bookingtime': row[2],
            'guests': row[3],
            'experienceprice': row[4],
            'experienceimage': row[5]
        } for row in rows
    ]

def get_total_purchased_by_product():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ProductID, SUM(Quantity) 
        FROM ProductOrders 
        GROUP BY ProductID
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return {str(row[0]): row[1] for row in result}

def get_user_orders(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders WHERE UserID = %s ORDER BY OrderDate DESC", (user_id,))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

def get_user_ordered_products(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT P.ProductName, P.ProductImage, P.ProductPrice, OP.Quantity, O.OrderDate
        FROM ProductOrders OP
        JOIN Product P ON OP.ProductID = P.ProductID
        JOIN Orders O ON OP.OrderID = O.OrderID
        WHERE O.UserID = %s
        ORDER BY O.OrderDate DESC
    """, (user_id,))
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def get_user_experiences(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            E.ExperienceName, E.ExperienceImage, E.ExperiencePrice,
            B.Guests, B.BookingDate, B.BookingTime, B.BookingID, B.IsCancelled,
            CS.StatusName AS CancelStatus,
            B.ReviewText, B.Rating
        FROM BookingExperience B
        JOIN Experiences E ON B.ExperienceID = E.ExperienceID
        JOIN Orders O ON B.OrderID = O.OrderID
        LEFT JOIN CancelExperienceRequests CR ON CR.BookingID = B.BookingID AND CR.UserID = %s
        LEFT JOIN CancelStatus CS ON CR.CancelStatusID = CS.CancelStatusID
        WHERE O.UserID = %s
        ORDER BY B.BookingDate DESC
    """, (user_id, user_id))
    return cursor.fetchall()

def get_user_ordered_destinations(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            d.DestinationName, d.DestinationPricePerNight, d.DestinationImage,
            bd.BookingStartDate, bd.BookingEndDate, bd.Guests,
            DATEDIFF(bd.BookingEndDate, bd.BookingStartDate) AS NoOfNights,
            bd.BookingDestinationID,
            cs.StatusName AS CancelStatus,
            bd.ReviewText, bd.Rating
        FROM BookingDestination bd
        JOIN Destination d ON bd.DestinationID = d.DestinationID
        JOIN Orders o ON bd.OrderID = o.OrderID
        LEFT JOIN CancelDestinationRequests cr ON cr.BookingDestinationID = bd.BookingDestinationID
                                               AND cr.UserID = %s
        LEFT JOIN CancelStatus cs ON cr.CancelStatusID = cs.CancelStatusID
        WHERE o.UserID = %s
        ORDER BY bd.BookingStartDate DESC
    """, (user_id, user_id))

    destinations = cursor.fetchall()

    for dest in destinations:
        dest['TotalPrice'] = dest['DestinationPricePerNight'] * dest['Guests'] * dest['NoOfNights']

    cursor.close()
    conn.close()
    return destinations



def get_pending_cancel_count(cursor):
    cursor.execute("""
        SELECT COUNT(*) as total 
        FROM CancelExperienceRequests c
        JOIN CancelStatus cs ON c.CancelStatusID = cs.CancelStatusID
        WHERE cs.StatusName = 'Pending'
    """)
    return cursor.fetchone()['total']

def get_shipped_order_count(cursor):
    cursor.execute("""
        SELECT COUNT(*) as total 
        FROM ProductOrders po
        JOIN OrderStatus os ON po.OrderStatusID = os.OrderStatusID
        WHERE os.StatusName = 'Shipped'
    """)
    return cursor.fetchone()['total']

def get_cancel_requests(cursor):
    cursor.execute("""
        SELECT 
            c.CancelRequestID, 
            c.RequestDate, 
            cs.StatusName AS CancelStatus,
            u.FirstName, u.LastName, u.Email,
            e.ExperienceName, 
            b.BookingDate,
            b.IsCancelled
        FROM CancelExperienceRequests c
        JOIN BookingExperience b ON c.BookingID = b.BookingID
        JOIN User u ON c.UserID = u.UserID
        JOIN Experiences e ON b.ExperienceID = e.ExperienceID
        JOIN CancelStatus cs ON c.CancelStatusID = cs.CancelStatusID
        ORDER BY c.RequestDate DESC
    """)
    return cursor.fetchall()

def get_product_orders(cursor, product_status_filter='All'):
    product_sql = """
        SELECT po.OrderID, po.ProductID, p.ProductName, u.FirstName, u.LastName, u.Email,
               po.Quantity, po.OrderDate, os.StatusName AS Status
        FROM ProductOrders po
        JOIN Product p ON po.ProductID = p.ProductID
        JOIN User u ON po.UserID = u.UserID
        JOIN OrderStatus os ON po.OrderStatusID = os.OrderStatusID
    """
    if product_status_filter != 'All':
        product_sql += " WHERE os.StatusName = %s"
        cursor.execute(product_sql, (product_status_filter,))
    else:
        cursor.execute(product_sql)
    return cursor.fetchall()

def get_experience_orders(cursor):
    cursor.execute("""
            SELECT b.BookingID, e.ExperienceName, u.FirstName, u.LastName, u.Email,
               b.Guests, b.BookingDate, b.BookingTime, o.OrderID,
               b.IsCancelled,
               cs.StatusName AS CancelStatus
        FROM BookingExperience b
        JOIN Experiences e ON b.ExperienceID = e.ExperienceID
        JOIN User u ON b.UserID = u.UserID
        LEFT JOIN Orders o ON b.OrderID = o.OrderID
        LEFT JOIN CancelExperienceRequests cr ON cr.BookingID = b.BookingID
        LEFT JOIN CancelStatus cs ON cr.CancelStatusID = cs.CancelStatusID
        ORDER BY b.BookingDate DESC
    """)
    return cursor.fetchall()

def get_status_id(cursor, table, status_name):
    query = f"SELECT {table}ID FROM {table} WHERE StatusName = %s"
    cursor.execute(query, (status_name,))
    return cursor.fetchone()[0]

def get_ordered_destinations(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.DestinationName, b.BookingStartDate, b.BookingEndDate, b.Guests, e.DestinationPricePerNight, e.DestinationImage
        FROM BookingDestination b
        JOIN Destination e ON e.DestinationID = b.DestinationID
        WHERE b.OrderID = %s
    """, (order_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            'destinationname': row[0],
            'bookingstartdate': row[1],
            'bookingenddate': row[2],
            'guests': row[3],
            'destination_price': row[4],
            'destinationimage': row[5],
            'no_of_nights' : abs((row[2] - row[1]).days)
        } for row in rows
    ]

def get_destination_by_name(destination_name):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
              SELECT *
              FROM destination 
              WHERE destination.DestinationName = %s
          """, (destination_name,))
        rows = cursor.fetchone()
        return rows

    except Exception:
        return {"success": False, "message": f"Error retrieving destination {destination_name}"}
    finally:
        cursor.close()
        conn.close()


def get_destination_by_id(destination_id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
              SELECT *
              FROM destination 
              WHERE destination.DestinationID = %s
          """, (destination_id,))
        rows = cursor.fetchone()
        return rows

    except Exception as e:
        print(e)
        return {"success": False, "message": f"Error retrieving destination with id: {destination_id}"}
    finally:
        cursor.close()
        conn.close()

def request_destination_cancel(cursor, user_id, booking_destination_id):
        # Handle destination cancel request only if destination_booking_id exists
        cursor.execute("""
                        SELECT * FROM CancelDestinationRequests 
                        WHERE BookingDestinationID = %s AND UserID = %s
                    """, (booking_destination_id, user_id))
        existing = cursor.fetchone()

        if not existing:
            cursor.execute("""
                            INSERT INTO CancelDestinationRequests (BookingDestinationID, UserID)
                            VALUES (%s, %s)
                        """, (booking_destination_id, user_id))


def get_destination_cancel_requests(cursor):
    cursor.execute("""
        SELECT 
            d.CancelRequestID, 
            d.RequestDate, 
            cs.StatusName AS CancelStatus,
            u.FirstName, u.LastName, u.Email,
            bd.BookingStartDate,bd.BookingEndDate,
            dest.DestinationName
        FROM CancelDestinationRequests d
        JOIN BookingDestination bd ON d.BookingDestinationID = bd.BookingDestinationID
        JOIN Destination dest ON bd.DestinationID = dest.DestinationID
        JOIN User u ON d.UserID = u.UserID
        JOIN CancelStatus cs ON d.CancelStatusID = cs.CancelStatusID
        ORDER BY d.RequestDate DESC
    """)
    return cursor.fetchall()

def update_user_password(user_id, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("""
            UPDATE User SET Password = %s WHERE UserID = %s
        """, (hashed_password, user_id))
        conn.commit()
        return {"success": True, "message": "Password updated successfully"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    finally:
        cursor.close()
        conn.close()