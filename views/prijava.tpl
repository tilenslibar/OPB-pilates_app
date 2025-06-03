<!DOCTYPE html>
<html>
<head>
    <title>{{naslov}}</title>
</head>
<body>
    <h1>Prijava</h1>
    <p>{{sporocilo}}</p>

    <form form action="/prijava" method="post">
        <label>Uporabnisko ime: <input type="text" name="username" required></label><br>
        <label>Geslo: <input type="password" name="password" required></label><br>
    <button type="submit">Prijava</button>
    </form>

    <p>Ce se nimas racuna: <a href="ustvari_racun">Ustvari racun</a></p>
</body>
