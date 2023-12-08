Учебный проект "Мой блог"

<h3>Requirements</h3>

Run <code>pip install -r requirements.txt</code> to install dependencies.


<h3>Installation</h3>

<b>My Blog</b> requires <b>Python 3.9</b> or higher.

<b>Run local</b>
- Clone this repo.
- At the repo's root, enter in the Terminal: <code>python3 -m pip install</code> 
- Make <code>Flask run</code>


<b>Run in Docker</b>
- Clone this repo
- Build docker image with <code>docker build -t flaskapp . </code>
- Run docker with <code>docker run -p 5000:5000 flaskapp </code>