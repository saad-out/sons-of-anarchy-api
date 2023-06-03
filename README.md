# <p align="center">The Sons Of Anarchy TV Show RESTful API</p>

<p align="center">
  <img src="https://github.com/saad-out/sons-of-anarchy-api/blob/main/docs/images/soa_no_bg.png" style="width:1200px;"/>
</p>

# Project Description

Welcome to the Sons of Anarchy API! This project presents a robust and user-friendly RESTful API built on Flask, a powerful Python web framework. It serves as a comprehensive data hub for accessing character, season, and episode information from the iconic TV show Sons of Anarchy. This API offers a seamless way to retrieve data related to the show's characters, seasons, and episodes. Whether you're a fan looking to explore the gritty world of SAMCRO or a developer seeking a reliable data source for Sons of Anarchy, our API offers a straightforward solution. With carefully designed endpoints and well-structured responses, integrating Sons of Anarchy data into your applications, websites, or projects becomes easy.

<p align="center">
  <img src="https://github.com/saad-out/sons-of-anarchy-api/blob/main/docs/images/api_response.png" style="width:1200px;"/>
</p>

# How It Works

**NOTE: For detailed documentation on each API endpoint, please refer to https://saad-out.github.io/sons-of-anarchy-api/.**

The Sons of Anarchy API is currently in `version 1`, with all endpoints prefixed by `api/v1/`. The available endpoints include `characters/`, `seasons/`, and `episodes/`. You can access data for all characters, seasons, or episodes, or specify a specific item by appending its ID to the endpoint.

## Python Example: Fetching Character Data
To retrieve information about a specific character, such as "Jax Teller" with an ID of 1, you can use the `requests` module in Python:
```
import requests

response = requests.get('https://sons-of-anrachy-api.onrender.com/api/v1/characters/1')
character_data = response.json()

print(character_data)
```
The above code fetches the character with ID 1 and receives the following JSON response:
```
{
    "aliases": ["J.T.", "John Teller"],
    "club": "Sons of Anarchy Motorcycle Club, Redwood Original (SAMCRO)",
    "firstName": "Jax",
    "fullName": "Jackson Nathaniel \"Jax\" Teller",
    "gender": "Male",
    "id": 1,
    "image": "https://sons-of-anrachy-api.onrender.com/api/v1/images/jax.jpg",
    "lastName": "Teller",
    "middleName": "Nathaniel",
    "occupation": "Outlaw biker",
    "playedBy": ["Charlie Hunnam"],
    "titles": ["Vice President", "President"]
}
```
## JavaScript Example: Fetching Season Data
To retrieve information about a specific season, such as the 7th season, you can use the `fetch` function in JavaScript:
```
fetch('https://sons-of-anrachy-api.onrender.com/api/v1/seasons/7')
  .then(response => response.json())
  .then(seasonData => console.log(seasonData));
```
The above code fetches season 7 and receives the following JSON response:
```
{
    "endDate": "2014-12-09",
    "episodes": [
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/80",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/81",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/82",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/83",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/84",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/85",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/86",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/87",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/88",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/89",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/90",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/91",
        "https://sons-of-anrachy-api.onrender.com/api/v1/episodes/92"
    ],
    "id": 7,
    "numberOfEpisodes": 13,
    "premierDate": "2014-09-09",
    "seasonOrder": "S07",
    "synopsis": "The final season of Sons of Anarchy brings the epic saga to a gripping conclusion...",
    "viewership": 4.6
}
```
In addition, the API supports pagination using the `offset` and `limit` query parameters. This allows you to control the number of results returned and start the search at a specific offset. By specifying the limit, you can limit the number of items per page, while the offset determines the starting point of the results.

For example, to retrieve episodes with a limit of 2 and starting from offset 10, you can use the following endpoint: `episodes?limit=2&offset=10`.

