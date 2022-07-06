# Python - Everything is object

<p><img src="./r_208403_QPSN8.jpg" alt="" style="" /><br /></p>

<h2>Background Context</h2>

<p>Now that we understand that everything is an object and have a little bit of knowledge, let&rsquo;s pause and look a little bit closer at how Python works with different types of objects.</p>

<p>BTW, have you ever modified a variable without knowing it or wanting to? I mean:</p>

<pre><code>&gt;&gt;&gt; a = 1
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a = 2
&gt;&gt;&gt; b
1
&gt;&gt;&gt; 
</code></pre>

<p>OK. But what about this?</p>

<pre><code>&gt;&gt;&gt; l = [1, 2, 3]
&gt;&gt;&gt; m = l
&gt;&gt;&gt; l[0] = &#39;x&#39;
&gt;&gt;&gt; m
[&#39;x&#39;, 2, 3]
&gt;&gt;&gt; 
</code></pre>

<p><img src="./giphy.webp" alt="" style="" /><br />
<br /></p>

<p>This project is a little bit different than the usual projects. The first part is only questions about Python&rsquo;s specificity like &ldquo;What would be the result of&hellip;&rdquo;. 
You should <strong>read all documentation first (as usual :))</strong>, then take the time to <strong>think and brainstorm with your peers</strong> about what you think and why. <strong>Try to do this without coding anything for a few hours</strong>.</p>

<p>Trying examples in the Python interpreter will give you most of the answers without having to think about it. <strong>Don&rsquo;t go this route</strong>. First read, then think, then brainstorm together. Only then you can test in the interpreter.</p>

<p>It&rsquo;s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.
The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.</p>

<p>Note that during interviews for Python positions, <strong>you will most likely have to answer to these type of questions</strong>.</p>

<p>All your answers should be only one line in a file. No space before or after the answer.</p>

## Resources

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values" title="9.10. Objects and values" target="_blank">9.10. Objects and values</a> </li>
<li><a href="http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing" title="9.11. Aliasing" target="_blank">9.11. Aliasing</a> </li>
<li><a href="https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types" title="Immutable vs mutable types" target="_blank">Immutable vs mutable types</a> </li>
<li><a href="http://composingprograms.com/pages/24-mutable-data.html#sequence-objects" title="Mutation" target="_blank">Mutation</a> (<em>Only this chapter</em>)</li>
<li><a href="http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists" title="9.12. Cloning lists" target="_blank">9.12. Cloning lists</a> </li>
<li><a href="http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html" title="Python tuples: immutable but potentially changing" target="_blank">Python tuples: immutable but potentially changing</a> </li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Why Python programming is awesome</li>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the built-in mutable types</li>
<li>What are the built-in immutable types</li>
<li>How does Python pass variables to functions</li>
</ul>

--- 
---

<details>
<summary><strong>Show Tasks/Hide Tasks</strong></summary><br>

# TASKS

# 0. Who am I?
   
<p>What function would you use to print the type of an object?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

  </div>

[(answer)](/../0x00-python-hello_world/2-print.py)


# 1. Where are you?

   
<p>How do you get the variable identifier (which is the memory address in the CPython implementation)?</p>

<p>Write the name of the function in the file, without <code>()</code>.</p>

  </div>

[(answer)](./1-answer.txt)


# 2. Right count
   
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 100
</code></pre>

  </div>

[(answer)](./2-answer.txt)


# 3. Right count =
   
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = 89
</code></pre>

  </div>

[(answer)](./3-answer.txt)

# 4. Right count =
   
<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a
</code></pre>

  </div>

[(answer)](./4-answer.txt)

# 5. Right count =+

<p>In the following code, do <code>a</code> and <code>b</code> point to the same object?
Answer with <code>Yes</code> or <code>No</code>.</p>

<pre><code>&gt;&gt;&gt; a = 89
&gt;&gt;&gt; b = a + 1
</code></pre>

  </div>

[(answer)](./5-answer.txt)


# 6. Is equal
   
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Best School&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

  </div>

[(answer)](./6-answer.txt)


# 7. Is the same
    
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Best&quot;
&gt;&gt;&gt; s2 = s1
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

  </div>

[(answer)](./7-answer.txt)


# 8. Is really equal

<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Best School&quot;
&gt;&gt;&gt; s2 = &quot;Best School&quot;
&gt;&gt;&gt; print(s1 == s2)
</code></pre>

  </div>

