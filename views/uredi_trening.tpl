<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Uredi trening</title>
    <link rel="stylesheet" href="/views/main.css">
</head>
<body>
<div class="container" style="width:90vw;max-width:1500px;margin:0 auto;">
    <h1>Uredi trening</h1>
    <form action="/uredi_trening" method="post">
        <input type="hidden" name="trening_id" value="{{trening.id}}">
        <label>Ime: <input type="text" name="ime" value="{{trening.ime}}" required></label><br>
        <input type="submit" value="Shrani spremembe">
    </form>
    <br>
    <a href="/treningi">Nazaj na treninge</a>
</div>
</body>
</html>
