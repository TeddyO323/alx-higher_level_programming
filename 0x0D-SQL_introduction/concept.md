# Databases
</h1>



<div class="gap formatted-content">
<h2>What are databases?</h2>

<p>First, what are databases for?</p>

<p>Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you&rsquo;re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you&rsquo;re using is stateless or stateful, you will need to persist your data somewhere. That&rsquo;s what databases are for.</p>

<p>Then, why not store your data in flat files, as you did in the &ldquo;Relational databases, done wrong&rdquo; project? A solid database is expected to be <strong>acid</strong>, which means it guarantees:</p>

<ul>
<li><strong>A</strong>tomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.</li>
<li><strong>C</strong>onsistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.</li>
<li><strong>I</strong>solation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. That&rsquo;s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.</li>
<li><strong>D</strong>urability: unplug your server at any time, boot it back up, and it didn&rsquo;t lose any data.</li>
</ul>

<p>Also, a solid database will provide strong performance (because I/O is your bottleneck and databases are I/O, so their performance makes a whole lot more of a difference than the performance of your application&rsquo;s code) and scalability (inserting one user in a collection of 5 users should take about the same time as inserting one user in a collection of 5 billion users).</p>

<h2>ACID is a cool acronym! CRUD is another cool one</h2>

<p>You will definitely run into the concept of &ldquo;CRUD&rdquo; operations. It&rsquo;s just a fancy way to refer to the 4 operations that can be performed on the data itself:</p>

<ul>
<li><strong>C</strong>reate some data;</li>
<li><strong>R</strong>ead some data;</li>
<li><strong>U</strong>pdate some data;</li>
<li><strong>D</strong>estroy some data.</li>
</ul>

<p>Obviously, a database should allow all four. Yes, that&rsquo;s it.</p>

<h2>2+ kinds of databases</h2>

<p>When people talk about databases, they&rsquo;re usually referring to <strong>relational databases</strong> (such as PostgreSQL, MySQL, Oracle, &hellip;); but there are many other kinds of databases used in the industry, which are globally referred to as <strong>&ldquo;NoSQL&rdquo; databases</strong>, even though they can be very different from each other, and serve very various purposes. Also, the name &ldquo;NoSQL&rdquo; comes from <strong>SQL</strong>, which is the name of the syntax used to give orders (CRUD operations, creating and deleting tables, &hellip;) to a relational databases; however, some non-relational databases, which are referred to as &ldquo;NoSQL&rdquo; give the option to use the SQL syntax. Therefore, the term &ldquo;NoSQL&rdquo; is quite controversial to refer to non-relational databases, but it is still widely used.</p>

<p>&ldquo;NoSQL&rdquo; (non-relational) databases have known a boost in popularity, over the last decade or so, so much that there was a point, a few years ago, where people were wondering if they were to replace relational databases entirely. But years later, the market has now solidified, NoSQL databases&rsquo; market share doesn&rsquo;t progress much anymore and is now quite steady. The result: many NoSQL databases have made it into solid maturity, and are used in some very ambitious projects (as well as small ones), but relational databases are still by far the most used in projects, and are not going anywhere after all.</p>

<p>Therefore: it is crucial for a software engineer to know very well how relational databases work, because the odds are very strong that you will encounter them in your career; but it is also very important to get acquainted with the most popular types of NoSQL databases, because the odds that you run into them, however kinda smaller, are pretty strong too.</p>

<h2>SQL</h2>

<p>In order to work with relational databases, you will need to get familiar with SQL syntax. A lot of developers will acknowledge that they find the SQL syntax unpleasantly hard to use, which has some outcomes:</p>

<ul>
<li>Engineers that are comfortable with SQL are very respected in the industry, even more so in this age where data has gotten so valuable. To be honest, the fact that I aced the SQL challenge on my Apple interview is probably a huge reason for me to have gotten the job; it turns out the initial role was a lot about manipulating data.</li>
<li>The fear of SQL explains a lot why non-relational databases got called &ldquo;NoSQL&rdquo;, a bit like if it was a statement, a complain. Non-relational databases push a lot the button of not having to use SQL.</li>
<li>Modern full-fledged frameworks contain tools that are called ORMs, and one of their roles is to abstract away SQL queries (which is good for day-to-day ease of use, but <a href="/rltoken/oH5XoaYgi5KecakIRbXHHA" title="can turn out very dangerous" target="_blank">can turn out very dangerous</a>). We&rsquo;ll cover ORMs more later, but it&rsquo;s worth noting that you do find back-end engineers in the industry who work with relational databases, but never write a line of SQL, which makes them a lot less valuable on a project.</li>
<li>For a beginner, keep in mind that SQL&rsquo;s syntax is a bit hard to wrap your head around, so maybe you should follow a tutorial first. Please don&rsquo;t try to memorize the SQL syntax. I&rsquo;ve used SQL extensively in very advanced cases, on systems with hundreds of millions of records, and I still go on Google each time I need to compose a SQL query.</li>
</ul>

