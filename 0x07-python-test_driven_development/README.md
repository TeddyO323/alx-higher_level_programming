# Python - Test-driven development

🔴  Red
✅  Green
🛠  Refactor

---
- Test-Driven Development (TDD) is a development technique that advocates writing tests before software source code.

---

# Concept

<em>For this project, look at this concept:</em>

<a href="./47.md">Never forget a test</a>

<p><img src="./giphy-4.gif" alt="" style="" /></p>

---

# Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3.4/library/doctest.html" title="doctest — Test interactive Python examples" target="_blank">doctest — Test interactive Python examples</a> (<em>until &ldquo;26.2.3.7. Warnings&rdquo; included</em>)</li>
<li><a href="https://pymotw.com/3/doctest/" title="doctest – Testing through documentation" target="_blank">doctest – Testing through documentation</a> </li>
<li><a href="https://www.youtube.com/watch?v=1Lfv5tUGsn8" title="Unit Tests in Python" target="_blank">Unit Tests in Python</a></li>
</ul>

## Learning Objectives

<ul>
<li>Why Python programming is awesome</li>
<li>What&rsquo;s an interactive test</li>
<li>Why tests are important</li>
<li>How to write Docstrings to create tests</li>
<li>How to write documentation for each module and function</li>
<li>What are the basic option flags to create tests</li>
<li>How to find edge cases</li>
</ul>

---
---

<details>
    <summary><strong>Show Quiz/Hide Quiz</strong></summary><br>

# QUIZ

**1.) Is this a standardized way to comment a function in Python?**
<pre><code>/* Addition function */
    def add(a, b):
        return a + b
    </code></pre>


A.) Yes


B.) No

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **B.) No**
    
    </details>
    
---

**2.) Is this a standardized way to comment a function in Python?**
<pre><code>"""" Addition function """
    def add(a, b):
        return a + b
    </code></pre>

A.) Yes

B.) No

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **B.) No**
    </details>
    
---
    

**3.) Is this a standardized way to comment a function in Python?**
<pre><code>##########
    # Addition function
    ##########
    def add(a, b):
        return a + b
    </code></pre>

A.) Yes


B.) No

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **B.) No**
    
    </details>
    
---
    

**4.) Is this a standardized way to comment a function in Python?**
<pre><code>def add(a, b):
    """ Addition function """
    return a + b
</code></pre>

A.) Yes


B.) No

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **A.) Yes**
    
    </details>

---


**5.) Is this module correctly commented?**
<pre><code#!/usr/bin/python3
    """ 
        My calculation module
    """
    import sys
    ...
    ></code></pre>


A.) Yes


B.) No

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **A.) Yes**
    
    </details>

---

**6.) Is this module correctly commented?**
<pre><code>#!/usr/bin/python3
    import sys
    
    """ 
        My calculation module
    """
    ...
</code></pre>


A.) Yes


B.) No

Tips:
Docstring must be before import statements

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **B.) No**
    
    </details>

---

**7.) Based on this code, what should all the test cases be? (select multiple)**

<pre><code>def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
</code></pre>



A.) empty list


B.) list with one element (any type)


C.) list with 2 different element (same type)


D.) list with twice the same element (same type)


E.) list with more than 2 times the same element (same type)


F.) list with multiple types (integer, string, etc…)


G.) not a list argument (ex: passing a dictionary to the method)

<details>
    <summary><strong><code>Show Answer/Hide Answer</code></strong></summary><br>
    
    **All of them lol**
    
    </details>
    </details>

---
---

<details>
    <summary><strong>Show Tasks/Hide Tasks</strong></summary><br>
    
# TASKS

# 0. Integers addition
    
<p>Write a function that adds 2 integers.</p>

