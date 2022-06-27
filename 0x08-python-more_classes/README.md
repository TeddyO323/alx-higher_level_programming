# 0x08. Python - More Classes and Objects



# Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://python.swaroopch.com/oop.html" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; (excluded)</em>)</li>
<li><a href="https://python-course.eu/oop/object-oriented-programming.php" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: &ldquo;General Introduction,&rdquo; &ldquo;First-class Everything,&rdquo; &ldquo;A Minimal Class in Python,&rdquo; &ldquo;Attributes,&rdquo; &ldquo;Methods,&rdquo; &ldquo;The <code>__init__</code> Method,&rdquo;  &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;<code>__str__</code>- and <code>__repr__</code>-Methods,&rdquo; &ldquo;Public- Protected- and Private Attributes,&rdquo; &amp; &ldquo;Destructor&rdquo;</em>)</li>
<li><a href="https://python-course.eu/oop/class-instance-attributes.php" title="Class and Instance Attributes" target="_blank">Class and Instance Attributes</a> </li>
<li><a href="https://www.youtube.com/watch?v=rq8cL2XMM5M" title="classmethods and staticmethods" target="_blank">classmethods and staticmethods</a> </li>
<li><a href="https://python-course.eu/oop/properties-vs-getters-and-setters.php" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> (<em>Mainly the last part &ldquo;Public instead of Private Attributes&rdquo;</em>)</li>
<li><a href="https://shipit.dev/posts/python-str-vs-repr.html" title="str vs repr" target="_blank">str vs repr</a> </li>
</ul>


# Learning Objectives

<ul>
<li>Why Python programming is awesome </li>
<li>What is OOP</li>
<li>&ldquo;first-class everything&rdquo;</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is <code>self</code></li>
<li>What is a method</li>
<li>What is the special <code>__init__</code> method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them</li>
<li>What is the difference between <code>__str__</code> and <code>__repr__</code></li>
<li>What is a class attribute</li>
<li>What is the difference between a object attribute and a class attribute</li>
<li>What is a class method</li>
<li>What is a static method</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is and what does contain <code>__dict__</code> of a class and of an instance of a class</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>

</ul>

---

<details>
<summary><strong>Show Quiz/Hide Quiz</strong></summary><br>

# QUIZ

  <p>1.) What is <code>__init__</code>? </p>

A.) A class attribute


B.) A class method


C.) The instance method called when a new object is created


D.) The instance method called when a class is called for the first time

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>

**C.) The instance method called when a new object is created**

</details>

---

<p>2.) What is <code>__str__</code>?</p>

A.) Instance method that returns an “informal” and nicely printable string representation of an instance


B.) Instance method that returns the dictionary representation of an instance


C.) Instance method that prints an “informal” and nicely printable string representation of an instance

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>

**A.) Instance method that returns an “informal” and nicely printable string representation of an instance**

</details>

---

<p>3.) What is <code>__repr__</code>?</p>

A.) Instance method that prints an “official” string representation of an instance


B.) Instance method that returns an “official” string representation of an instance


C.) Instance method that returns the dictionary representation of an instance

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>

**B.) Instance method that returns an “official” string representation of an instance**

</details>

---

<p>4.) What is <code>__del__</code>?</p>

A.) Instance method that removes the last character of an instance


B.) Instance method that prints the memory address of an instance


C.) Instance method called when an instance is deleted

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>

**C.) Instance method called when an instance is deleted**

</details>

---

<p>5.) What is <code>__doc__</code>?</p>


A.) The string documentation of an object (based on docstring)


B.) Prints the documentation of an object


C.) Creates man file

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>

**A.) The string documentation of an object (based on docstring)**


</details>

---

6.) What do these lines print?

<pre><code>class User:
  id = 1

print(User.id)</code></pre> 

A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **B.) 1**
  
  </details>
  
  ---

**7.) What do these lines print**

<Pre><code>class User:
  id = 1

u = User()
print(u.id)
</code></Pre> 


A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **B.) 1**
  
  </details>
  
  ---

**8.) What do these lines print?**

<pre><code>class User:
  id = 1

u = User()
u.id = 89
print(u.id)</code></pre>



A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 89
  **
  
  </details>
  
  ---


**9.) What do these lines print?**

<pre><code>class User:
  id = 1

User.id = 98
u = User()
print(u.id)
</code></pre>



A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **D.) 98**
  
  </details>
  
  ---

**10.) What do these lines print?**
<pre><code>class User:
  id = 1

u = User()
User.id = 98
print(u.id)
</code></pre>

A.) None


B.) 1


C.) 89


D.) 98
<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **D.) 98**
  
  </details>
  
  ---


**11.) What do these lines print?**
<pre><code>
  class User:
      id = 1
  
  User.id = 98
  u = User()
  u.id = 89
  print(u.id)
</code></pre>


A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 89**
  
  </details>
  
  ---

**12.) What do these lines print?**
<pre><code>class User:
  id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)
</code></pre>



A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **D.) 98**
  
  </details>
  
  ---

**13.) What do these lines print?**
<pre><code>class User:
  id = 1

u = User()
u.id = 89
User.id = 98
print(User.id)
</code></pre>


A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **D.) 98**
  
  </details>
  
  ---

**14.) What do these lines print?**
<pre><code>class User:
  id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)</code></pre>



A.) None


B.) 1


C.) 89


D.) 98

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 89**
  
  </details>
  
  ---

</details>

---
<details>
<summary><strong>Show Tasks/Hide Tasks</strong></summary><br>

# TASKS

# 0. Simple rectangle 
[(answer)](./0-rectangle.py)
    