<h2>Some terminology around relational databases</h2>

<p>One good thing about relational databases is that whether they&rsquo;re PostgreSQL, MySQL, Oracle, or other, they&rsquo;ve managed to be pretty consistent across brands. Therefore, not only are their versions of SQL pretty decently similar (at least for CRUD operations), but the terminology they&rsquo;re using are mostly the same.</p>

<p>Say you need to store users. To do that, you create a <strong>table</strong> that is called &ldquo;users&rdquo;.</p>

<p>Your users have 3 pieces of information to store: their &ldquo;id&rdquo;, their &ldquo;login&rdquo;, and their &ldquo;password&rdquo;. Those are called <strong>columns</strong>, and they all have <strong>types</strong>, like <strong>integer</strong> for the &ldquo;id&rdquo;, <strong>varchar(32)</strong> for &ldquo;login&rdquo; (a string of variable length, but maximum 32), and <strong>char(32)</strong> (a string of exactly 32 characters, which is the case for all text encrypted with the md5 algorithm, for instance). The available types may vary heavily from one database &ldquo;brand&rdquo; to the other.</p>

<p>Now, let&rsquo;s add a user in the database with SQL:</p>

<pre><code>INSERT INTO users (login, password) VALUES (&#39;rudy&#39;, &#39;01234567890123456789012345678901&#39;);
</code></pre>

<p>This adds a <strong>row</strong> in the table (sometimes also refered to as a <strong>record</strong>, or more rarely, a <strong>tuple</strong>).</p>

<h2>Why are they called &ldquo;relational&rdquo; databases?</h2>

<p>Historically, the initial reason was that tables used to be called &ldquo;relations&rdquo; (they gather a lot of datas that are &ldquo;related&rdquo; to each other, since they follow the same structure). However, tables are now tables, and the term &ldquo;relation&rdquo; has now been recycled for another use.</p>

<p>A <strong>relation</strong> as used today is something that ties two records together, most often across different tables. For instance, say you have a blog, and you have 2 tables:</p>

<ul>
<li>posts, with the fields id, title and body</li>
<li>comments, with the fields id and body</li>
</ul>

<p>In both tables, the &ldquo;id&rdquo; fields are <strong>primary keys</strong>, because they uniquely identify the row that they belong to (if you say &ldquo;give me the post of id 4&rdquo;, you&rsquo;re sure to be getting only one post).</p>

<p>But how do you know that a given comment is attached to a given post. Well, you add a post<em>id field to the comments table, containing the id of the post you with to attach it to. The post</em>id field is called a <strong>foreign key</strong>, uniquely identifying another&rsquo;s table primary key.</p>

<p>Now that you have that, you can easily identify, from a comment, which post it is attached to; but you can also easily identify, from a post, which comments are attached to it. Just fetch the comments whose post_id field contain the id of the post you had in mind. The fact that you can do that is what is called a relation.</p>

<p>Once you have your relation, you can do pretty advanced things. For instance, you can join tables together while querying them, which will allow you to search for &ldquo;the comments whose posts were published within the last month&rdquo;, for instance (well, provided the posts table has a published_at column of type date, for instance).</p>

<p>Note: you can have a relation between rows of the same table, for instance, a user that is the &ldquo;sponsor&rdquo; of another one, a comment that is a &ldquo;reply&rdquo; of another one, &hellip;</p>

<h2>Some more terminology around relational databases</h2>

<h3>Indexes</h3>

<p>Say you want to get all of the comments that are attached to the post of ID 12:</p>

<pre><code>SELECT * FROM comments WHERE post_id=12;
</code></pre>

<p>If you have millions or billions of comments, having your database extract the comments that match this condition can be amazingly time-consuming. Therefore, you can add an <strong>index</strong> on the comments table, that applies to the post_id column. This will &ldquo;precompute&rdquo; every possible SELECT query with WHERE conditions on this column, which will update themselves every time you modify data, so that those calls are ready to respond very quickly.</p>

<p>Let&rsquo;s complicate things a bit, and say you want to optimize this query:</p>

<pre><code>SELECT * FROM comments WHERE post_id=12 AND published=1;
</code></pre>

<p>Your index on the post_id column might not help much on that query. However, for that query, you can absolutely define an index on multiple column (in this case, the columns post_id and published).</p>

<p>Setting indexes properly is a known quick win to improve performance of relational databases on queries that are performed very often and take a long time to respond (so-called <strong>slow queries</strong>). I can quote at least a dozen occurrences in my career where setting up an index properly boosted a database&rsquo;s performance with minimal effort, the most notable of which allowed us to boost a data migration that was taking ~48 hours, to suddenly complete in about 3 hours.</p>

<h3>Joins</h3>

<p>You can join tables together that have relations between each other, so that you can operate on data across those tables. For instance, I want the titles of all posts that have published comments.</p>

<pre><code>SELECT posts.title FROM posts JOIN comments ON posts.id = comments.post_id WHERE comments.published=1;
</code></pre>

<p>(Note: each post on that query will appear as many times as it has comments, but let&rsquo;s focus on the join for now.)</p>

<p>Performance is dramatically better if you manage to get the database to do most of the work, as opposed to your application, because the database knows most about your data and how to handle it most efficiently. Joins are amazing wins for that, because the other way to get it done is to perform many separate SQL queries, and manipulate that data in your code, which is very inefficient.</p>

<p>Note: you can join tables together across many relations. The largest join in my career was 7-fold, in a database at Apple that contained information about localization projects.</p>

<h2>A NoSQL kind of database: document-based databases</h2>

<p>One particularly popular type of NoSQL database is document-oriented databases, such as MongoDB or CouchDB. One reason they&rsquo;re popular is because their learning curve is very smooth, and they feel natural to use: you just send them JSON documents, much like we&rsquo;ve done in the &ldquo;Relational databases done wrong&rdquo; project, and they make it right when you need to fetch them back. You don&rsquo;t need your JSON documents to have specific fields of specific types, just send whatever JSON you want; the technical word for this is that they are <em>schemaless</em>.</p>

<p>One caveat is that they&rsquo;re much, much harder to scale than relational databases (the data being more &ldquo;formatted&rdquo; in relational databases makes it easier and faster to work with).</p>

<p>Another caveat is that there is some comfort in having the database enforcing a schema (proper columns of proper types, &hellip;); if the database doesn&rsquo;t do it, you can expect that some JSON documents in the collection are not of the schema you expect, and then you have to enforce schema in your code, which means more work. As a result, some document-based databases offer ways to enforce some schema, but I don&rsquo;t believe many developers use it, because it defeats the purpose of having schemaless storage.</p>

<p>Just as relational databases, document-based databases offer a variety of extra features to tune your usage of the data: indexes, joins, &hellip; sometimes even relations!</p>

<p>Document-based databases will be covered towards the end of year 1.</p>

<h2>Another NoSQL kind of database: key-value stores</h2>

<p>Some applications may need very large key-value storage, which you may think of as the persistence of a single huge &ldquo;dictionary&rdquo; structure (the same structure that Ruby calls &ldquo;hash&rdquo;, Python calls &ldquo;dict&rdquo;, PHP calls &ldquo;associative array&rdquo;, Objective C and Swift calls &ldquo;dictionary&rdquo;, &hellip;). An obvious need for that is around caching (if you don&rsquo;t understand why, we&rsquo;ll cover this when we talk about caching). Cassandre, memcached and Redis are popular key-value stores.</p>

<p>As your collection of key-values grows, you may need pretty advanced ways to organize them (and expire them, for instance), so, obviously, each key-value storage solution comes with more advanced tools than just the usual CRUD operations.</p>

<h2>At the intersection of NoSQL and relational</h2>

<p>As mentioned before, NoSQL databases sometimes get closer to relational databases by allowing to be queried using the SQL syntax (like Cassandra and Hypertable); but databases are getting closer also the other way around, as relational databases themselves have started offering some document-based storage.</p>

<p>A mature example of that is PostgreSQL&rsquo;s &ldquo;hstore&rdquo; type, which allows to store JSON data in PostgreSQL, in a way that is queriable. Most recently, this has allowed PostgreSQL to have a certain leg up against their competition of open-source relational databases, because MySQL hasn&rsquo;t been able to ship a similar feature yet, although they&rsquo;re expected too (MySQL development has dramatically slowed down now that they belong to Oracle, which is a direct closed-source competitor; a few years ago, most MySQL contributors went ahead to create another open-source database called MariaDB, which never really became mainstream, so maybe there won&rsquo;t ever be document-based storage in MySQL, actually).</p>

<h2>What NoSQL storage do I need?</h2>

<p>NoSQL databases address all kinds of requirements, and therefore the ways they work are dramatically different. Here&rsquo;s a really accurate map of the various solutions: http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis</p>

<p>Note: in year 1, your main project must be done using a relational database, and we&rsquo;ll cover document-oriented databases (probably MongoDB) and key-value stores (probably Redis) towards the end of the year.</p>

</div>
