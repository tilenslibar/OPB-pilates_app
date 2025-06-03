<!DOCTYPE html>
<html>
<head>
    <title>{{naslov}}</title>
</head>
<body>
    <h1>{{naslov}}</h1>
    <p>{{sporocilo}}</p>
    <form form action="/ustvari_racun" method="post">
        <label>Uporabnisko ime: <input type="text" name="username" required></label><br>
        <label>Geslo: <input type="password" name="password" required></label><br>
    <button type="submit">Prijava</button>
    </form>
</body>
</html>
