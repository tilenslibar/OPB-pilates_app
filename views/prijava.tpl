<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="UTF-8">
    <title>{{naslov}}</title>
    <link rel="stylesheet" href="/views/main.css">
</head>
<body>
<div class="container">
    <h1>Prijava</h1>
    <p class="meta-label" style="font-size:1.12em;text-align:center;margin-bottom:18px;">Če še niste prijavljeni, se prijavite z uporabniškim imenom in geslom.</p>
    <form action="/prijava" method="post">
        <label>Uporabniško ime: <input type="text" name="username" required></label><br>
        <label>Geslo: <input type="password" name="password" required></label><br>
        <button type="submit">Prijava</button>
    </form>
    <p class="meta-label" style="font-size:1.04em;text-align:center;margin-top:18px;">Nimate računa? <a href="ustvari_racun">Ustvarite račun</a></p>
</div>
</body>
</html>
