
# geotechapps

Tired of dealing with complex software for your foundation designs? Our web-based geotechnical design tool is here to simplify the process, empowering you to create the perfect foundation for your projects with ease. Whether you're dealing with specific soil conditions, load requirements, or other critical specifications, our intuitive platform guides you through the entire design process. Generate accurate engineering drawings and detailed design reports that comply with industry standards. Build with confidence and bring your vision to life, all from the comfort of your browser.


![Logo](https://github.com/GideonAmhaG/portfolio_project/blob/main/logorot.png)


## Live Demo

Check out the live demo of geotechapps [here](https://geotechapps.phaedrusstudios.com/).


## Features

- **JavaScript-Driven Engineering Drawings:**
  - Utilizes JavaScript to dynamically generate precise engineering drawings based on user inputs, including load conditions and soil properties.
  - Supports interactive visualization, allowing users to adjust parameters and instantly see the impact on the foundation design.

- **Python & Flask Backend:**
  - Powered by Flask, a lightweight and flexible Python web framework, ensuring fast and scalable backend operations.
  - Manages complex calculations for foundation design, utilizing Python's extensive math libraries to process geotechnical data efficiently.

- **SQLite3 Database Integration:**
  - Employs SQLite3 for database management, chosen for its simplicity and ease of integration with Python via the `sqlite3` module.
  - Stores and retrieves user inputs and design results, ensuring data persistence across sessions.

- **Responsive Front-End Design with Bootstrap:**
  - Developed using HTML and Bootstrap to provide a clean, responsive user interface.
  - Ensures compatibility across devices and browsers, allowing users to access the tool from desktops, tablets, and smartphones.

- **Comprehensive Design Reporting:**
  - Generates detailed design reports that include all calculations, assumptions, and methodologies used.
  - Reports are visible in a user-friendly format, providing full transparency and traceability for engineering review and approval.

- **Managed Hosting Deployment:**
  - Hosted on a managed platform, offering robust security, scalability, and uptime without the overhead of server management.
  - Ensures consistent performance and availability, allowing users to access the web tool reliably from any location.


## Installation

1. **Review License:**
   - Before proceeding, please read the License section to understand the terms of use.

2. **Clone the Repository:**
   - Clone this repository to your local machine using Git:
     ```bash
     git clone https://github.com/GideonAmhaG/geotechapps
     ```
   - Navigate into the project directory:
     ```bash
     cd geotechapps
     ```

3. **Set Up the Environment:**
   - Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).
   - Create a virtual environment (optional but recommended):
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```

4. **Install Dependencies:**
   - Install the required Python packages listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Application:**
   - Start the application by running `main.py`:
     ```bash
     python3 main.py
     ```
   - Open your web browser and go to the address provided in the terminal (typically `http://localhost:5000` or similar).

6. **Access the Application:**
   - Use the HTTPS address displayed in your terminal to access the application in your web browser.


## Usage/Examples

Press "Start Designing" -> choose foundation type -> choose soil type -> insert proper inputs (read FAQ page) -> press calculate-regular or calculate-advanced -> view generated engineering drawing -> press "Generate Design Report" to see all calculations, assumptions, and methodologies used. 


## Contributing

This code is proprietary and cannot be used without my permission.


## Related

Here are some related projects

[AirBnB_clone_v4](https://github.com/GideonAmhaG/AirBnB_clone_v4)
[Simple_shell_G](https://github.com/GideonAmhaG/Simple_shell_G)
[printf](https://github.com/GideonAmhaG/printf)
[monty_G](https://github.com/GideonAmhaG/monty_G)


## Authors

Gideon Amha Gebremedhin - [Github](https://github.com/GideonAmhaG) | [X](https://x.com/GideonAmha)


## License

This code is proprietary and cannot be used without my permission.


## Demo

[Demo](https://www.youtube.com/watch?v=Fz7UzISw99Q)


## Lessons Learned

Most difficult technical challenge:

One of the most difficult technical challenges that I faced while creating my web tool that designs building foundations was selecting the right technologies to use. There are many options available for web development, and each one has its own advantages and disadvantages. I wanted to choose the technologies that would best suit my needs and goals, such as simplicity, speed, scalability, reliability, and usability. However, I was confused and overwhelmed by the variety and complexity of the technologies, and I received different opinions and suggestions from different people.

To overcome this challenge, I decided to do some research and analysis on the different technologies that I was considering. I used Python as my programming language, as it is easy to learn, write, and debug, and it has many libraries and frameworks for web development. However, I was not sure which web framework to use for Python, as there are many options, such as Django, Flask, Pyramid, and Web2py. I compared Flask and Django, as they are the most popular and widely used frameworks for Python. I found out that Flask is a lightweight and minimalist framework that gives me full control over the design and features of my web tool, while Django is a full-stack framework that provides a lot of functionality out of the box, but also imposes a lot of structure and conventions that can be restrictive and complicated. After trying out both frameworks, I decided to use Flask because it is simple, fast, and scalable.

For the database system, I also had many options to choose from, such as MySQL, PostgreSQL, MongoDB, and SQLite3. I compared SQLite3 and MySQL, as they are the most common and widely used database systems for web development. I found out that SQLite3 is easy to use and integrate with Python using the sqlite3 module, and it supports multiple features, such as transactions, triggers, views, indexes, foreign keys, etc., while MySQL is a powerful and reliable system that supports many features but also requires me to install and configure it on a server, which can be time-consuming and complex. After trying out both systems, I decided to use SQLite3 because it is simple, fast, and self-contained.

For the front-end development, I used HTML. However, I also needed to use some additional technologies to make my web tool look more attractive, responsive, and interactive. I compared Bootstrap and Foundation, as they are the most popular and widely used front-end frameworks for web development. I found out that Bootstrap provides more components and themes than Foundation, but also has more dependencies and complexity than Foundation. After trying out both frameworks, I decided to use Bootstrap because it provides more functionality and customization options.

For the web hosting solution, I also had many options to choose from, such as shared hosting, dedicated hosting, cloud hosting, etc. I compared dockerized app on a server with Nginx and Gunicorn and managed hosting, as they are the most flexible and scalable solutions for web development. I found out that dockerized app on a server with Nginx and Gunicorn is a solution that involves using Docker, a software platform that allows me to build, run, and deploy my web tool as a containerized application. A container is a standalone unit of software that packages up the code and all its dependencies so that it can run anywhere. Nginx is a web server that can handle high traffic and serve static files efficiently. Gunicorn is a web server gateway interface (WSGI) server that can run Python web applications and communicate with Nginx. This solution gives me more control and customization over my web tool, but also requires me to set up and manage the server, the Docker environment, the nginx configuration, and the Gunicorn workers. Managed hosting is a service that provides web hosting solutions that are fully managed by the provider. This means that the provider takes care of all the technical aspects of running a web server, such as security, performance, backup, maintenance, and updates. Managed hosting saves me the time and hassle of setting up and managing my own server, and it ensures that my web tool is always online, fast, and secure. After trying out both solutions, I decided to use managed hosting because it provides more benefits and guarantees than a dockerized app on a server with Nginx and Gunicorn.

What I've learned:

Creating this web tool was a challenging and rewarding experience for me. I learned a lot from this project, both technically and personally. Here are some of the main takeaways that I want to share:
Technical takeaways: I learned how to use various technologies for web development, such as Python, Flask, HTML, Bootstrap, SQLite3, and managed hosting. I learned how to calculate the optimal foundation design based on the user’s input and the soil properties using Python’s math libraries. I learned how to create a user-friendly and responsive user interface using HTML and Bootstrap. I learned how to store and retrieve the data of my web tool using SQLite3 and Python’s sqlite3 module. I learned how to deploy and host my web tool using managed hosting.
What I might do differently: If I had more time and resources, I might try to improve some aspects of my web tool, such as adding more features, enhancing the user experience, optimizing the performance, and testing the reliability. For example, I might add a better storage feature that allows the user to save their foundation designs on the cloud or on their local device, and access them anytime and anywhere. I might also add more functionality to the user interface, such as allowing the user to edit, save, or share their foundation design. I might also optimize the performance of my web tool by reducing the loading time, improving the accuracy of the calculations, and handling errors gracefully. I might also test the reliability of my web tool by conducting more experiments on different scenarios and locations, and checking for bugs or glitches.
What I learned about myself as a software engineer: I learned that I have a passion for solving real-world problems using software engineering skills. I enjoyed the process of researching, designing, developing, testing, and deploying my web tool that designs building foundations. I also enjoyed learning new technologies and applying them to my project. I learned that I have a growth mindset that allows me to overcome challenges and learn from failures. I also learned that I have good communication and collaboration skills that enable me to work effectively with others and seek feedback.
How this project informs my software engineering path in the future: This project has inspired me to pursue more projects that involve web development, data analysis, civil engineering, and other domains that interest me. I think these fields are very interesting and have a lot of potential for innovation and impact. I want to continue learning new skills and technologies that can help me create more useful and creative web tools that can solve real-world problems. I also want to explore more opportunities for collaboration and networking with other software engineers and domain experts who share similar interests and goals.
Confirm or question any beliefs I held prior to this project: This project has confirmed my belief that software engineering is a powerful and rewarding career that can make a difference in the world. It has also challenged some of my assumptions about web development, such as thinking that SQLite3 is not suitable for web applications or that managed hosting is not secure enough. I realized that these assumptions are not always true and that each technology has its own strengths and weaknesses depending on the context and requirements of the project. Therefore, it is important to do some research and analysis before choosing the technologies to use for a web development project.


## Screenshots

![Web app Screenshot](https://github.com/GideonAmhaG/portfolio_project/blob/main/website_screenshot.png)