Here's an example Python code snippet demonstrating the usage of the above endpoint:
```
import requests

response = requests.get('https://sons-of-anrachy-api.onrender.com/api/v1/episodes?limit=2&offset=10')
data = response.json()

print(data)
```
The output of the above code will be:
```
[
  {
    "airDate": "2008-11-12",
    "directedBy": [
      "Stephen Kay"
    ],
    "episodeNumber": 11,
    "id": 11,
    "season": "https://sons-of-anrachy-api.onrender.com/api/v1/seasons/1",
    "seasonNumber": "S01",
    "synopsis": "SAMCRO faces a new challenge when the IRA seeks revenge against the club...",
    "title": "Capybara",
    "writtenBy": [
      "Dave Erickson",
      "Kurt Sutter"
    ]
  },
  {
    "airDate": "2008-11-19",
    "directedBy": [
      "Terrence O'Hara"
    ],
    "episodeNumber": 12,
    "id": 12,
    "season": "https://sons-of-anrachy-api.onrender.com/api/v1/seasons/1",
    "seasonNumber": "S01",
    "synopsis": "As tensions between SAMCRO and the IRA escalate, Jax must make a difficult decision...",
    "title": "The Sleep of Babies",
    "writtenBy": [
      "Kurt Sutter"
    ]
  }
]
```

Please note that the Sons of Anarchy API V1 returns data in JSON format, while character images are provided in PNG format.

Feel free to adjust and modify the examples to fit your project's requirements and utilize the API's functionality effectively.

# Authentication

The Sons of Anarchy Flask API provides both public and restricted routes for accessing and modifying data.

## Public Routes (GET)
All GET routes in the API are freely accessible without requiring any authentication. You can retrieve data by simply sending a GET request to the specified endpoint.

## Restricted Routes (POST, PUT, DELETE)
The API also exposes POST, PUT, and DELETE routes for modifying existing data related to characters, seasons, and episodes. However, these routes have restricted access and can only be accessed by registered admins.

To authenticate and access the restricted routes, you need to include a JWT (JSON Web Token) in the `x-access-tokens` header of your requests. The JWT token is obtained by logging in with your email and password through the login endpoint. Once authenticated, you will receive a token that should be included in subsequent requests to the restricted routes.

Please note that the JWT token has an expiration period, after which you will need to obtain a new token by logging in again. It's important to keep the token confidential and avoid sharing it with unauthorized individuals.

To register new users and provide access to modify data, please contact us via email or Twitter (provided below). We welcome contributions and improvements to the data and can register individuals who demonstrate a genuine interest in enhancing the API.


# Technologies Used

