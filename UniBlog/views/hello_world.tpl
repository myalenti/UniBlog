<html>
<title></title>
<body>
hello {{username}}
<p>
    %for thing in things:
    <li>{{thing}}</li>
    %end
</p>
<p>
    <form action="/favorite_fruit" method="POST">
        What is your Favorite Fruit?
        <input type="text" name="fruit" size="40" value=""><br>
        <input type="submit" value="Submit"></input>
    </form>
</p>
</body>
</html>


