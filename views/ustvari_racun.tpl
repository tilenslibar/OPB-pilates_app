<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{naslov}}</title>
    <link rel="stylesheet" href="/views/main.css">
</head>
<body>
<div class="container" style="width:90vw;max-width:1500px;margin:0 auto;">
    <h1>{{naslov}}</h1>
    <p class="meta-label" style="font-size:1.12em;text-align:center;margin-bottom:18px;">Vnesite podatke za ustvarjanje računa.</p>
    <form form action="/ustvari_racun" method="post">
        <label>Uporabnisko ime: <input type="text" name="username" required></label><br>
        <label>Geslo: <input type="password" name="password" required></label><br>
        <label>Vloga: 
            <select name="rola" required>
                <option value="trener">Trener</option>
                <option value="uporabnik">Uporabnik</option>
            </select>
        </label><br>
    <button type="submit">Prijava</button>
    </form>
</div>
</body>
</html>