[(answer)](./8-answer.txt)



#  9. Is really the same
   
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; s1 = &quot;Best School&quot;
&gt;&gt;&gt; s2 = &quot;Best School&quot;
&gt;&gt;&gt; print(s1 is s2)
</code></pre>

  </div>

[(answer)](./9-answer.txt)


# 10. And with a list, is it equal
   
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

  </div>

[(answer)](./10-answer.txt)


# 11. And with a list, is it the same
   
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = [1, 2, 3] 
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

  </div>

[(answer)](./11-answer.txt)

# 12. And with a list, is it really equal
   
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 == l2)
</code></pre>

  </div>
  
[(answer)](./12-answer.txt)



# 13. And with a list, is it really the same
    
<p>What do these 3 lines print?</p>

<pre><code>&gt;&gt;&gt; l1 = [1, 2, 3]
&gt;&gt;&gt; l2 = l1
&gt;&gt;&gt; print(l1 is l2)
</code></pre>

  </div>

[(answer)](./13-answer.txt)


# 14. List append
   
    <p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
</code></pre>

  </div>

  [(answer)](./14-answer.txt)


# 15. List add
    
<p>What does this script print?</p>

<pre><code>l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
</code></pre>

  </div>

  [(answer)](./15-answer.txt)



# 16. Integer incrementation
    
 <p>What does this script print?</p>

<pre><code>def increment(n):
    n += 1

a = 1
increment(a)
print(a)
</code></pre>

  </div>

[(answer)](./16-answer.txt)


# 17. List incrementation
   
<p>What does this script print?</p>

<pre><code>def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
</code></pre>

  </div>

[(answer)](./17-answer.txt)



# 18. List assignation
   
<p>What does this script print?</p>

<pre><code>def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
</code></pre>

  </div>

[(answer)](./18-answer.txt)



# 19. Copy a list object
    
<p>Write a function <code>def copy_list(l):</code> that returns a <strong>copy</strong> of a list.</p>

