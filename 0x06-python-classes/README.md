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

# QUIZ


**1.) In this following code, what is <code>User</code>?**

<pre><code>class User:
    id = 89
    name = &quot;no name&quot;
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
</code></pre>


     <ul class="quiz_question_answers" data-question-id="248">
                <li class="">
  <input type="checkbox" name="quiz-answer-1501193339111" id="quiz-answer-1501193339111" data-quiz-question-id="248" data-quiz-answer-id="1501193339111" disabled="disabled" checked="checked" />
  <label for="quiz-answer-1501193339111">
    <p>A class</p>

</label></li>

           <li class="">
  <input type="checkbox" name="quiz-answer-1501193345296" id="quiz-answer-1501193345296" data-quiz-question-id="248" data-quiz-answer-id="1501193345296" disabled="disabled" />
  <label for="quiz-answer-1501193345296">
    <p>A string</p>

</label></li>

           <li class="">
  <input type="checkbox" name="quiz-answer-1501193351736" id="quiz-answer-1501193351736" data-quiz-question-id="248" data-quiz-answer-id="1501193351736" disabled="disabled" />
  <label for="quiz-answer-1501193351736">
    <p>An attribute</p>

</label></li>

         <li class="">
  <input type="checkbox" name="quiz-answer-1501193358123" id="quiz-answer-1501193358123" data-quiz-question-id="248" data-quiz-answer-id="1501193358123" disabled="disabled" />
  <label for="quiz-answer-1501193358123">
    <p>A method</p>

</label></li>

        <li class="">
  <input type="checkbox" name="quiz-answer-1501193367507" id="quiz-answer-1501193367507" data-quiz-question-id="248" data-quiz-answer-id="1501193367507" disabled="disabled" />
  <label for="quiz-answer-1501193367507">
    <p>An instance</p>

</label></li>

      </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
 <div class="quiz_question_item_container" data-role="quiz_question249" data-position="2">
    <div class=" clearfix" id="quiz_question-249">

    <h4 class="quiz_question">