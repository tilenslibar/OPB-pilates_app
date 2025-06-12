<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{naslov}}</title>
    <link rel="stylesheet" href="/views/main.css">
    <style>
        table {
            border-collapse: collapse;
            width: 70%;
        }
        th, td {
            border: 1px solid #999;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #eee;
        }
    </style>
</head>
<body>
<div class="container">
    <h2>Dodaj novo vajo</h2>
    <form action="/dodaj" method="post" accept-charset="UTF-8">
        <label>Ime:
            <input type="text" name="ime" required placeholder="Npr. Plank, Most, ..." maxlength="60">
        </label><br>
        <label>Opis:
            <textarea name="opis" rows="4" placeholder="Npr. vaja za krepitev trupa, navodila za izvedbo ..." required maxlength="500"></textarea>
        </label><br>
        <label>Tip:
            <select name="tip">
                <option>Sprostitvena</option>
                <option>Krepitvena</option>
                <option>Raztezna</option>
            </select>
        </label><br>
        <label>Link:
            <input type="text" name="link" required placeholder="Npr. https://primer-vaje.si">
        </label><br>
        <input type="submit" value="Dodaj vajo">
    </form>
    <hr>
    <h2>Baza vaj</h2>
    <table style="border-collapse: collapse; width: 95%; margin: 36px auto 28px auto; background: #fff; box-shadow: 0 2px 24px #f9e7d7; border-radius: 18px; overflow: hidden; font-size: 1.04em; letter-spacing: 0.01em; border: 1.5px solid #e8b6d1;">
        <tr>
            <th style="border: 1.5px solid #e8b6d1;">Ime</th>
            <th style="border: 1.5px solid #e8b6d1;">Opis</th>
            <th style="border: 1.5px solid #e8b6d1;">Tip</th>
            <th style="border: 1.5px solid #e8b6d1;">Link</th>
            <th style="border: 1.5px solid #e8b6d1;">Izbriši</th>
            <th style="border: 1.5px solid #e8b6d1;">Uredi</th>
        </tr>
        % for vaja in vaje:
            <tr>
                <td class="vaja-ime" style="border: 1.5px solid #e8b6d1;">{{vaja.ime}}</td>
                <td class="meta-label" style="border: 1.5px solid #e8b6d1;">{{vaja.opis}}</td>
                <td class="meta-label" style="border: 1.5px solid #e8b6d1;">{{vaja.tip}}</td>
                <td class="meta-label" style="border: 1.5px solid #e8b6d1;">
                    <iframe width="300" height="200" src="{{vaja.link}}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                </td>
                <td style="border: 1.5px solid #e8b6d1;">
                    <form action="/izbrisi_vajo" method="post" style="display:inline;">
                        <input type="hidden" name="ime" value="{{vaja.ime}}">
                        <button type="submit" class="delete-btn">X</button>
                    </form>
                </td>
                <td style="border: 1.5px solid #e8b6d1;">
                    <form action="/uredi_vajo" method="get" style="display:inline;">
                        <input type="hidden" name="ime" value="{{vaja.ime}}">
                        <button type="submit" class="edit-btn">✏️</button>
                    </form>
                </td>
            </tr>
        % end
    </table>

    <br>
    <a href="/">Nazaj na domačo stran</a>
</div>
</body>
</html>