<p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;0-rectangle&#39;).Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
&lt;class &#39;0-rectangle.Rectangle&#39;&gt;
{}
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>0-rectangle.py</code></li>
        </ul>
    
 ---

# 1. Real definition of a rectangle
[(answer)](./1-rectangle.py)

    
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;1-rectangle&#39;).Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{&#39;_Rectangle__height&#39;: 4, &#39;_Rectangle__width&#39;: 2}
{&#39;_Rectangle__height&#39;: 3, &#39;_Rectangle__width&#39;: 10}
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>1-rectangle.py</code></li>
        </ul>
      </div>

---  

# 2. Area and Perimeter
[(answer)](./2-rectangle.py)

    
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;2-rectangle&#39;).Rectangle

my_rectangle = Rectangle(2, 4)
print(&quot;Area: {} - Perimeter: {}&quot;.format(my_rectangle.area(), my_rectangle.perimeter()))

print(&quot;--&quot;)

my_rectangle.width = 10
my_rectangle.height = 3
print(&quot;Area: {} - Perimeter: {}&quot;.format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>2-rectangle.py</code></li>
        </ul>

---      

  # 3. String representation
  [(answer)](./3-rectangle.py)

    
   
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;3-rectangle&#39;).Rectangle

my_rectangle = Rectangle(2, 4)
print(&quot;Area: {} - Perimeter: {}&quot;.format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print(&quot;--&quot;)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
--
##########
##########
##########
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>Object address can be different</strong></p>

<p><strong>No test cases needed</strong></p>

  </div>

 
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>3-rectangle.py</code></li>
        </ul>
      </div>

---

# 4. Eval is magic
[(answer)](./4-rectangle.py)

   
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;4-rectangle&#39;).Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print(&quot;--&quot;)
print(my_rectangle)
print(&quot;--&quot;)
print(repr(my_rectangle))
print(&quot;--&quot;)
print(hex(id(my_rectangle)))
print(&quot;--&quot;)

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print(&quot;--&quot;)
print(new_rectangle)
print(&quot;--&quot;)
print(repr(new_rectangle))
print(&quot;--&quot;)
print(hex(id(new_rectangle)))
print(&quot;--&quot;)

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>4-rectangle.py</code></li>
        </ul>
      </div>

---

  # 5. Detect instance deletion

  [(answer)](./5-rectangle.py)

    
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;5-rectangle&#39;).Rectangle

my_rectangle = Rectangle(2, 4)
print(&quot;Area: {} - Perimeter: {}&quot;.format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name &#39;my_rectangle&#39; is not defined
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

 
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>5-rectangle.py</code></li>
        </ul>

--- 

  # 6. How many instances
  [(answer)](./6-rectangle.py)

   
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;6-rectangle&#39;).Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print(&quot;{:d} instances of Rectangle&quot;.format(Rectangle.number_of_instances))
del my_rectangle_1
print(&quot;{:d} instances of Rectangle&quot;.format(Rectangle.number_of_instances))
del my_rectangle_2
print(&quot;{:d} instances of Rectangle&quot;.format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>6-rectangle.py</code></li>
        </ul>

--- 

  # 7. Change representation
  [(answer)](./7-rectangle.py)

    
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character(s) stored in  <code>print_symbol</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;7-rectangle&#39;).Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print(&quot;--&quot;)
my_rectangle_1.print_symbol = &quot;&amp;&quot;
print(my_rectangle_1)
print(&quot;--&quot;)

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print(&quot;--&quot;)
Rectangle.print_symbol = &quot;C&quot;
print(my_rectangle_2)
print(&quot;--&quot;)

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print(&quot;--&quot;)

my_rectangle_3.print_symbol = [&quot;C&quot;, &quot;is&quot;, &quot;fun!&quot;]
print(my_rectangle_3)

print(&quot;--&quot;)

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
[&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;]
[&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;]
[&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;][&#39;C&#39;, &#39;is&#39;, &#39;fun!&#39;]
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>7-rectangle.py</code></li>
        </ul>
      </div>

--- 

  # 8. Compare rectangles
  [(answer)](./8-rectangle.py)

    
  <p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;8-rectangle&#39;).Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print(&quot;my_rectangle_1 is bigger or equal to my_rectangle_2&quot;)
else:
    print(&quot;my_rectangle_2 is bigger than my_rectangle_1&quot;)


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print(&quot;my_rectangle_1 is bigger or equal to my_rectangle_2&quot;)
else:
    print(&quot;my_rectangle_2 is bigger than my_rectangle_1&quot;)

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>8-rectangle.py</code></li>
        </ul>

--- 

# 9. A square is a rectangle
[(answer)](./9-rectangle.py)

   
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)</p>

<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message <code>Bye rectangle...</code> (<code>...</code> being 3 dots not ellipsis) when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;9-rectangle&#39;).Rectangle

my_square = Rectangle.square(5)
print(&quot;Area: {} - Perimeter: {}&quot;.format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>9-rectangle.py</code></li>
        </ul>

---

# 10. N queens
[(answer)](./101-nqueens.py)

    
  <p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br />
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r" title="Judit Polgár" target="_blank">Judit Polgár</a>, the strongest female chess player of all time</small><br />
<br /></p>

<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>

<ul>
<li>Usage: <code>nqueens N</code>

<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>

<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don&rsquo;t have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>

<p>Read: <a href="https://en.wikipedia.org/wiki/Queen_%28chess%29" title="Queen" target="_blank">Queen</a>, <a href="https://en.wikipedia.org/wiki/Backtracking" title="Backtracking" target="_blank">Backtracking</a></p>

<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>

  </div>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x08-python-more_classes</code></li>
            <li>File: <code>101-nqueens.py</code></li>
        </ul>

  </details>




