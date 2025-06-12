<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{naslov}}</title>
    <link rel="stylesheet" href="/views/main.css">
</head>
<body>
<div class="container">
    <h2>Ustvari trening</h2>
    <form form action="/dodaj_trening" method="post">
        <label>Ime: <input type="text" name="ime" required></label><br>
        <button type="submit">Dodaj trening</button>
    </form>
    <hr>
    <h2>Treningi</h2>
    % for trening in treningi:
    <div style="border:1px solid #ccc; padding:10px; margin-bottom:20px;">
        <h2 class="trening-ime" style="display:inline-block; margin-right:20px;">{{trening.ime}}</h2>
        <form action="/izbrisi_trening" method="post" style="display:inline;">
            <input type="hidden" name="trening_id" value="{{trening.id}}">
            <button type="submit" class="delete-btn">X</button>
        </form>
        <form action="/uredi_trening" method="get" style="display:inline;">
            <input type="hidden" name="trening_id" value="{{trening.id}}">
            <button type="submit" class="edit-btn">✏️</button>
        </form>
        % if len(trening.vaje) > 0:
        <ol class="vaja-ol">
            % for vaja in trening.vaje:
                <li>
                    <div style="display:flex;align-items:center;gap:10px;">
                        <div>
                            <span class="vaja-ime-trening">{{vaja.ime}}</span>
                            <form action="/izbrisi_vajo_iz_treninga" method="post" style="display:inline; margin-left:4px; vertical-align:middle;">
                                <input type="hidden" name="trening_id" value="{{trening.id}}">
                                <input type="hidden" name="vaja_ime" value="{{vaja.ime}}">
                                <button type="submit" class="delete-btn">X</button>
                            </form>
                            <br>
                            <strong class="meta-label">opis:</strong> <span class="meta-label">{{vaja.opis}}</span><br>
                            <strong class="meta-label">tip:</strong> <span class="meta-label">{{vaja.tip}}</span><br>
                            <strong class="meta-label">link:</strong> <span class="meta-label"><a href="{{vaja.link}}" target="_blank" style="color: #bfae9e; font-style: italic; text-decoration: underline;">{{vaja.link}}</a></span>
                        </div>
                    </div>
                </li>
            % end
            <br>
        </ol>
        % end
        <form form action={{"/dodaj_vajo_treningu/" + str(trening.id)}} method="post">
            <label>Dodaj vajo:
                <select name="vaja_ime">
                    % for vaja in vse_vaje:
                    <option>{{vaja.ime}}</option>
                    % end
                </select>
            </label><br>
            <button type="submit">Dodaj vajo</button>
        </form>
    </div>
    % end
    <br>
    <a href="/">Nazaj na domačo stran</a>
</div>
</body>
</html>
