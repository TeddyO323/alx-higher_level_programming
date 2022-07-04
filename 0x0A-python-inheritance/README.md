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

A.) 89


B.) 90


C.) 1


</code></pre>

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

<p>What do these lines print?</p>

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










            
        
    



