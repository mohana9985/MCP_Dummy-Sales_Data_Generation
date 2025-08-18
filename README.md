# MCP Dummy Sales Data Generation

This project generates dummy sales data and provides a simple API to interact with it. It uses Docker to run a MySQL database, phpMyAdmin for database management, and a Python server for the API.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Interacting with the API](#interacting-with-the-api)
- [Claude Desktop App Integration](#claude-desktop-app-integration)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Project Structure

The project is organized as follows:

```
.
├── .env
├── .gitignore
├── .python-version
├── docker-compose.yml
├── ecommerce_db.sql
├── mcp_data_gen.py
├── pyproject.toml
├── README.md
├── utilis.py
└── uv.lock
```

-   **`.env`**: Environment variables for database connection.
-   **`.gitignore`**: Specifies intentionally untracked files to ignore.
-   **`.python-version`**: Specifies the Python version to be used.
-   **`docker-compose.yml`**: Docker Compose configuration for setting up the MySQL database and phpMyAdmin.
-   **`ecommerce_db.sql`**: SQL script to create the database schema and populate it with sample data.
-   **`mcp_data_gen.py`**: Main entry point of the application. Contains the logic for generating dummy data and the API endpoints.
-   **`pyproject.toml`**: Python project configuration file.
-   **`README.md`**: This file.
-   **`utilis.py`**: Utility functions, including database connection.
-   **`uv.lock`**: A lock file for the `uv` package manager.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mohana9985/MCP_Dummy-Sales_Data_Generation.git
    cd dummy-sales-data
    ```

2.  **Set up the environment:**
    - Create a `.env` file in the root directory and add the following:
      ```
      MYSQL_HOST=localhost
      MYSQL_USER=qtgenai
      MYSQL_PASSWORD=qtgenai
      MYSQL_DATABASE=genaicommerce
      ```

3.  **Start the services using Docker Desktop:**
    - Open Docker Desktop.
    - **Note:** The `docker-compose.yml` uses the `arm64v8/phpmyadmin` image which is specific to Mac ARM64 architecture. If you are on a different architecture (like Windows or a non-ARM Mac), you will need to use the `phpmyadmin/phpmyadmin` image instead.
    - Run the following command in your terminal:
      ```bash
      docker-compose up -d
      ```
    - This will start the Python API server, a MySQL container, and a phpMyAdmin container. You can access phpMyAdmin at `http://localhost:8080`.

## Usage

Once the services are running in Docker, the API server will be available to handle requests.

## Interacting with the API

You can use any API client to interact with the running server. For example, you can use the Claude Desktop App to send requests to the API endpoints listed below.

## Claude Desktop App Integration

After installing the Claude Desktop App, you can configure it to interact with this project's API.

1.  **Open a terminal and run the help command to see available options:**
    ```bash
    mcp --help
    ```
2.  **Install the MCP configuration:**
    ```bash
    mcp install mcp_dummy_gen.py
    ```
    *Note: You will need to replace `<filename>` with the actual configuration file for this project.*

Once configured, you can interact with the API using natural language through the Claude Desktop App.

## API Endpoints

The `mcp_data_gen.py` script exposes the following API endpoints:

-   **GET `/products/latest`**: Fetches the latest products.
-   **GET `/products/selected/{name}`**: Fetches a product by name.
-   **GET `/users/latest`**: Fetches the latest users.
-   **GET `/users/selected/{username}`**: Fetches a user by username.
-   **GET `/categories/latest`**: Fetches the latest categories.
-   **GET `/categories/selected/{name}`**: Fetches a category by name.
-   **POST `/products`**: Creates a new product.
-   **DELETE `/products/{name}`**: Deletes a product by name.
-   **POST `/users`**: Creates a new user.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
