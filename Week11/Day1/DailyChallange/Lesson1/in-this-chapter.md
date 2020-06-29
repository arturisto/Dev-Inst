<h1>Templates</h1>
<p>Templates are a way to generate dynamic html code.</p>

This means adding variables, for loops and if statements inside the HTML code.
The template is written in a template language that combines python and HTML.
There are a lot of python modules that can convert template to html code (they’re called template engines), flask use jinja2.

<p>Templates can be written in any extension.</p>

What is in the template ?
Delimiters
There are three types of enclosures in jinja2:
<ul>
<li>Variables: <code>{{ ... }}</code> is used to define expressions, it will just be replaced by their python value.</li>

<li>Statements: <code>{% ... %} </code>is used to define statements (it means if or loops).</li>

<li>Comments: <code>{# #}</code> is used for comments (means it won’t be included in the template output).</li>

</ul>