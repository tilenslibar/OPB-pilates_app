<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Uredi vajo</title>
    <link rel="stylesheet" href="/views/main.css">
</head>
<body>
<div class="container">
    <h1>Uredi vajo</h1>
    <form action="/uredi_vajo" method="post">
        <input type="hidden" name="staro_ime" value="{{vaja.ime}}">
        <label>Ime: <input type="text" name="ime" value="{{vaja.ime}}" required></label><br>
        <label>Opis:
            <textarea name="opis" rows="3" style="width:100%;border:1.5px solid #e8b6d1;border-radius:10px;padding:10px 14px;background:#fff;color:#4d3c2c;margin-bottom:12px;font-size:1em;resize:vertical;box-sizing:border-box;transition:border 0.2s,background 0.2s;">{{vaja.opis}}</textarea>
        </label><br>
        <label>Tip:
            <select name="tip">
                <option value="Sprostitvena" {{'selected' if vaja.tip=='Sprostitvena' else ''}}>Sprostitvena</option>
                <option value="Krepitvena" {{'selected' if vaja.tip=='Krepitvena' else ''}}>Krepitvena</option>
                <option value="Raztezna" {{'selected' if vaja.tip=='Raztezna' else ''}}>Raztezna</option>
            </select>
        </label><br>
        <label>Link: <input type="text" name="link" value="{{vaja.link}}" required></label><br>
        <input type="submit" value="Shrani spremembe">
    </form>
    <br>
    <a href="/vaje">Nazaj na vaje</a>
</div>
</body>
</html>
