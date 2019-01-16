import MySQLdb


def exists(connection, token):
    try:
        cursor = connection.cursor()
        sql = "SELECT EXISTS(SELECT token FROM users WHERE token=%s)"
        cursor.execute(sql, (token,))
        response = cursor.fetchone()[0]
        cursor.close()
        if response == 1:
            return True
        else:
            return False
    except MySQLdb.Error:
        return False


def get_username(connection, token):
    try:
        cursor = connection.cursor()
        sql = "SELECT username FROM users WHERE token = %s"
        cursor.execute(sql, (token,))
        response = cursor.fetchall()[0]
        cursor.close()
        if len(response) == 1:
            return response[0]
        else:
            return False
    except MySQLdb.Error:
        return False