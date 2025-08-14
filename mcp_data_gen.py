import os 
from dotenv import load_dotenv
from utilis import get_mysql_connection
from mcp.server.fastmcp import FastMCP
from typing import Literal

mcp= FastMCP("data-generator")

@mcp.resource(name="get_products", uri="products://lastest")
def get_products():
    """Fetches the latest products from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        lastest_products= "SELECT * FROM products ORDER BY product_id DESC LIMIT 3;"
        cursor.execute(lastest_products)
        products = cursor.fetchall()
        product = products[0]
        message = f"{product[1], product[2]}"
        return message
    
    except Exception as e:
        return "failed to fetch producrs"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"

@mcp.resource(name="get_selected_product", uri="products://selected/{name}")
def get_selected_product(name: str):
    """Fetches a specific product by name from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        selected_product_query = "SELECT * FROM products WHERE name = %s;"
        cursor.execute(selected_product_query, (name,))
        products = cursor.fetchall()
        
        if products:
            product = products[0]
            message = f"{product[1], product[2]}"
            return message
        else:
            return "Product not found."
    
    except Exception as e:
        return "failed to fetch product."
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"

@mcp.resource(name="get_users", uri="users://lastest")
def get_users():
    """Fetches the latest users from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        lastest_users= "SELECT * FROM `users` ORDER BY user_id DESC LIMIT 1;"
        cursor.execute(lastest_users)
        users = cursor.fetchall()
        user = users[0]
        message= f"{user[1]}"
        return message
    
    except Exception as e:
        return "failed to fetch users"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"

@mcp.resource(name="get_selected_user", uri="users://selected/{username}")
def get_selected_user(username: str):
    """Fetches a specific user by username from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        selected_users_query = "SELECT * FROM users WHERE username= %s;"
        cursor.execute(selected_users_query, (username,))
        users = cursor.fetchall()
        
        if users:
            user = users[0]
            message = f"{user[1], user[3]}"
            return message
        else:
            return "user not found."
    
    except Exception as e:
        return "failed to fetch users."
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"


@mcp.resource(name="get_categories", uri="categories://lastest")
def get_categories():
    """Fetches the latest categories from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        lastest_categories= "SELECT * FROM `categories` ORDER BY category_id DESC LIMIT 3;"
        cursor.execute(lastest_categories)
        categories = cursor.fetchall()
        message = ""
        for category in categories:
            #categorie = categories[0]
            message= f"{categories[1], categories[2]}"
        return message
    
    except Exception as e:
        return "failed to fetch categories"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"

@mcp.resource(name="get_selected_categorie", uri="categories://selected/{name}")
def get_selected_categorie(name: str):
    """Fetches a specific categorie by name from the database."""
    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        selected_categories_query = "SELECT * FROM categories WHERE name = %s;"
        cursor.execute(selected_categories_query, (name,))
        categories = cursor.fetchall()
        
        if categories:
            categorie = categories[0]
            message = f"{categorie[1], categorie[2]}"
            return message
        else:
            return "categorie not found."
    
    except Exception as e:
        return "failed to fetch categorie."
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "Successfully"


@mcp.tool()
def create_products(
    name: str,
    description: str,
    price: float,
    stock_quantity: int,
    category_id: int,
    image_url: str = "https://icon-library.com/images/no-image-icon/no-image-icon-0.jpg") -> Literal["success", "failed"]:

    """Creates a new product in the database."""

    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        new_product_query = "INSERT INTO products (name, description, price, stock_quantity, category_id, image_url) VALUES (%s, %s, %s, %s, %s, %s);"
        new_product= cursor.execute(new_product_query, (name, description, price, stock_quantity, category_id, image_url))
        connection.commit()
    
    except Exception as e:
        return "failed"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "success"

@mcp.tool()
def delete_products(name: str) -> Literal["success", "failed"]:

    """Deletes a product from the database by name."""

    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        delete_product_query = "DELETE FROM products WHERE name= %s;"
        delete_product= cursor.execute(delete_product_query, (name,))
        connection.commit()
    
    except Exception as e:
        return "failed"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "success"


@mcp.tool()
def create_users(
    username: str,
    password_hash: str,
    email: str,
    first_name: str,
    last_name: str,
    address: str,
    city: str,
    state: str,
    zip_code: str,
    country: str) -> Literal["success", "failed"]:
    
    """Creates a new user in the database."""

    try:
        connection= get_mysql_connection()
        cursor= connection.cursor()
        new_user_query = "INSERT INTO users (username, password_hash, email, first_name, last_name, address, city, state, zip_code, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        new_user= cursor.execute(new_user_query, (
            username, password_hash, email, first_name, last_name,
            address, city, state, zip_code, country
        ))
        connection.commit()
    
    except Exception as e:
        return "failed"
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return "success"








if __name__ == '__main__':
    load_dotenv()
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    mcp.run(mcp.streamable_http_app, host=host, port=port)