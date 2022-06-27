
## 0x06. Python - Classes and Objects

<div data-react-class="tags/Tags" data-react-props="{Python&quot;OOP&quot;}]}" data-react-cache-id="tags/Tags-0"></div>


<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg" alt="" style="" /></p>

**Background Context**

<p>OOP is a totally new concept for all of you (especially those who think they know about it :)). 
It&rsquo;s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum). </p>

<p>As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. 
The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!</p>

<p>Read or watch the below resources in the order presented.</p>

# Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://python.swaroopch.com/oop.html" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; excluded. You do NOT have to learn about class attributes, <code>classmethod</code> and <code>staticmethod</code> yet</em>)</li>
<li><a href="https://python-course.eu/oop/object-oriented-programming.php" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please *</em>be careful*<em>: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON&rsquo;T have to learn about class attributes), Methods, The <code>__init__</code> Method, &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;Public, Protected, and Private Attributes&rdquo;</em>)</li>
<li><a href="https://python-course.eu/oop/properties-vs-getters-and-setters.php" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> </li>
<li><a href="https://www.youtube.com/watch?v=1AGyBuVCTeE" title="Learn to Program 9 : Object Oriented Programming" target="_blank">Learn to Program 9 : Object Oriented Programming</a> </li>
<li><a href="https://www.youtube.com/watch?v=apACNr7DC_s" title="Python Classes and Objects" target="_blank">Python Classes and Objects</a> </li>
<li><a href="https://www.youtube.com/watch?v=-DP1i2ZU9gk" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> </li>
</ul>

**Learning Objectives**

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
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is the <code>__dict__</code> of a class and/or instance of a class and what does it contain</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the <code>getattr</code> function</li>
</ul>

---

<details>
<summary><strong>Show Quiz/Hide Quiz</strong></summary><br>

# QUIZ


### 1.) In this following code, what is <code>User</code>?

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>

A.) A class


B.) A string


C.) An attribute


D.) A method


E.) An instance

<details>
<code><summary><strong>Show Answer/Hide Answer</strong></summary></code><br>

**A.) A class**

</details>

---

### 2.) In this following code, what is <code>id</code>?

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>

A.) A public instance attribute


B.) A public class attribute


C.) A public class method


D.) A public instance method


E.) A private class attribute


F.) A protected class attribute

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**B.) A public class attribute**

</details>

---

 
### 3.) In this following code, what is <code>__password</code>?

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>

A.) A public class attribute


B.) A public instance attribute


C.) A protected class attribute


D.) A protected instance attribute


E.) A private class attribute


F.) A private instance attribute

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**E.) A private class attribute**

</details>

---

### 4.) In this following code, what is <code>is_new</code>?

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>

A.) A public class attribute


B.) A public instance attribute


C.) A protected class attribute


D.) A protected instance attribute


E.) A private class attribute


F.) A private instance attribute

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**B.) A public instance attribute**

</details>

---

### 5.) What do these lines print?</p>

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;     
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt; 
&gt;&gt;&gt; u = User()
&gt;&gt;&gt; u.is_new
</code></pre>

A.) is_new


B.) Nothing


C.) False


D.) True

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**D.) True**

</details>

---

### 6.) What do these lines print?

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;     
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt; 
&gt;&gt;&gt; u = User()
&gt;&gt;&gt; u.id
</code></pre>

A.) name


B.) None


C.) John


D.) no name

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**C.) John**

</details>

---

### 7.) What do these lines print?

<pre><code>&gt;&gt;&gt; class User:
&gt;&gt;&gt;     id = 89
&gt;&gt;&gt;     name = &quot;no name&quot;
&gt;&gt;&gt;     __password = None
&gt;&gt;&gt;     
&gt;&gt;&gt;     def __init__(self, new_name=None):
&gt;&gt;&gt;         self.is_new = True
&gt;&gt;&gt;         if new_name is not None:
&gt;&gt;&gt;             self.name = new_name
&gt;&gt;&gt; 
&gt;&gt;&gt; u = User(&quot;John&quot;)
&gt;&gt;&gt; u.name
</code></pre>

A.) name


B.) None


C.) John


D.) no name

<details>
<summary><strong><pre><code>Show Answer/Hide Answer</code></pre></strong></summary><br>

