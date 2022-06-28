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

# TASKS