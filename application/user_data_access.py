import mysql.connector
import sys
import bcrypt

if sys.platform == "win32":
    mysql_password = "password"
else:
    mysql_password = ""

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=mysql_password,
        database="login"
    )

# ---------- USER ACCOUNT MANAGEMENT ----------
def register_person(fname, lname, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT email FROM User WHERE email = %s", (email,))
        if cursor.fetchone():
            return {"success": False, "message": "User already exists"}

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("""
            INSERT INTO User (firstname, lastname, email, password)
            VALUES (%s, %s, %s, %s)
        """, (fname, lname, email, hashed_password))
        conn.commit()
        return {"success": True, "message": "User registered successfully", "email": email}
    except Exception as e:
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()

def authenticate_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT UserID, Email, Password FROM User WHERE Email = %s", (email,))
        user = cursor.fetchone()
        if user:
            user_id, stored_email, stored_password = user
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                return {"success": True, "message": "Login successful", "email": stored_email, "user_id": user_id}
        return {"success": False, "message": "Incorrect email or password"}
    finally:
        cursor.close()
        conn.close()

# ---------- PRODUCT & ORDER MANAGEMENT ----------
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ProductID, ProductName, ProductPrice, ProductImage, ProductDescription
        FROM Product WHERE ProductStatusID < 3
    """)
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            'productid': p[0], 'productname': p[1], 'productprice': p[2],
            'productimage': p[3], 'productdescription': p[4]
        } for p in products
    ]

def get_promotional_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ProductID, ProductName, ProductPrice, ProductImage
        FROM Product WHERE ProductStatusID = 3
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {'productid': r[0], 'productname': r[1], 'productprice': r[2], 'productimage': r[3]}
        for r in results
    ]

def get_product_details(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ProductName, ProductPrice, ProductImage, ProductDescription
        FROM Product WHERE ProductID = %s
    """, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()
    return product

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

def get_total_purchased_by_product():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ProductID, SUM(Quantity) FROM ProductOrders GROUP BY ProductID")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return {str(row[0]): row[1] for row in data}

# ---------- EXPERIENCE MANAGEMENT ----------
def get_experience():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            e.ExperienceID, e.ExperienceName, e.ExperiencePrice, e.ExperienceImage,
            e.ExperienceDescription, e.ExperienceDuration, el.ExperienceLevelKey,
            e.ExperienceMinAge, e.ExperienceGroupSize,
            GROUP_CONCAT(be.ReviewText SEPARATOR '||'),
            GROUP_CONCAT(be.Rating SEPARATOR '||')
        FROM Experiences e
        JOIN ExperienceLevel el ON e.ExperienceLevelID = el.ExperienceLevelID
        LEFT JOIN BookingExperience be ON be.ExperienceID = e.ExperienceID AND be.ReviewText IS NOT NULL
        GROUP BY e.ExperienceID
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    experiences = []
    for row in rows:
        reviews = []
        if row[9]:
            texts = row[9].split('||')
            ratings = row[10].split('||') if row[10] else []
            reviews = [{"text": t, "author": "Guest", "rating": r} for t, r in zip(texts, ratings)]
        experiences.append({
            "experienceid": row[0], "experiencename": row[1], "experienceprice": row[2],
            "experienceimage": row[3], "experiencedescription": row[4],
            "experienceduration": row[5], "experiencelevelkey": row[6],
            "experienceminage": row[7], "experiencegroupsize": row[8],
            "reviews": reviews
        })
    return experiences

def get_user_experiences(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT 
            E.ExperienceName, E.ExperienceImage, E.ExperiencePrice,
            B.Guests, B.BookingDate, B.BookingTime, B.BookingID, B.IsCancelled,
            CS.StatusName AS CancelStatus
        FROM BookingExperience B
        JOIN Experiences E ON B.ExperienceID = E.ExperienceID
        JOIN Orders O ON B.OrderID = O.OrderID
        LEFT JOIN CancelExperienceRequests CR ON CR.BookingID = B.BookingID AND CR.UserID = %s
        LEFT JOIN CancelStatus CS ON CR.CancelStatusID = CS.CancelStatusID
        WHERE O.UserID = %s
        ORDER BY B.BookingDate DESC
    """, (user_id, user_id))
    return cursor.fetchall()

# ---------- UTILS ----------
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

def get_user_orders(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Orders WHERE UserID = %s ORDER BY OrderDate DESC", (user_id,))
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

def process_order_items(order_id, product_cart, experience_cart, default_user_id):
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

        conn.commit()
    except Exception as e:
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