![SQLAlchemy Badge](https://img.shields.io/badge/SQLAlchemy-red?style=flat&logo=python&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

The Sons of Anarchy Flask API utilizes a range of technologies to provide its functionality and ensure a robust and reliable experience for users. The key technologies used in the development of this API are as follows:

- Flask: The API application is built using Flask, a lightweight and flexible Python web framework. Flask provides the foundation for handling HTTP requests, routing, and building RESTful endpoints.

- Flask-SQLAlchemy: Flask-SQLAlchemy is used as the Object-Relational Mapping (ORM) tool to interact with the database. It simplifies database operations by providing an intuitive interface to define database models and perform database queries.

- Flask-Migrate: Flask-Migrate is employed for database migrations. It integrates with Flask-SQLAlchemy to manage changes to the database schema over time. With Flask-Migrate, developers can easily create and apply database migrations, ensuring smooth updates and version control.

- Flask-CORS: To handle Cross-Origin Resource Sharing (CORS) and enable cross-origin requests, Flask-CORS is utilized. It allows the API to respond to requests originating from different domains or origins, ensuring compatibility and accessibility from various client applications.

- PostgreSQL: The API employs PostgreSQL as the underlying database system. PostgreSQL is a powerful and open-source relational database management system that offers scalability, robustness, and extensive features to store and retrieve data efficiently.

- Render: The API is deployed on Render, a cloud platform that simplifies the deployment and scaling of applications. Render provides a seamless deployment experience with automatic SSL certificates, easy scaling, and zero-downtime deployments.

- ElephantSQL: The PostgreSQL database used by the API is hosted on ElephantSQL. ElephantSQL is a fully managed PostgreSQL database service that provides high availability, automated backups, and robust security features.

- Git and GitHub: Git is utilized for version control, allowing for efficient collaboration and tracking of changes. GitHub serves as the remote repository for hosting the project, facilitating code review, issue tracking, and documentation management.

- HTML, CSS, and JavaScript: HTML, CSS, and JavaScript are used for documentation purposes, creating an informative and user-friendly interface to showcase the API endpoints and their functionalities.

- GitHub Pages: The documentation is hosted on GitHub Pages, a static site hosting service provided by GitHub. GitHub Pages allows for easy publishing and accessibility of the API documentation.

- VS Code with Vim extension: The development setup involves using Visual Studio Code (VS Code) as the Integrated Development Environment (IDE) with the Vim extension. This setup provides a powerful coding environment with features like syntax highlighting, code completion, and Vim keybindings.

- Ubuntu: Ubuntu is the chosen operating system for the development environment. It offers a stable and versatile platform for building and testing the API.

These technologies work together to create a reliable, efficient, and secure API for accessing Sons of Anarchy data. Their combination enables seamless integration, efficient data management, and a smooth deployment experience on the Render platform with the ElephantSQL database.

# Installation

**Prerequisites: Ensure that you have [Python](https://www.python.org/downloads/) and [PostgreSQL](https://www.postgresql.org/download/) installed on your machine.**

To run the Sons of Anarchy Flask API locally for testing or other purposes, follow the steps below:

1- Clone the repository:
```
git clone https://github.com/saad-out/sons-of-anarchy-api.git
```
2- Change your directory into the repository:
```
cd sons-of-anarchy-api/
```
3- Create and activate a virtual environment (optional but recommended):
```
python -m venv myenv      # Create a virtual environment  (or python3 -m venv myenv)
source myenv/bin/activate    # Activate the virtual environment (Linux/Mac)
myenv\Scripts\activate       # Activate the virtual environment (Windows)
```
4- Install the required dependencies bt running the following command from the root of the project:
```
pip install -r requirements.txt
```
5- Create a `.env` file at the root of the project and define the following environment variables:
```
SECRET_KEY={your_app_secret_key_here}

APP_HOST={your app host here}                             # Defaults to 0.0.0.0
APP_PORT={your app port here}                             # Defaults to 5000
DEBUG={True or False}                                     # Defaults to False
APP_URL={URL where your app will be available at}         # Defaults to http://localhost:5000

POSTGRES_HOST={your DB host}
POSTGRES_USER={your DB user}
POSTGRES_USER_PASSWORD={your DB user password}
POSTGRES_DB={your DB name}

# Note: Fill in the values for the environment variables according to your setup.
```
6- Navigate to the `src/` folder:
```
cd src/
```
7- Run the application using Gunicorn with the following command:
```
gunicorn --bind 0.0.0.0:5000 api.v1.run:app
```
This command starts the application and binds it to the address `0.0.0.0` on port `5000`.

You can now access the Sons of Anarchy Flask API locally by visiting the specified URL, which is `http://localhost:5000` by default. Make sure that PostgreSQL is running and the database connection details provided in the `.env` file are correct for the application to function properly.

# Documentation
For detailed documentation on the Sons of Anarchy Flask API, please refer to the [official API documentation](https://saad-out.github.io/sons-of-anarchy-api/), hosted on GitHub Pages. It provides comprehensive information on the API endpoints, request parameters, response formats, and examples of API usage.

# Contributing

Contributions to the Sons of Anarchy Flask API project are highly welcomed and appreciated. While there are no predefined guidelines for contributing at the moment, you can still actively participate in improving the project. If you have any ideas, suggestions, or bug reports, please feel free to open an issue on the GitHub repository. Alternatively, you can reach out with your thoughts and contributions through social media channels mentioned below. Your feedback and contributions will help enhance the API and provide a better experience for all users.

# Contact Information:
This project was made possible thanks to the following contributors:

[Saad Out](https://github.com/saad-out)

If you have any questions, suggestions, or feedback regarding the Sons of Anarchy Flask API, please feel free to reach out through the following channels:

Email: outsaad03@gmail.com

Twitter: [@saadout1](https://twitter.com/saadout1)

We value your input and are always ready to assist you. Don't hesitate to get in touch with us for any inquiries or contributions related to the API.

# License:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Sons of Anarchy Flask API is released under the MIT License. This license allows you to use, modify, and distribute the code for both commercial and non-commercial purposes. It grants you the freedom to adapt the API to your specific needs while providing the flexibility to incorporate it into your projects without restrictions.

For more details, please refer to the LICENSE file in the repository.

**Note: The API's data, including characters, seasons, and episodes, belongs to the respective creators and rights holders of the Sons of Anarchy TV show. The API itself is an independent project created for informational and educational purposes.** 
