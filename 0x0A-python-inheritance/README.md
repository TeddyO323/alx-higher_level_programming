# 0x0A. Python - Inheritance

## Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/classes.html#inheritance" title="Inheritance" target="_blank">Inheritance</a> </li>
<li><a href="https://docs.python.org/3/tutorial/classes.html#multiple-inheritance" title="Multiple inheritance" target="_blank">Multiple inheritance</a> </li>
<li><a href="https://www.packt.com/inheritance-python/" title="Inheritance in Python" target="_blank">Inheritance in Python</a> </li>
<li><a href="https://www.youtube.com/watch?v=d8kCdLCi6Lk" title="Learn to Program 10 : Inheritance Magic Methods" target="_blank">Learn to Program 10 : Inheritance Magic Methods</a> </li>
</ul>

## Learning Objectives

<ul>
<li>Why Python programming is awesome </li>
<li>What is a superclass, baseclass or parentclass</li>
<li>What is a subclass</li>
<li>How to list all attributes and methods of a class or instance</li>
<li>When can an instance have new attributes</li>
<li>How to inherit class from another</li>
<li>How to define a class with multiple base classes </li>
<li>What is the default class every class inherit from</li>
<li>How to override a method or attribute inherited from the base class</li>
<li>Which attributes or methods are available by heritage to subclasses</li>
<li>What is the purpose of inheritance</li>
<li>What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions</li>
</ul>

---
---

<details>
    <summary><strong>Show Quiz/Hide Quiz</strong></summary><br>

### Quiz questions

<p>1.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)
</code></pre>

A.) None


B.) 0


C.) 1

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
**C.) 1**
    
</details>
    
---

<p>2.) What do these lines print?</p>

<pre><code>class Base():
        &quot;&quot;&quot; My base class &quot;&quot;&quot;
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    for i in range(3):
        b = Base()
    print(b.id)
    </code></pre>

A.) None


B.) 3
    
    
C.) 4
    
    
D.) 2

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
        
** B.) 3**
        
</details>
        
---

<p>3.) What do these lines print?</p>

<pre><code>class Base():
            &quot;&quot;&quot; My base class &quot;&quot;&quot;
        
            __nb_instances = 0
        
            def __init__(self):
                Base.__nb_instances += 1
                self.id = Base.__nb_instances
        
        class User(Base):
            &quot;&quot;&quot; My User class &quot;&quot;&quot;
            pass
        
        u = User()
        print(u.id)
        </code></pre>

    A.) None


    B.) 0
        
        
    C.) 1
        
        
    D.) 2

<details>
<summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
            
**C.) 1**
            
</details>
            
---

<p>4.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;
    pass

for i in range(4):
    u = User()
print(u.id)
</code></pre>


A.) 4


B.) 3


C.) 5


D.) None

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
**A.) 4**
    
</details>
    
---

<p>5.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;
    pass

b = Base()
u = User()
print(u.id)
</code></pre>


A.) 0


B.) 1


C.) 2


D.) 3

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 2**
  
</details>
  
  ---

<p>6.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;

    def __init__(self):
        self.id = 89

u = User()
print(u.id)
</code></pre>


A.) 89


B.) 90


C.) 1

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **A.) 89**
  
  </details>
  
  ---

<p>7.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;

    def __init__(self):
        super().__init__()

u = User()
print(u.id)
</code></pre>


A.) None


B.) 0


C.) 1


D.) 2

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 1**
  
  </details>
  
  ---

<p>8.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)

</code></pre>

A.) 89


B.) 90


C.) 1

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **C.) 1**
  
  </details>
  
  ---

<p>9.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;

    def __init__(self):
        super().__init__()
        self.id = 89

u = User()
print(u.id)
</code></pre>

A.) 89


B.) 90


C.) 1

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **A.) 89**
  
  </details>
  
  ---

<p>10.) What do these lines print?</p>

<pre><code>class Base():
    &quot;&quot;&quot; My base class &quot;&quot;&quot;

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    &quot;&quot;&quot; My User class &quot;&quot;&quot;

    def __init__(self):
        super().__init__()
        self.id += 99

u = User()
print(u.id)
</code></pre>

A.) 99


B.) 100


C.) 1

<details>
  <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
  
  **B.) 100**
  
  </details>
  </details>
  
  
---
---

<details>
<summary><strong>Show Tasks/Hide Tasks</strong></summary><br>


## TASKS

### 0. Lookup
    
<p>Write a function that returns the list of available attributes and methods of an object:</p>