<ul>
<li>Prototype: <code>def add_integer(a, b=98):</code></li>
<li><code>a</code> and <code>b</code> must be integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>a must be an integer</code> or <code>b must be an integer</code></li>
<li><code>a</code> and <code>b</code> must be first casted to integers if they are float</li>
<li>Returns an integer: the addition of <code>a</code> and <code>b</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__(&#39;0-add_integer&#39;).add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, &quot;School&quot;))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).__doc__)&#39; | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c &#39;print(__import__(&quot;0-add_integer&quot;).add_integer.__doc__)&#39; | wc -l
3
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>0-add_integer.py, tests/0-add_integer.txt</code></li>
        </ul>
      </div>

# 1. Divide a matrix
    
<p>Write a function that divides all elements of a matrix.</p>

<ul>
<li>Prototype: <code>def matrix_divided(matrix, div):</code></li>
<li><code>matrix</code> must be a list of lists of integers or floats, otherwise raise a <code>TypeError</code> exception with the message <code>matrix must be a matrix (list of lists) of integers/floats</code></li>
<li>Each row of the <code>matrix</code> must be of the same size, otherwise raise a <code>TypeError</code> exception with the message <code>Each row of the matrix must have the same size</code></li>
<li><code>div</code> must be a number (integer or float), otherwise raise a <code>TypeError</code> exception with the message <code>div must be a number</code></li>
<li><code>div</code> can&rsquo;t be equal to <code>0</code>, otherwise raise a <code>ZeroDivisionError</code> exception with the message <code>division by zero</code></li>
<li>All elements of the matrix should be divided by <code>div</code>, rounded to 2 decimal places </li>
<li>Returns a new matrix</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__(&#39;2-matrix_divided&#39;).matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>2-matrix_divided.py, tests/2-matrix_divided.txt</code></li>
        </ul>

# 2. Say my name
    
<p>Write a function that prints <code>My name is &lt;first name&gt; &lt;last name&gt;</code></p>

<ul>
<li>Prototype: <code>def say_my_name(first_name, last_name=&quot;&quot;):</code></li>
<li><code>first_name</code> and <code>last_name</code> must be strings otherwise, raise a <code>TypeError</code> exception with the message <code>first_name must be a string</code> or <code>last_name must be a string</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__(&#39;3-say_my_name&#39;).say_my_name

say_my_name(&quot;John&quot;, &quot;Smith&quot;)
say_my_name(&quot;Walter&quot;, &quot;White&quot;)
say_my_name(&quot;Bob&quot;)
try:
    say_my_name(12, &quot;White&quot;)
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

<p>Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.</p>

  </div>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>3-say_my_name.py, tests/3-say_my_name.txt</code></li>
        </ul>


# 3. Print square
    
<p>Write a function that prints a square with the character <code>#</code>.</p>

<ul>
<li>Prototype: <code>def print_square(size):</code></li>
<li><code>size</code> is the size length of the square</li>
<li><code>size</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>if <code>size</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>size must be &gt;= 0</code></li>
<li>if <code>size</code> is a float and is less than 0, raise a <code>TypeError</code> exception with the message <code>size must be an integer</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__(&#39;4-print_square&#39;).print_square

print_square(4)
print(&quot;&quot;)
print_square(10)
print(&quot;&quot;)
print_square(0)
print(&quot;&quot;)
print_square(1)
print(&quot;&quot;)
try:
    print_square(-1)
except Exception as e:
    print(e)
print(&quot;&quot;)

guillaume@ubuntu:~/0x07$ ./4-main.py
####
####
####
####

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


#

size must be &gt;= 0

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>4-print_square.py, tests/4-print_square.txt</code></li>
        </ul>
      </div> 
      
# 4. Text indentation
    
<p>Write a function that prints a text with 2 new lines after each of these characters: <code>.</code>, <code>?</code> and <code>:</code></p>

<ul>
<li>Prototype: <code>def text_indentation(text):</code></li>
<li><code>text</code> must be a string, otherwise raise a <code>TypeError</code> exception with the message <code>text must be a string</code></li>
<li>There should be no space at the beginning or at the end of each printed line</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__(&#39;5-text_indentation&#39;).text_indentation

text_indentation(&quot;&quot;&quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres&quot;&quot;&quot;)

guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>5-text_indentation.py, tests/5-text_indentation.txt</code></li>
        </ul>
      </div>

# 5. Max integer - Unittest
    
<p>Since the beginning you have been creating &ldquo;Interactive tests&rdquo;. For this exercise, you will add Unittests.</p>

<p>In this task, you will write unittests for the function <code>def max_integer(list=[]):</code>.</p>

<ul>
<li>Your test file should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="https://docs.python.org/3.4/library/unittest.html#module-unittest" title="unittest module" target="_blank">unittest module</a> </li>
<li>Your test file should be python files (extension: <code>.py</code>)</li>
<li>Your test file should be executed by using this command: <code>python3 -m unittest tests.6-max_integer_test</code> </li>
<li>All tests you make must be passable by the function below</li>
<li>We strongly encourage you to work together on test cases, so that you don&rsquo;t miss any edge case</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 6-max_integer.py
#!/usr/bin/python3
&quot;&quot;&quot;Module to find the max integer in a list
&quot;&quot;&quot;


def max_integer(list=[]):
    &quot;&quot;&quot;Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    &quot;&quot;&quot;
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i &lt; len(list):
        if list[i] &gt; result:
            result = list[i]
        i += 1
    return result

guillaume@ubuntu:~/0x07$ 
guillaume@ubuntu:~/0x07$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ ./6-main.py
4
4
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2&gt;&amp;1 | tail -1
OK
guillaume@ubuntu:~/0x07$
guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
&quot;&quot;&quot;Unittest for max_integer([..])
&quot;&quot;&quot;
import unittest
max_integer = __import__(&#39;6-max_integer&#39;).max_integer

class TestMaxInteger(unittest.TestCase):
guillaume@ubuntu:~/0x07$ 
</code></pre>

  </div>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>tests/6-max_integer_test.py</code></li>
        </ul>

# 6. Matrix multiplication
    
<p>Write a function that multiplies 2 matrices:</p>

<ul>
<li><p>Read: <a href="https://en.wikipedia.org/wiki/Matrix_multiplication" title="Matrix multiplication - only Matrix product (two matrices)" target="_blank">Matrix multiplication - only Matrix product (two matrices)</a></p></li>
<li><p>Prototype: <code>def matrix_mul(m_a, m_b):</code></p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be validated with these requirements in this order</p></li>
<li><p><code>m_a</code> and <code>m_b</code> must be an list of lists of integers or floats:</p>

<ul>
<li>if <code>m_a</code> or <code>m_b</code> is not a list: raise a <code>TypeError</code> exception with the message <code>m_a must be a list</code> or <code>m_b must be a list</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a list of lists: raise a <code>TypeError</code> exception with the message <code>m_a must be a list of lists</code> or <code>m_b must be a list of lists</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is empty (it means: <code>= []</code> or <code>= [[]]</code>): raise a <code>ValueError</code> exception with the message <code>m_a can&#39;t be empty</code> or <code>m_b can&#39;t be empty</code></li>
<li>if one element of those list of lists is not an integer or a float: raise a <code>TypeError</code> exception with the message <code>m_a should contain only integers or floats</code> or <code>m_b should contain only integers or floats</code></li>
<li>if <code>m_a</code> or <code>m_b</code> is not a rectangle (all &lsquo;rows&rsquo; should be of the same size): raise a <code>TypeError</code> exception with the message <code>each row of m_a must be of the same size</code> or <code>each row of m_b must be of the same size</code></li>
</ul></li>
<li><p>If <code>m_a</code> and <code>m_b</code> can&rsquo;t be multiplied: raise a <code>ValueError</code> exception with the message <code>m_a and m_b can&#39;t be multiplied</code></p></li>
<li><p>You are not allowed to import any module</p></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__(&#39;100-matrix_mul&#39;).matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
</code></pre>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>100-matrix_mul.py, tests/100-matrix_mul.txt</code></li>
        </ul>
      </div>

# 7. Lazy matrix multiplication
    
<p>Write a function that multiplies 2 matrices by using the module <a href="https://numpy.org/" title="NumPy" target="_blank">NumPy</a></p>

<p>To install it: <code>pip3 install numpy==1.15.0</code></p>

<ul>
<li>Prototype: <code>def lazy_matrix_mul(m_a, m_b):</code></li>
<li>Test cases should be the same as <code>100-matrix_mul</code> but with new exception type/message</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x07$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__(&#39;101-lazy_matrix_mul&#39;).lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

guillaume@ubuntu:~/0x07$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
guillaume@ubuntu:~/0x07$ 
</code></pre>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt</code></li>
        </ul>

# 8. CPython #3: Python Strings
    
<p><img src="./2c4f2b92514745519f833afdf5bc5f3eaff8c6ca.gif" alt="" style="" />
<br /></p>

<p>Create a function that prints Python strings.</p>

<ul>
<li>Prototype: <code>void print_python_string(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid string, print an error message (see example)</li>
<li>Read: <a href="https://docs.python.org/3.4/howto/unicode.html" title="Unicode HOWTO" target="_blank">Unicode HOWTO</a></li>
</ul>

<p>About:</p>

<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c</code></li>
</ul>

<pre><code>julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL(&#39;./libPython.so&#39;)
lib.print_python_string.argtypes = [ctypes.py_object]
s = &quot;The spoon does not exist&quot;
lib.print_python_string(s)
s = &quot;ложка не существует&quot;
lib.print_python_string(s)
s = &quot;La cuillère n&#39;existe pas&quot;
lib.print_python_string(s)
s = &quot;勺子不存在&quot;
lib.print_python_string(s)
s = &quot;숟가락은 존재하지 않는다.&quot;
lib.print_python_string(s)
s = &quot;スプーンは存在しない&quot;
lib.print_python_string(s)
s = b&quot;The spoon does not exist&quot;
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n&#39;existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
julien@ubuntu:~/0x07. Pyhton Strings$ 
</code></pre>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x07-python-test_driven_development</code></li>
            <li>File: <code>102-python.c</code></li>
        </ul>
      </div>

<em>THE END</em>      



