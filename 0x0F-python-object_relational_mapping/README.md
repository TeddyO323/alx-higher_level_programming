# 0x0F. Python - Object-relational mapping

<h2>Before you start&hellip;</h2>

<p><strong>Please make sure your MySQL server is in 8.0</strong> -&gt; <a href="https://github.com/TeddyO323/alx-higher_level_programming/tree/main/0x0D-SQL_introduction#install-mysql-80-on-ubuntu-2004-lts" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>

<h2>Background Context</h2>

<p>In this project, you will link two amazing worlds: Databases and Python!</p>

<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>

<p>In the second part, you will use the module <code>SQLAlchemy</code> (don&rsquo;t ask me how to pronounce it&hellip;) an Object Relational Mapper (ORM). </p>

<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &ldquo;What can I do with my objects&rdquo; and not &ldquo;How this object is stored? where? when?&rdquo;. You won&rsquo;t write any SQL queries only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able to change your storage easily without re-writing your entire project.</p>

<p>Without ORM:</p>

<pre><code>conn = MySQLdb.connect(host=&quot;localhost&quot;, port=3306, user=&quot;root&quot;, passwd=&quot;root&quot;, db=&quot;my_db&quot;, charset=&quot;utf8&quot;)
cur = conn.cursor()
cur.execute(&quot;SELECT * FROM states ORDER BY id ASC&quot;) # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>

<p>With an ORM:</p>

<pre><code>engine = create_engine(&#39;mysql+mysqldb://{}:{}@localhost/{}&#39;.format(&quot;root&quot;, &quot;root&quot;, &quot;my_db&quot;), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print(&quot;{}: {}&quot;.format(state.id, state.name))
session.close()
</code></pre>

<p>Do you see the difference? Cool, right? </p>

<p>The biggest difficulty with ORM is: The syntax!</p>

<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&rsquo;t read the entire documentation before starting, just jump on it if you don&rsquo;t get something. </p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://www.fullstackpython.com/object-relational-mappers-orms.html" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
<li><a href="https://mysqlclient.readthedocs.io/" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don&rsquo;t pay attention to <code>_mysql</code></em>)</li>
<li><a href="https://www.mikusa.com/python-mysql-docs/index.html" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
<li><a href="https://docs.sqlalchemy.org/en/13/orm/tutorial.html" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
<li><a href="https://docs.sqlalchemy.org/en/13/" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
<li><a href="https://github.com/PyMySQL/mysqlclient" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
<li><a href="https://www.youtube.com/watch?v=woKYyhLCcnU" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
<li><a href="https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
<li><a href="http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
<li><a href="https://www.pythonsheets.com/notes/python-sqlalchemy.html" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
<li><a href="https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a href="https://overiq.com/sqlalchemy-101/" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>

<h2>More Info</h2>

<h3>Install <code>MySQLdb</code> module version <code>2.0.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed: <a href="/rltoken/paGukker_0KoG3D9FqymNQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, &#39;final&#39;, 0)
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.4.x</code></h3>

<pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
&#39;1.4.22&#39;
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&#39;@@SESSION.GTID_EXECUTED&#39; is deprecated and will be re
moved in a future release.&quot;)                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

  </div>
</div>

---

## TASKS

### 0. Get all states
    
