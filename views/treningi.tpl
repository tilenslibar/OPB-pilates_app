<!DOCTYPE html>
<html>
<head>
    <title>{{naslov}}</title>
</head>
<body>
    % for trening in treningi:
    <h2>{{trening.ime}}</h2>
    % if len(trening.vaje) > 0:
    <ol>
        % for vaja in trening.vaje:
            <li>
                <div>
                    <h3>{{vaja.ime}}</h3>
                    <strong>opis:</strong> {{vaja.opis}}<br>
                    <strong>tip:</strong> {{vaja.tip}}<br>
                    <strong>link:</strong> <a href="{{vaja.link}}" target="_blank">{{vaja.link}}</a>
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
    % end
    <br>
    <p>Ustvari trening</p>
    <form form action="/dodaj_trening" method="post">
        <label>Ime: <input type="text" name="ime" required></label><br>
        <button type="submit">Dodaj trening</button>
    </form>
    <a href="/">Nazaj na domačo stran</a>
</body>
</html>