<ul>
<li>The input list can contain any type of objects</li>
<li>Your file should be maximum 3-line long (no documentation needed)</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__(&#39;19-copy_list&#39;).copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py 
3 19-copy_list.py
guillaume@ubuntu:~/0x09$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[(answer)](./19-copy_list.py)


# 20. Tuple or not?
    
<pre><code>a = ()
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

[(answer)](./20-answer.txt)


# 21. Tuple or not?
  
<pre><code>a = (1, 2)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

[(answer)](./21-answer.txt)



# 22. Tuple or not?
    
<pre><code>a = (1)
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

[(answer)](./22-answer.txt)


# 23. Tuple or not?
    
<pre><code>a = (1, )
</code></pre>

<p>Is <code>a</code> a tuple? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

[(answer)](./23-answer.txt)


# 24. Who I am?
    
<p>What does this script print?</p>

<pre><code>a = (1)
b = (1)
a is b
</code></pre>

  </div>

[(answer)](./24-answer.txt)


# 25. Tuple or not
    
<p>What does this script print?</p>

<pre><code>a = (1, 2)
b = (1, 2)
a is b
</code></pre>

  </div>

[(answer)](./25-answer.txt)


# 26. Empty is not empty
    
<p>What does this script print?</p>

<pre><code>a = ()
b = ()
a is b
</code></pre>

  </div>

[(answer)](./26-answer.txt)


# 27. Still the same?
    
<pre><code>&gt;&gt;&gt; id(a)
139926795932424
&gt;&gt;&gt; a
[1, 2, 3, 4]
&gt;&gt;&gt; a = a + [5]
&gt;&gt;&gt; id(a)
</code></pre>

[(answer)](./27-answer.txt)


<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

# 28. Same or not?
    
<pre><code>&gt;&gt;&gt; a
[1, 2, 3]
&gt;&gt;&gt; id (a)
139926795932424
&gt;&gt;&gt; a += [4]
&gt;&gt;&gt; id(a)
</code></pre>

<p>Will the last line of this script print <code>139926795932424</code>? Answer with <code>Yes</code> or <code>No</code>.</p>

  </div>

[(answer)](./28-answer.txt)



# 29. #pythonic
   
<p>Write a function <code>magic_string()</code> that returns a string &ldquo;BestSchool&rdquo; n times the number of the iteration (see code):</p>

<ul>
<li>Format: see example</li>
<li>Your file should be maximum 4-line long (no documentation needed)</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__(&#39;100-magic_string&#39;).magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[(answer)](./100-magic_string.py)


# 30. Low memory cost
   
<p>Write a class <code>LockedClass</code> with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called <code>first_name</code>.</p>

<ul>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__(&#39;101-locked_class&#39;).LockedClass

lc = LockedClass()
lc.first_name = &quot;John&quot;
try:
    lc.last_name = &quot;Snow&quot;
except Exception as e:
    print(&quot;[{}] {}&quot;.format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] &#39;LockedClass&#39; object has no attribute &#39;last_name&#39;
guillaume@ubuntu:~/0x09$ 
</code></pre>

<p><strong>No test cases needed</strong></p>

  </div>

[(answer)](./101-locked_class.py)

# 31. int 1/3
    
<pre><code>julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
</code></pre>

<p>Assuming we are using a CPython implementation of Python3 with default options/configuration:</p>

<ul>
<li>How many int objects are created by the execution of the first line of the script? (<code>103-line1.txt</code>)</li>
<li>How many int objects are created by the execution of the second line of the script (<code>103-line2.txt</code>)</li>
</ul>

  </div>

  [(answer)](./103-line1.txt) and [(answer)](./103-line2.txt)

# 32. int 2/3
   
<pre><code>julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
</code></pre>

<p>Assuming we are using a CPython implementation of Python3 with default options/configuration:</p>

<ul>
<li>How many int objects are created by the execution of the first line of the script? (<code>104-line1.txt</code>)</li>
<li>How many int objects are created by the execution of the second line of the script (<code>104-line2.txt</code>)</li>
<li>After the execution of line 3, is the int object pointed by <code>a</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>104-line3.txt</code>)</li>
<li>After the execution of line 4, is the int object pointed by <code>b</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>104-line4.txt</code>)</li>
<li>How many int objects are created by the execution of the last line of the script (<code>104-line5.txt</code>)</li>
</ul>

  </div>

[(answer)](./104-line1.txt), [(answer)](./104-line2.txt), [(answer)](./104-line3.txt), [(answer)](./104-line4.txt) and [(answer)](./104-line5.txt)

# 33. int 3/3
   
<pre><code>julien@twix:/tmp/so$ cat int.py 
print(&quot;I&quot;)
print(&quot;Love&quot;)
print(&quot;Python&quot;)
julien@ubuntu:/tmp/so$ 
</code></pre>

<p>Assuming we are using a CPython implementation of Python3 with default options/configuration:</p>

<ul>
<li>Before the execution of line 2 (<code>print(&quot;Love&quot;)</code>), how many int objects have been created and are still in memory? (<code>105-line1.txt</code>)</li>
<li>Why? (optional blog post :))</li>
</ul>

<p>Hint: <code>NSMALLPOSINTS</code>, <code>NSMALLNEGINTS</code></p>

<p><img src="./70f9ea0e969dfcc407a7427aba4786d87a920494.gif" alt="" style="" /></p>

  </div>

  [(answer)](./105-line1.txt)

# 34. Clear strings
    
<pre><code>guillaume@ubuntu:/python3$ cat string.py 
a = &quot;SCHL&quot;
b = &quot;SCHL&quot;
del a
del b
c = &quot;SCHL&quot;
guillaume@ubuntu:/python3$ 
</code></pre>

<p>Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don&rsquo;t spell out the word):</p>

<ul>
<li>How many string objects are created by the execution of the first line of the script? (<code>106-line1.txt</code>)</li>
<li>How many string objects are created by the execution of the second line of the script (<code>106-line2.txt</code>)</li>
<li>After the execution of line 3, is the string object pointed by <code>a</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line3.txt</code>)</li>
<li>After the execution of line 4, is the string object pointed by <code>b</code> deleted? Answer with <code>Yes</code> or <code>No</code> (<code>106-line4.txt</code>)</li>
<li>How many string objects are created by the execution of the last line of the script (<code>106-line5.txt</code>)</li>
</ul>

  </div>

  [(answer)](./106-line1.txt), [(answer)](./106-line2.txt), [(answer)](./106-line3.txt), [(answer)](./106-line4.txt) and [(answer)](./106-line5.txt)

  <em>THE END</em>

  </details>

 
