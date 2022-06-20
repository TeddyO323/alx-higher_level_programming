# Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/errors.html" title="Errors and Exceptions" target="_blank">Errors and Exceptions</a> </li>
<li><a href="https://www.youtube.com/watch?v=7vbgD-3s-w4" title="Learn to Program 11 Static &amp; Exception Handling" target="_blank">Learn to Program 11 Static &amp; Exception Handling</a> (<em>starting at minute 7</em>)</li>
</ul>

# Learning Objectives

<ul>
<li>Why Python programming is awesome ‎</li>
<li>What&rsquo;s the difference between errors and exceptions</li>
<li>What are exceptions and how to use them</li>
<li>When do we need to use exceptions</li>
<li>How to correctly handle an exception</li>
<li>What&rsquo;s the purpose of catching exceptions</li>
<li>How to raise a builtin exception</li>
<li>When do we need to implement a clean-up action after an exception</li>
</ul>

---
# TASKS

# 0. Safe list printing
   
 
<p>Write a function that prints <code>x</code> elements of a list.</p>

<ul>
<li>Prototype: <code>def safe_print_list(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All elements must be printed on the same line followed by a new line.</li>
<li><code>x</code> represents the number of elements to print</li>
<li><code>x</code> can be bigger than the length of <code>my_list</code></li>
<li>Returns the real number of elements printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__(&#39;0-safe_print_list&#39;).safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print(&quot;nb_print: {:d}&quot;.format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>0-safe_print_list.py</code></li>
        </ul>
      </div>

# 1. Safe printing of an integers list
  
<p>Write a function that prints an integer with <code>&quot;{:d}&quot;.format()</code>.</p>

<ul>
<li>Prototype: <code>def safe_print_integer(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__(&#39;1-safe_print_integer&#39;).safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = &quot;School&quot;
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$ 
</code></pre>

<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>1-safe_print_integer.py</code></li>
        </ul>
      </div>

# 2. Print and count integers
   
 
<p>Write a function that prints the first <code>x</code> elements of a list and only integers.</p>

<ul>
<li>Prototype: <code>def safe_print_list_integers(my_list=[], x=0):</code></li>
<li><code>my_list</code> can contain any type (integer, string, etc.)</li>
<li>All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).</li>
<li><code>x</code> represents the number of elements to access in <code>my_list</code></li>
<li><code>x</code> can be bigger than the length of <code>my_list</code> - if it&rsquo;s the case, an exception is expected to occur</li>
<li>Returns the real number of integers printed</li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print an integer</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>len()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__(&#39;2-safe_print_list_integers&#39;).safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

my_list = [1, 2, 3, &quot;School&quot;, 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print(&quot;nb_print: {:d}&quot;.format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print(&quot;nb_print: {:d}&quot;.format(nb_print))

guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File &quot;./2-main.py&quot;, line 14, in &lt;module&gt;
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File &quot;/0x05/2-safe_print_list_integers.py&quot;, line 7, in safe_print_list_integers
    print(&quot;{:d}&quot;.format(my_list[i]), end=&quot;&quot;)
IndexError: list index out of range
guillaume@ubuntu:~/0x05$ 
</code></pre>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>2-safe_print_list_integers.py</code></li>
        </ul>
      </div>

# 3. Integers division with debug
  
<p>Write a function that divides 2 integers and prints the result.</p>

<ul>
<li>Prototype: <code>def safe_print_division(a, b):</code></li>
<li>You can assume that <code>a</code> and <code>b</code> are integers</li>
<li>The result of the division should print on the <code>finally:</code> section preceded by <code>Inside result:</code></li>
<li>Returns the value of the division, otherwise: <code>None</code></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You have to use <code>&quot;{}&quot;.format()</code> to print the result</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__(&#39;3-safe_print_division&#39;).safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print(&quot;{:d} / {:d} = {}&quot;.format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print(&quot;{:d} / {:d} = {}&quot;.format(a, b, result))

guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$ 
</code></pre>

  </div>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>3-safe_print_division.py</code></li>
        </ul>

# 4. Divide a list
  

 <p>Write a function that divides element by element 2 lists.</p>

<ul>
<li>Prototype: <code>def list_division(my_list_1, my_list_2, list_length):</code></li>
<li><code>my_list_1</code> and <code>my_list_2</code> can contain any type (integer, string, etc.)</li>
<li><code>list_length</code> can be bigger than the length of both lists</li>
<li>Returns a new list (length = <code>list_length</code>) with all divisions</li>
<li>If 2 elements can&rsquo;t be divided, the division result should be equal to <code>0</code></li>
<li>If an element is not an integer or float:

<ul>
<li>print: <code>wrong type</code></li>
</ul></li>
<li>If the division can&rsquo;t be done (<code>/0</code>):

<ul>
<li>print: <code>division by 0</code></li>
</ul></li>
<li>If <code>my_list_1</code> or <code>my_list_2</code> is too short

<ul>
<li>print: <code>out of range</code></li>
</ul></li>
<li>You have to use <code>try: / except: / finally:</code> </li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__(&#39;4-list_division&#39;).list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print(&quot;--&quot;)

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, &quot;H&quot;, 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

guillaume@ubuntu:~/0x05$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
guillaume@ubuntu:~/0x05$ 
</code></pre>

  
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>4-list_division.py</code></li>
        </ul>
      </div>


# 5. Raise exception
    
 <p>Write a function that raises a type exception.</p>

<ul>
<li>Prototype: <code>def raise_exception():</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__(&#39;5-raise_exception&#39;).raise_exception

try:
    raise_exception()
except TypeError as te:
    print(&quot;Exception raised&quot;)

guillaume@ubuntu:~/0x05$ ./5-main.py
Exception raised
guillaume@ubuntu:~/0x05$ 
</code></pre>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>5-raise_exception.py</code></li>
        </ul>
      </div>

# 6. Raise a message
   

<p>Write a function that raises a name exception with a message.</p>

<ul>
<li>Prototype: <code>def raise_exception_msg(message=&quot;&quot;):</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__(&#39;6-raise_exception_msg&#39;).raise_exception_msg

try:
    raise_exception_msg(&quot;C is fun&quot;)
except NameError as ne:
    print(ne)

guillaume@ubuntu:~/0x05$ ./6-main.py
C is fun
guillaume@ubuntu:~/0x05$ 
</code></pre>

  
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>6-raise_exception_msg.py</code></li>
        </ul>

# 7. Safe integer print with error message
    

 <p>Write a function that prints an integer.</p>

<ul>
<li>Prototype: <code>def safe_print_integer_err(value):</code></li>
<li><code>value</code> can be any type (integer, string, etc.)</li>
<li>The integer should be printed followed by a new line</li>
<li>Returns <code>True</code> if <code>value</code> has been correctly printed (it means the <code>value</code> is an integer)</li>
<li>Otherwise, returns <code>False</code> and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
<li>You have to use <code>&quot;{:d}&quot;.format()</code> to print as integer</li>
<li>You are not allowed to use <code>type()</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__(&#39;100-safe_print_integer_err&#39;).safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

value = &quot;School&quot;
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print(&quot;{} is not an integer&quot;.format(value))

guillaume@ubuntu:~/0x05$ ./100-main.py
89
-89
Exception: Unknown format code &#39;d&#39; for object of type &#39;str&#39;
School is not an integer
guillaume@ubuntu:~/0x05$ ./100-main.py 2&gt; /dev/null
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>100-safe_print_integer_err.py</code></li>
        </ul>
      </div>

# 8. Safe function
   
 <p>Write a function that executes a function safely.  </p>

<ul>
<li>Prototype: <code>def safe_function(fct, *args):</code></li>
<li>You can assume <code>fct</code> will be always a pointer to a function</li>
<li>Returns the result of the function,</li>
<li>Otherwise, returns <code>None</code> if something happens during the function and prints in <code>stderr</code> the error precede by <code>Exception:</code></li>
<li>You have to use <code>try: / except:</code> </li>
</ul>

<pre><code>guillaume@ubuntu:~/0x05$ cat 101-main.py
#!/usr/bin/python3
safe_function = __import__(&#39;101-safe_function&#39;).safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print(&quot;result of my_div: {}&quot;.format(result))

result = safe_function(my_div, 10, 0)
print(&quot;result of my_div: {}&quot;.format(result))


def print_list(my_list, len):
    i = 0
    while i &lt; len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print(&quot;result of print_list: {}&quot;.format(result))

guillaume@ubuntu:~/0x05$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
guillaume@ubuntu:~/0x05$ ./101-main.py 2&gt; /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
guillaume@ubuntu:~/0x05$ 
</code></pre>

 
 <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>101-safe_function.py</code></li>
        </ul>

# 9. ByteCode -&gt; Python #4
   
 <p>Write the Python function <code>def magic_calculation(a, b):</code> that does exactly the same as the following Python bytecode:</p>

<pre><code>  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        &gt;&gt;   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (&gt;)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 (&#39;Too far&#39;)
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     &gt;&gt;   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        &gt;&gt;   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     &gt;&gt;   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        &gt;&gt;  102 POP_BLOCK

 13     &gt;&gt;  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
</code></pre>

<ul>
<li>Tip: <a href="/rltoken/-eivu0w172OUPm-iCeKgtw" title="Python bytecode" target="_blank">Python bytecode</a></li>
</ul>

  </div>

 
<p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>102-magic_calculation.py</code></li>
        </ul>
      </div>


# 10. CPython #2: PyFloatObject
    
    <p>Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.<br />
<br />
<img src="https://github.com/TeddyO323/photos/blob/main/070710952984e4d126e114405cefe83af2271ce8.gif?raw=true" alt="" style="" />
<br />
Python lists:</p>

<ul>
<li>Prototype: <code>void print_python_list(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyListObject</code>, print an error message (see example)</li>
</ul>

<p>Python bytes:</p>

<ul>
<li>Prototype: <code>void print_python_bytes(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Line &ldquo;first X bytes&rdquo;: print a maximum of 10 bytes</li>
<li>If <code>p</code> is not a valid <code>PyBytesObject</code>, print an error message (see example)</li>
</ul>

<p>Python float:</p>

<ul>
<li>Prototype: <code>void print_python_float(PyObject *p);</code></li>
<li>Format: see example</li>
<li>If <code>p</code> is not a valid <code>PyFloatObject</code>, print an error message (see example)</li>
<li>Read <code>/usr/include/python3.4/floatobject.h</code></li>
</ul>

<p>About:</p>

<ul>
<li>Python version: 3.4</li>
<li>You are allowed to use the C standard library</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c</code></li>
<li>You are not allowed to use the following macros/functions:

<ul>
<li><code>Py_SIZE</code></li>
<li><code>Py_TYPE</code></li>
<li><code>PyList_Size</code></li>
<li><code>PyList_GetItem</code></li>
<li><code>PyBytes_AS_STRING</code></li>
<li><code>PyBytes_GET_SIZE</code></li>
<li><code>PyBytes_AsString</code></li>
<li><code>PyBytes_AsStringAndSize</code></li>
<li><code>PyFloat_AS_DOUBLE</code></li>
<li><code>PySequence_GetItem</code></li>
<li><code>PySequence_Fast_GET_SIZE</code></li>
<li><code>PySequence_Fast_GET_ITEM</code></li>
<li><code>PySequence_ITEM</code></li>
<li><code>PySequence_Fast_ITEMS</code></li>
</ul></li>
</ul>

<p><strong>NOTE</strong>:</p>

<ul>
<li>The python script will be launched using the <code>-u</code> option (Force <code>stdout</code> to be unbuffered).</li>
<li>It is <strong>strongly</strong> advised to either use <code>setbuf(stdout, NULL);</code> or <code>fflush(stdout)</code> in your C functions IF you choose to use <code>printf</code>. The reason to that is that Python<code>s</code>print<code>and libC</code>s <code>printf</code> don&rsquo;t share the same buffer, and the output can appear disordered.</li>
</ul>

<pre><code>julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ cat 103-tests.py 
#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL(&#39;./libPython.so&#39;)
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b&quot;Hello&quot;
lib.print_python_bytes(s);
b = b&#39;\xff\xf8\x00\x00\x00\x00\x00\x00&#39;;
lib.print_python_bytes(b);
b = b&#39;What does the \&#39;b\&#39; character do in front of a string literal?&#39;;
lib.print_python_bytes(b);
l = [b&#39;Hello&#39;, b&#39;World&#39;]
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b&quot;School&quot;, &quot;Betty&quot;]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = [&quot;School&quot;]
lib.print_python_list(l)
lib.print_python_bytes(l);
f = 3.14
lib.print_python_float(f);
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l);
lib.print_python_float(l);
lib.print_python_list(f);
julien@ubuntu:~/CPython$ ./103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: ??
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the &#39;b&#39; character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
[.] float object info
  value: 6.0
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: School
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
[.] float object info
  value: 3.14
[-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793]
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: float
[.] float object info
  value: -1.0
Element 1: float
[.] float object info
  value: -0.1
Element 2: float
[.] float object info
  value: 0.0
Element 3: float
[.] float object info
  value: 1.0
Element 4: float
[.] float object info
  value: 3.14
Element 5: float
[.] float object info
  value: 3.14159
Element 6: float
[.] float object info
  value: 3.14159265
Element 7: float
[.] float object info
  value: 3.141592653589793
[.] float object info
  [ERROR] Invalid Float Object
[*] Python list info
  [ERROR] Invalid List Object
julien@ubuntu:~/CPython$
</code></pre>

  <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-higher_level_programming</code></li>
            <li>Directory: <code>0x05-python-exceptions</code></li>
            <li>File: <code>103-python.c</code></li>
        </ul>
      </div>