**D.) no name**

</details>
</details>


---

# TASKS

# 0. My first square
   
<p>Write an empty class <code>Square</code> that defines a square:</p>
<ul>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__(&#39;0-square&#39;).Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/0x06$ ./0-main.py
&lt;class &#39;0-square.Square&#39;&gt;
{}
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>0-square.py</code></li>
        </ul>
      </div>

# 1. Square with size
   
 <p>Write a class <code>Square</code> that defines a square by: (based on <code>0-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with <code>size</code> (no type/value verification)</li>
<li>You are not allowed to import any module</li>
</ul>

<p><strong>Why?</strong></p>

<p><em>Why <code>size</code> is private attribute?</em></p>

<p>The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.</p>

<pre><code>guillaume@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__(&#39;1-square&#39;).Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./1-main.py
&lt;class &#39;1-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 3}
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>1-square.py</code></li>
        </ul>
      </div>

# 2. Size validation
   
   
 <p>Write a class <code>Square</code> that defines a square by: (based on <code>1-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__(&#39;2-square&#39;).Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square(&quot;3&quot;)
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./2-main.py
&lt;class &#39;2-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 3}
&lt;class &#39;2-square.Square&#39;&gt;
{&#39;_Square__size&#39;: 0}
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
size must be an integer
size must be &gt;= 0
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>2-square.py</code></li>
        </ul>

# 3. Area of a square
   
<p>Write a class <code>Square</code> that defines a square by: (based on <code>2-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code>

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__(&#39;3-square&#39;).Square

my_square_1 = Square(3)
print(&quot;Area: {}&quot;.format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print(&quot;Area: {}&quot;.format(my_square_2.area()))

guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
&#39;Square&#39; object has no attribute &#39;size&#39;
&#39;Square&#39; object has no attribute &#39;__size&#39;
Area: 25
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>3-square.py</code></li>
        </ul>
      </div>

# 4. Access and update private attribute
    

<p>Write a class <code>Square</code> that defines a square by: (based on <code>3-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>You are not allowed to import any module</li>
</ul>

<p><strong>Why?</strong></p>

<p><em>Why a getter and setter?</em></p>

<p>Reminder: <code>size</code> is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.</p>

<pre><code>guillaume@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__(&#39;4-square&#39;).Square

my_square = Square(89)
print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))

my_square.size = 3
print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))

try:
    my_square.size = &quot;5 feet&quot;
    print(&quot;Area: {} for size: {}&quot;.format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 
</code></pre>

 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>4-square.py</code></li>
        </ul>
      </div>

# 5. Printing a square
   
  <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__(&#39;5-square&#39;).Square

my_square = Square(3)
my_square.my_print()

print(&quot;--&quot;)

my_square.size = 10
my_square.my_print()

print(&quot;--&quot;)

my_square.size = 0
my_square.my_print()

print(&quot;--&quot;)

guillaume@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>5-square.py</code></li>
        </ul>

# 6. Coordinates of a square
  
 <p>Write a class <code>Square</code> that defines a square by: (based on <code>5-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:

<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:

<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integers</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space - <strong>Don&rsquo;t fill lines by spaces</strong> when <code>position[1] &gt; 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__(&#39;6-square&#39;).Square

my_square_1 = Square(3)
my_square_1.my_print()

print(&quot;--&quot;)

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print(&quot;--&quot;)

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print(&quot;--&quot;)

guillaume@ubuntu:~/0x06$ ./6-main.py | tr &quot; &quot; &quot;_&quot; | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 
</code></pre>

  </div>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>6-square.py</code></li>
        </ul>
      </div>

# 7. Singly linked list
   

 <p>Write a class <code>Node</code> that defines a node of a singly linked list by: </p>

<ul>
<li>Private instance attribute: <code>data</code>:

<ul>
<li>property <code>def data(self):</code> to retrieve it</li>
<li>property setter <code>def data(self, value):</code> to set it:

<ul>
<li><code>data</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>data must be an integer</code><br></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>next_node</code>:

<ul>
<li>property <code>def next_node(self):</code> to retrieve it</li>
<li>property setter <code>def next_node(self, value):</code> to set it:

<ul>
<li><code>next_node</code> can be <code>None</code> or must be a <code>Node</code>, otherwise raise a <code>TypeError</code> exception with the message <code>next_node must be a Node object</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>data</code> and <code>next_node</code>: <code>def __init__(self, data, next_node=None):</code></li>
</ul>

<p>And, write a class <code>SinglyLinkedList</code> that defines a singly linked list by: </p>

<ul>
<li>Private instance attribute: <code>head</code> (no setter or getter)</li>
<li>Simple instantiation: <code>def __init__(self):</code></li>
<li>Should be printable:

<ul>
<li>print the entire list in stdout</li>
<li>one node number by line</li>
</ul></li>
<li>Public instance method: <code>def sorted_insert(self, value):</code> that inserts a new <code>Node</code> into the correct sorted position in the list (increasing order)</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__(&#39;100-singly_linked_list&#39;).SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/0x06$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/0x06$ 
</code></pre>

  </div>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>100-singly_linked_list.py</code></li>
        </ul>

# 8. Print Square instance
  

 <p>Write a class <code>Square</code> that defines a square by: (based on <code>6-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>position</code>:

<ul>
<li>property <code>def position(self):</code> to retrieve it</li>
<li>property setter <code>def position(self, value):</code> to set it:

<ul>
<li><code>position</code> must be a tuple of 2 positive integers, otherwise raise a <code>TypeError</code> exception with the message <code>position must be a tuple of 2 positive integer</code><br></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>size</code> and optional <code>position</code>: <code>def __init__(self, size=0, position=(0, 0)):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li>Public instance method: <code>def my_print(self):</code> that prints in stdout the square with the character <code>#</code>:

<ul>
<li>if <code>size</code> is equal to 0, print an empty line</li>
<li><code>position</code> should be use by using space</li>
</ul></li>
<li>Printing a <code>Square</code> instance should have the same behavior as <code>my_print()</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 101-main.py
#!/usr/bin/python3
Square = __import__(&#39;101-square&#39;).Square

my_square = Square(5, (0, 0))
print(my_square)

print(&quot;--&quot;)

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/0x06$ ./101-main.py | tr &quot; &quot; &quot;_&quot; | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/0x06$ 
</code></pre>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>101-square.py</code></li>
        </ul>
      </div>

# 9. Compare 2 squares
   
   
 <p>Write a class <code>Square</code> that defines a square by: (based on <code>4-square.py</code>)</p>

<ul>
<li>Private instance attribute: <code>size</code>:

<ul>
<li>property <code>def size(self):</code> to retrieve it</li>
<li>property setter <code>def size(self, value):</code> to set it:

<ul>
<li><code>size</code> must be a number (float or integer), otherwise raise a <code>TypeError</code> exception with the message <code>size must be a number</code><br></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the current square area</li>
<li><code>Square</code> instance can answer to comparators: <code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code> and <code>&lt;=</code> based on the square area</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x06$ cat 102-main.py
#!/usr/bin/python3
Square = __import__(&#39;102-square&#39;).Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 &lt; s_6:
    print(&quot;Square 5 &lt; Square 6&quot;)
if s_5 &lt;= s_6:
    print(&quot;Square 5 &lt;= Square 6&quot;)
if s_5 == s_6:
    print(&quot;Square 5 == Square 6&quot;)
if s_5 != s_6:
    print(&quot;Square 5 != Square 6&quot;)
if s_5 &gt; s_6:
    print(&quot;Square 5 &gt; Square 6&quot;)
if s_5 &gt;= s_6:
    print(&quot;Square 5 &gt;= Square 6&quot;)

guillaume@ubuntu:~/0x06$ ./102-main.py
Square 5 &lt; Square 6
Square 5 &lt;= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/0x06$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>102-square.py</code></li>
        </ul>

# 10. ByteCode -&gt; Python #5
   
 
 <p>Write the Python class <code>MagicClass</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 (&#39;radius must be a number&#39;)
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     &gt;&gt;   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
</code></pre>

<ul>
<li>Tip: <a href="/rltoken/l0hEn4L06ZhFg5HzGPbEhQ" title="Python bytecode" target="_blank">Python bytecode</a></li>
</ul>

  
  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x06-python-classes</code></li>
            <li>File: <code>103-magic_class.py</code></li>
        </ul>
      </div>





