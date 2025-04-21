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

