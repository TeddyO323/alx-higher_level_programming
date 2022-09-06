# 0x12. JavaScript - Warm up

<h2>Background Context</h2>

<p>JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:</p>

<ul>
<li>Scripting (same as we did with Python)</li>
<li>Web front-end</li>
</ul>

<p>For the moment, and for learning all basic concepts of this language, we will do some scripting.
After, we will make our AirBnB project dynamic by using Javascript and JQuery.</p>

<p><img src="./Javascript-535.png.jpeg" alt="" loading='lazy' style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics" title="Writing JavaScript Code" target="_blank">Writing JavaScript Code</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables" title="Variables" target="_blank">Variables</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures" title="Data Types" target="_blank">Data Types</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics" title="Operators" target="_blank">Operators</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence" title="Operator Precedence" target="_blank">Operator Precedence</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling" title="Controlling Program Flow" target="_blank">Controlling Program Flow</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions" title="Functions" target="_blank">Functions</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects" title="Objects and Arrays" target="_blank">Objects and Arrays</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects" title="Intrinsic Objects" target="_blank">Intrinsic Objects</a> </li>
<li><a href="http://darrenderidder.github.io/talks/ModulePatterns/#/" title="Module patterns" target="_blank">Module patterns</a> </li>
<li><a href="https://www.youtube.com/watch?v=sjyJBL5fkp8" title="var, let and const" target="_blank">var, let and const</a> </li>
<li><a href="https://www.youtube.com/watch?v=vZBCTc9zHtI" title="JavaScript Tutorial" target="_blank">JavaScript Tutorial</a> </li>
<li><a href="https://github.com/mbeaudru/modern-js-cheatsheet" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to run a JavaScript script</li>
<li>How to create variables and constants</li>
<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
<li>What are all the data types available in JavaScript</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use <code>while</code> and <code>for</code> loops</li>
<li>How to use <code>break</code> and <code>continue</code> statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any <code>return</code> statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>

<h2>More Info</h2>

<h3>Install Node 14</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="https://github.com/standard/semistandard" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

  </div>
</div>

---

## TASKS

### 0. First constant, first print
    
      
<p>Write a script that prints &ldquo;JavaScript is amazing&rdquo;:</p>

<ul>
<li>You must create a constant variable called <code>myVar</code> with the value &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./0-javascript_is_amazing.js)

---

  ### 1. 3 languages
 
<p>Write a script that prints 3 lines:</p>

<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./1-multi_languages.js)

---

  ### 2. Arguments
    
<p>Write a script that prints a message depending of the number of arguments passed:</p>

<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>If only one argument is passed to the script, print &ldquo;Argument found&rdquo;</li>
<li>Otherwise, print &ldquo;Arguments found&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p>Reference: <a href="/rltoken/5kTYi3rxb6KM1_pivm-tXg" title="process.argv" target="_blank">process.argv</a></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>


  </div>

[Answer](./2-arguments.js)

---

### 3. Value of my argument
   
<p>Write a script that prints the first argument passed to it:</p>

<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>length</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./3-value_argument.js)

---

###  4. Create a sentence
  
<p>Write a script that prints two arguments passed to it, in the following format: &ldquo;<first argument> is <second argument>&rdquo;</p>

<ul>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./4-concat.js)

---

### 5. An Integer
 
<p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>

<ul>
<li>If the argument can&rsquo;t be converted to an integer, print &ldquo;Not a number&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>try/catch</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js &quot;89&quot;
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./5-to_integer.js)

---

 ### 6. Loop to languages
    
<p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>

<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use any <code>if/else</code> statement</li>
<li>You can use only one <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./6-multi_languages_loop.js)

---

### 7. I love C
   
<p>Write a script that prints <code>x</code> times &ldquo;C is fun&rdquo;</p>

<ul>
<li>Where <code>x</code> is the first argument of the script</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing number of occurrences&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You can use only two <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./7-multi_c.js)

---

### 8. Square
  
<p>Write a script that prints a square</p>

<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing size&rdquo;</li>
<li>You must use the character <code>X</code> to print the square</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./8-square.js)

---

### 9. Add
    
<p>Write a script that prints the addition of 2 integers</p>

<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: <code>function add(a, b)</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./9-add.js)

---

### 10. Factorial
   
     
<p>Write a script that computes and prints a factorial</p>

<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of <code>NaN</code> is <code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./10-factorial.js)

---

### 11. Second biggest!
   
<p>Write a script that searches the second biggest integer in the list of arguments.</p>

<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print <code>0</code></li>
<li>If the number of arguments is 1, print <code>0</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./11-second_biggest.js)

---

### 12. Object
    
<p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>

<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: &#39;object&#39;,
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: &#39;object&#39;, value: 12 }
{ type: &#39;object&#39;, value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>


  </div>

[Answer](./12-object.js)

---

### 13. Add file
    
     
<p>Write a function that returns the addition of 2 integers.</p>

<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be <code>add</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p><a href="http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html" title="Tip" target="_blank">Tip</a> </p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require(&#39;./13-add&#39;).add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./13-add.js)

---

### 14. Const or not const
   
      
<p>Write a file that modifies the value of <code>myVar</code> to <code>333</code></p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require(&#39;./100-let_me_const&#39;)
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$ 
</code></pre>

<p><img src="./4ae30fb44f708dbb3abc211b784db614e615ca21.gif" alt="" loading='lazy' style="" /></p>

<p>Do you get it? Tweet! Post! Talk about it!</p>

<p>Hint: Scope</p>

<p><strong>This exercise doesn&rsquo;t pass <code>semistandard</code></strong> so don&rsquo;t worry about it.</p>

  </div>

[Answer](./100-let_me_const.js)

---

### 15. Call me Moby
    
<p>Write a function that executes <code>x</code> times a function.</p>

<ul>
<li>The function must be visible from outside</li>
<li>Prototype: <code>function (x, theFunction)</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require(&#39;./101-call_me_moby&#39;).callMeMoby;
callMeMoby(3, function () {
  console.log(&#39;C is fun&#39;);
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./101-call_me_moby.js)

---

### 16. Add me maybe
   
<p>Write a function that increments and calls a function.</p>

<ul>
<li>The function must be visible from outside</li>
<li>Prototype: <code>function (number, theFunction)</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require(&#39;./102-add_me_maybe&#39;).addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log(&#39;New value: &#39; + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./102-add_me_maybe.js)

---

### 17. Increment object
   
<p>Update this script by adding a new function <code>incr</code> that increments the integer <code>value</code>.</p>

<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: &#39;object&#39;,
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: &#39;object&#39;, value: 12 }
{ type: &#39;object&#39;, value: 13, incr: [Function] }
{ type: &#39;object&#39;, value: 14, incr: [Function] }
{ type: &#39;object&#39;, value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

[Answer](./103-object_fct.js)

---

<em>THE END</em>


