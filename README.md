# Flask User Management API Client

This project is a Flask-based web application that serves as a client for managing user data through a JSON placeholder API.

The application provides a simple interface for performing CRUD (Create, Read, Update, Delete) operations on user data. It interacts with an external API to fetch, create, and delete user records. The main features include displaying a list of users, adding new users, and deleting existing users.

The project is containerized using Docker, making it easy to set up and run in various environments. It uses Flask as the web framework and the Requests library for making HTTP requests to the API. The application is designed to be configurable, with the API URL settable through an environment variable, allowing for flexibility in connecting to different backend services.

## Repository Structure

- `app.py`: The main Flask application file containing the route definitions and API interaction logic.
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Docker Compose configuration for easy deployment and management of the application container.
- `requirements.txt`: Lists the Python dependencies required by the application.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main template for rendering the user list and form.

## Usage Instructions

### Installation

Prerequisites:
- Docker and Docker Compose installed on your system
- Python 3.12 (if running outside Docker)

To run the application using Docker:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build and start the Docker container:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8081`.

To run the application without Docker:

1. Ensure you have Python 3.12 installed.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

The application will be accessible at `http://localhost:8080`.

### Configuration

The application can be configured using the following environment variable:

- `API_URL`: The URL of the JSON placeholder API. Default is 'https://jsonplaceholder.typicode.com'.

To set this in Docker, modify the `docker-compose.yml` file:

```yaml
environment:
  API_URL: http://your-api-url
```

For local development, you can set the environment variable before running the application:

```bash
export API_URL=http://your-api-url
python app.py
```

### Usage

Once the application is running, you can:

1. View the list of users on the home page.
2. Add a new user by filling out the form at the bottom of the page.
3. Delete a user by clicking the "Delete" button next to their name.

### Troubleshooting

Common issues and solutions:

1. Connection refused error:
   - Problem: The application cannot connect to the API.
   - Error message: "ConnectionError: HTTPConnectionPool(host='host.docker.internal', port=8080): Max retries exceeded with url: /users (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x...>: Failed to establish a new connection: [Errno 111] Connection refused'))"
   - Diagnostic process:
     a. Check if the API server is running and accessible.
     b. Verify the `API_URL` environment variable is set correctly.
   - Solution: Ensure the API is running and the URL is correct in the environment settings.

2. Docker container not starting:
   - Problem: The Docker container fails to start.
   - Error message: "Error response from daemon: driver failed programming external connectivity on endpoint..."
   - Diagnostic process:
     a. Check Docker logs: `docker logs <container_id>`
     b. Verify port availability: `netstat -tuln | grep 8081`
   - Solution: Ensure port 8081 is not in use by another application, or modify the port mapping in `docker-compose.yml`.

Debugging:
- To enable debug mode, set the `FLASK_ENV` environment variable to `development`:
  ```bash
  export FLASK_ENV=development
  python app.py
  ```
- Flask debug output will be visible in the console where you run the application.
- Log files: The application doesn't use file logging by default. All logs are output to the console.

Performance optimization:
- Monitor response times for API requests.
- Use tools like Flask-DebugToolbar for profiling if performance issues are encountered.
- Baseline performance: API requests should typically complete within 100-500ms.

## Data Flow

The application follows a simple request-response flow for managing user data:

1. User List Retrieval:
   Client -> Flask App -> External API -> Flask App -> Client

2. User Creation:
   Client -> Flask App -> External API -> Flask App -> Client (Redirect)

3. User Deletion:
   Client -> Flask App -> External API -> Flask App -> Client (Redirect)

```
+--------+    HTTP     +-----------+    HTTP    +-------------+
| Client | <---------> | Flask App | <--------> | External API|
+--------+    Request  +-----------+   Request  +-------------+
              Response              Response
```

The Flask application acts as an intermediary between the client (web browser) and the external API, handling the routing of requests and processing of responses.

## Deployment

Prerequisites:
- Docker and Docker Compose installed on the target system

Deployment steps:
1. Clone the repository on the target system.
2. Navigate to the project directory.
3. Build and start the Docker container:

```bash
docker-compose up -d --build
```

4. The application will be accessible on port 8081 of the host machine.

Environment configurations:
- Ensure the `API_URL` environment variable is set correctly in the `docker-compose.yml` file for the production environment.

Monitoring:
- Use Docker's built-in health checks and logging capabilities to monitor the application's status.
- Implement additional monitoring tools as needed for production use.