<ul>
<li>Prototype: <code>def lookup(obj):</code></li>
<li>Returns a <code>list</code> object</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__(&#39;0-lookup&#39;).lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;]
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;, &#39;my_attr1&#39;, &#39;my_meth&#39;]
[&#39;__abs__&#39;, &#39;__add__&#39;, &#39;__and__&#39;, &#39;__bool__&#39;, &#39;__ceil__&#39;, &#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dir__&#39;, &#39;__divmod__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__float__&#39;, &#39;__floor__&#39;, &#39;__floordiv__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__getnewargs__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__index__&#39;, &#39;__init__&#39;, &#39;__int__&#39;, &#39;__invert__&#39;, &#39;__le__&#39;, &#39;__lshift__&#39;, &#39;__lt__&#39;, &#39;__mod__&#39;, &#39;__mul__&#39;, &#39;__ne__&#39;, &#39;__neg__&#39;, &#39;__new__&#39;, &#39;__or__&#39;, &#39;__pos__&#39;, &#39;__pow__&#39;, &#39;__radd__&#39;, &#39;__rand__&#39;, &#39;__rdivmod__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__rfloordiv__&#39;, &#39;__rlshift__&#39;, &#39;__rmod__&#39;, &#39;__rmul__&#39;, &#39;__ror__&#39;, &#39;__round__&#39;, &#39;__rpow__&#39;, &#39;__rrshift__&#39;, &#39;__rshift__&#39;, &#39;__rsub__&#39;, &#39;__rtruediv__&#39;, &#39;__rxor__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__sub__&#39;, &#39;__subclasshook__&#39;, &#39;__truediv__&#39;, &#39;__trunc__&#39;, &#39;__xor__&#39;, &#39;bit_length&#39;, &#39;conjugate&#39;, &#39;denominator&#39;, &#39;from_bytes&#39;, &#39;imag&#39;, &#39;numerator&#39;, &#39;real&#39;, &#39;to_bytes&#39;]
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./0-lookup.py)

  ---

### 1. My list
    
<p>Write a class <code>MyList</code> that inherits from <code>list</code>:</p>

<ul>
<li>Public instance method: <code>def print_sorted(self):</code> that prints the list, but sorted (ascending sort)</li>
<li>You can assume that all the elements of the list will be of type <code>int</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__(&#39;1-my_list&#39;).MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

guillaume@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
guillaume@ubuntu:~/0x0A$ 
</code></pre>

  </div>

[(answer)](./1-my_list.py)

  ---  

### 2. Exact same object
    
<p>Write a function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_same_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__(&#39;2-is_same_class&#39;).is_same_class

a = 1
if is_same_class(a, int):
    print(&quot;{} is an instance of the class {}&quot;.format(a, int.__name__))
if is_same_class(a, float):
    print(&quot;{} is an instance of the class {}&quot;.format(a, float.__name__))
if is_same_class(a, object):
    print(&quot;{} is an instance of the class {}&quot;.format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./2-is_same_class.py)

  ---

### 3. Same class or inherit from
    
<p>Write a function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def is_kind_of_class(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__(&#39;3-is_kind_of_class&#39;).is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print(&quot;{} comes from {}&quot;.format(a, int.__name__))
if is_kind_of_class(a, float):
    print(&quot;{} comes from {}&quot;.format(a, float.__name__))
if is_kind_of_class(a, object):
    print(&quot;{} comes from {}&quot;.format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./3-is_kind_of_class.py)

  ---

### 4. Only sub class of
    
<p>Write a function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.</p>

<ul>
<li>Prototype: <code>def inherits_from(obj, a_class):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__(&#39;4-inherits_from&#39;).inherits_from

a = True
if inherits_from(a, int):
    print(&quot;{} inherited from class {}&quot;.format(a, int.__name__))
if inherits_from(a, bool):
    print(&quot;{} inherited from class {}&quot;.format(a, bool.__name__))
if inherits_from(a, object):
    print(&quot;{} inherited from class {}&quot;.format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./4-inherits_from.py)

  ---

### 5. Geometry module

<p>Write an empty class <code>BaseGeometry</code>.</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__(&#39;5-base_geometry&#39;).BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

guillaume@ubuntu:~/0x0A$ ./5-main.py
&lt;5-base_geometry.BaseGeometry object at 0x7f2050c69208&gt;
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;]
[&#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;]
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

[(answer)](./5-base_geometry.py)

  ---


### 6. Improve Geometry
    
<p>Write a class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__(&#39;6-base_geometry&#39;).BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./6-main.py
[Exception] area() is not implemented
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./6-base_geometry.py)

  ---

### 7. Integer validator
    
<p>Write a class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).</p>

<ul>
<li>Public instance method: <code>def area(self):</code> that raises an <code>Exception</code> with the message <code>area() is not implemented</code></li>
<li>Public instance method: <code>def integer_validator(self, name, value):</code> that validates <code>value</code>:

<ul>
<li>you can assume <code>name</code> is always a string</li>
<li>if <code>value</code> is not an integer: raise a <code>TypeError</code> exception, with the message <code>&lt;name&gt; must be an integer</code></li>
<li>if <code>value</code> is less or equal to 0: raise a <code>ValueError</code> exception with the message <code>&lt;name&gt; must be greater than 0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__(&#39;7-base_geometry&#39;).BaseGeometry

bg = BaseGeometry()

bg.integer_validator(&quot;my_int&quot;, 12)
bg.integer_validator(&quot;width&quot;, 89)

try:
    bg.integer_validator(&quot;name&quot;, &quot;John&quot;)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    bg.integer_validator(&quot;age&quot;, 0)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    bg.integer_validator(&quot;distance&quot;, -4)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
guillaume@ubuntu:~/0x0A$ 
</code></pre>

  </div>

  [(answer)](./7-base_geometry.py)

  ---

### 8. Rectangle
    
<p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers, validated by <code>integer_validator</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;8-rectangle&#39;).Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print(&quot;Rectangle: {} - {}&quot;.format(r.width, r.height))
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./8-main.py
&lt;8-rectangle.Rectangle object at 0x7f6f488f7eb8&gt;
[&#39;_Rectangle__height&#39;, &#39;_Rectangle__width&#39;, &#39;__class__&#39;, &#39;__delattr__&#39;, &#39;__dict__&#39;, &#39;__dir__&#39;, &#39;__doc__&#39;, &#39;__eq__&#39;, &#39;__format__&#39;, &#39;__ge__&#39;, &#39;__getattribute__&#39;, &#39;__gt__&#39;, &#39;__hash__&#39;, &#39;__init__&#39;, &#39;__le__&#39;, &#39;__lt__&#39;, &#39;__module__&#39;, &#39;__ne__&#39;, &#39;__new__&#39;, &#39;__reduce__&#39;, &#39;__reduce_ex__&#39;, &#39;__repr__&#39;, &#39;__setattr__&#39;, &#39;__sizeof__&#39;, &#39;__str__&#39;, &#39;__subclasshook__&#39;, &#39;__weakref__&#39;, &#39;area&#39;, &#39;integer_validator&#39;]
[AttributeError] &#39;Rectangle&#39; object has no attribute &#39;width&#39;
[TypeError] height must be an integer
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./8-rectangle.py)

  ---

### 9. Full rectangle
   
<p>Write a class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)</p>

<ul>
<li>Instantiation with <code>width</code> and <code>height</code>: <code>def __init__(self, width, height):</code>:

<ul>
<li><code>width</code> and <code>height</code> must be private. No getter or setter</li>
<li><code>width</code> and <code>height</code> must be positive integers validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the following rectangle description: <code>[Rectangle] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__(&#39;9-rectangle&#39;).Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

guillaume@ubuntu:~/0x0A$ ./9-main.py
[Rectangle] 3/5
15
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

   [(answer)](./9-rectangle.py)

  ---


### 10. Square #1
    
<p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>):</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 10-main.py
#!/usr/bin/python3
Square = __import__(&#39;10-square&#39;).Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./10-main.py
[Rectangle] 13/13
169
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

   [(answer)](./10-square.py)

  ---

### 11. Square #2
  
<p>Write a class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).</p>

<ul>
<li>Instantiation with <code>size</code>: <code>def __init__(self, size):</code>:

<ul>
<li><code>size</code> must be private. No getter or setter</li>
<li><code>size</code> must be a positive integer, validated by <code>integer_validator</code></li>
</ul></li>
<li>the <code>area()</code> method must be implemented</li>
<li><code>print()</code> should print, and <code>str()</code> should return, the square description: <code>[Square] &lt;width&gt;/&lt;height&gt;</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 11-main.py
#!/usr/bin/python3
Square = __import__(&#39;11-square&#39;).Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./11-main.py
[Square] 13/13
169
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

   [(answer)](./11-square.py)

  ---

### 12. My integer
    
<p>Write a class <code>MyInt</code> that inherits from <code>int</code>:</p>

<ul>
<li><code>MyInt</code> is a rebel. <code>MyInt</code> has <code>==</code> and <code>!=</code> operators inverted</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__(&#39;100-my_int&#39;).MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

guillaume@ubuntu:~/0x0A$ ./100-main.py
3
False
True
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

   [(answer)](./100-my_int.py)

  ---

### 13. Can I?
   
<p>Write a function that adds a new attribute to an object if it&rsquo;s possible:</p>

<ul>
<li>Raise a <code>TypeError</code> exception, with the message <code>can&#39;t add new attribute</code> if the object can&rsquo;t have new attribute</li>
<li>You are not allowed to use <code>try/except</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x0A$ cat 101-main.py
#!/usr/bin/python3
add_attribute = __import__(&#39;101-add_attribute&#39;).add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, &quot;name&quot;, &quot;John&quot;)
print(mc.name)

try:
    a = &quot;My String&quot;
    add_attribute(a, &quot;name&quot;, &quot;Bob&quot;)
    print(a.name)
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./101-main.py
John
[TypeError] can&#39;t add new attribute
guillaume@ubuntu:~/0x0A$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

  [(answer)](./101-add_attribute.py)

  ---

  <em>THE END</em>


  </details>