<p>Write a script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, &#39;California&#39;)
(2, &#39;Arizona&#39;)
(3, &#39;Texas&#39;)
(4, &#39;New York&#39;)
(5, &#39;Nevada&#39;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./0-select_states.py)

---

### 1. Filter states
    
<p>Write a script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, &#39;New York&#39;)
(5, &#39;Nevada&#39;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./1-filter_states.py)

---

### 2. Filter states by user input
   
<p>Write a script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (no argument validation needed)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use <code>format</code> to create the SQL query with the user input</li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &#39;Arizona&#39;
(2, &#39;Arizona&#39;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./2-my_filter_states.py)

---

### 3. SQL Injection...
   
<p>Wait, do you remember the previous task? Did you test <code>&quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;</code> as an input?</p>

<pre><code>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &quot;Arizona&#39;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &#39;&quot;
(2, &#39;Arizona&#39;)
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p>What? Empty?</p>

<p>Yes, it&rsquo;s an <a href="/rltoken/qzLjdkHPTue2U1isMj5fJA" title="SQL injection" target="_blank">SQL injection</a> to delete all records of a table&hellip;</p>

<p>Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!</p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name searched</code> (safe from MySQL injection)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa &#39;Arizona&#39;
(2, &#39;Arizona&#39;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./3-my_safe_filter_states.py)

---

### 4. Cities by states

<p>Write a script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, &#39;San Francisco&#39;, &#39;California&#39;)
(2, &#39;San Jose&#39;, &#39;California&#39;)
(3, &#39;Los Angeles&#39;, &#39;California&#39;)
(4, &#39;Fremont&#39;, &#39;California&#39;)
(5, &#39;Livermore&#39;, &#39;California&#39;)
(6, &#39;Page&#39;, &#39;Arizona&#39;)
(7, &#39;Phoenix&#39;, &#39;Arizona&#39;)
(8, &#39;Dallas&#39;, &#39;Texas&#39;)
(9, &#39;Houston&#39;, &#39;Texas&#39;)
(10, &#39;Austin&#39;, &#39;Texas&#39;)
(11, &#39;New York&#39;, &#39;New York&#39;)
(12, &#39;Las Vegas&#39;, &#39;Nevada&#39;)
(13, &#39;Reno&#39;, &#39;Nevada&#39;)
(14, &#39;Henderson&#39;, &#39;Nevada&#39;)
(15, &#39;Carson City&#39;, &#39;Nevada&#39;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./4-cities_by_state.py)

---

### 5. All cities by state
    
<p>Write a script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name</code> (SQL injection free!)</li>
<li>You must use the module <code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>You can use only <code>execute()</code> once</li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$  
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./5-filter_cities.py)

---

### 6. First state model
   
 <p><img src="./f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg" alt="" loading='lazy' style="" /></p>

<p>Write a python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>:</p>

<ul>
<li><code>State</code> class:

<ul>
<li>inherits from <code>Base</code>  <a href="/rltoken/SFKIwNZ3IG6_4TL6dEsIuA" title="Tips" target="_blank">Tips</a></li>
<li>links to the MySQL table <code>states</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string with maximum 128 characters and can&rsquo;t be null</li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li><strong>WARNING:</strong> all classes who inherit from <code>Base</code> <strong>must</strong> be imported before calling <code>Base.metadata.create_all(engine)</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table &#39;hbtn_0e_6_usa.states&#39; doesn&#39;t exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
&quot;&quot;&quot;Start link class to table in database 
&quot;&quot;&quot;
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == &quot;__main__&quot;:
    engine = create_engine(&#39;mysql+mysqldb://{}:{}@localhost/{}&#39;.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./model_state.py)

---

### 7. All states via SQLAlchemy
    
<p>Write a script that lists all <code>State</code> objects from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./7-model_state_fetch_all.py)

---

### 8. First state
    
     
<p>Write a script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>The state you display must be the first in <code>states.id</code></li>
<li>You are not allowed to fetch all states from the database before displaying the result</li>
<li>The results must be displayed as they are in the example below</li>
<li>If the table <code>states</code> is empty, print <code>Nothing</code> followed by a new line</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./8-model_state_fetch_first.py)

---

### 9. Contains `a`
   
<p>Write a script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>states.id</code></li>
<li>The results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./9-model_state_filter_a.py)

---

### 10. Get a state
    
<p>Write a script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 4 arguments: <code>mysql username</code>, <code>mysql password</code>, <code>database name</code> and <code>state name to search</code> (SQL injection free)</li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You can assume you have one record with the state name to search</li>
<li>Results must display the <code>states.id</code></li>
<li>If no state has the name you searched for, display <code>Not found</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./10-model_state_my_get.py)

---

### 11. Add a new state
    
<p>Write a script that adds the <code>State</code> object &ldquo;Louisiana&rdquo; to the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Print the new <code>states.id</code> after creation</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./11-model_state_insert.py)

---

### 12. Update a state
    
<p>Write a script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Change the name of the <code>State</code> where <code>id = 2</code> to <code>New Mexico</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./12-model_state_update_id_2.py)

---

### 13. Delete states
   
<p>Write a script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./13-model_state_delete_a.py)

---

### 14. Cities in state
   
<p>Write a Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.</p>

<ul>
<li><code>City</code> class:

<ul>
<li>inherits from <code>Base</code> (imported from <code>model_state</code>)</li>
<li>links to the MySQL table <code>cities</code></li>
<li>class attribute <code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
<li>class attribute <code>name</code> that represents a column of a string of 128 characters and can&rsquo;t be null</li>
<li>class attribute <code>state_id</code> that represents a column of an integer, can&rsquo;t be null and is a foreign key to <code>states.id</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul>

<p>Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>: </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>You must import <code>State</code> and <code>Base</code> from <code>model_state</code> - <code>from model_state import Base, State</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./14-model_city_fetch_by_state.py)

---

### 15. City relationship
    
<p>Improve the files <code>model_city.py</code> and <code>model_state.py</code>, and save them as <code>relationship_city.py</code> and <code>relationship_state.py</code>:</p>

<ul>
<li><code>City</code> class:

<ul>
<li>No change</li>
</ul></li>
<li><code>State</code> class:

<ul>
<li>In addition to previous requirements, the class attribute <code>cities</code> must represent a relationship with the class <code>City</code>. If the <code>State</code> object is deleted, all linked <code>City</code> objects must be automatically deleted. Also, the reference  from a <code>City</code> object to his <code>State</code> should be named <code>state</code></li>
</ul></li>
<li>You must use the module <code>SQLAlchemy</code></li>
</ul>

<p>Write a script that creates the <code>State</code> &ldquo;California&rdquo; with the <code>City</code> &ldquo;San Francisco&rdquo; from the database <code>hbtn_0e_100_usa</code>: (<code>100-relationship_states_cities.py</code>)</p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql
-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;

guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 5: Table &#39;hbtn_0e_100_usa.states&#39; doesn&#39;t exist
guillaume@ubuntu:~/0x0F$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
id  name
1   California
id  name    state_id
1   San Francisco   1
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./100-relationship_states_cities.py)

---

### 16. List relationship
    
<p>Write a script that lists all <code>State</code> objects, and corresponding <code>City</code> objects, contained in the database <code>hbtn_0e_101_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>The connection to your MySQL server must be to <code>localhost</code> on port <code>3306</code></li>
<li>You must only use one query to the database</li>
<li>You must use the <code>cities</code> relationship for all <code>State</code> objects</li>
<li>Results must be sorted in ascending order by <code>states.id</code> and <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>&lt;state id&gt;: &lt;state name&gt;
&lt;tabulation&gt;&lt;city id&gt;: &lt;city name&gt;
</code></pre>

<pre><code>guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql
-- Create states table in hbtn_0e_101_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
guillaume@ubuntu:~/0x0F$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./101-relationship_states_cities_list.py)

---

### 17. From city

<p>Write a script that lists all <code>City</code> objects from the database <code>hbtn_0e_101_usa</code> </p>

<ul>
<li>Your script should take 3 arguments: <code>mysql username</code>, <code>mysql password</code> and <code>database name</code></li>
<li>You must use the module <code>SQLAlchemy</code></li>
<li>Your script should connect to a MySQL server running on <code>localhost</code> at port <code>3306</code></li>
<li>You must use only one query to the database</li>
<li>You must use the <code>state</code> relationship to access to the <code>State</code> object linked to the <code>City</code> object</li>
<li>Results must be sorted in ascending order by <code>cities.id</code></li>
<li>Results must be displayed as they are in the example below</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>&lt;city id&gt;: &lt;city name&gt; -&gt; &lt;state name&gt;
</code></pre>

<pre><code>guillaume@ubuntu:~/0x0F$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -&gt; California
2: San Jose -&gt; California
3: Los Angeles -&gt; California
4: Fremont -&gt; California
5: Livermore -&gt; California
6: Page -&gt; Arizona
7: Phoenix -&gt; Arizona
8: Dallas -&gt; Texas
9: Houston -&gt; Texas
10: Austin -&gt; Texas
11: New York -&gt; New York
12: Las Vegas -&gt; Nevada
13: Reno -&gt; Nevada
14: Henderson -&gt; Nevada
15: Carson City -&gt; Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[Answer](./102-relationship_cities_states_list.py)

---

<em>THE END</em>