<!DOCTYPE html>
<html>
<head>
    <title>{{naslov}}</title>
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
    <h1>{{naslov}}</h1>
    <table>
        <tr>
            <th>Ime</th>
            <th>Opis</th>
            <th>Tip</th>
        </tr>
        % for vaja in vaje:
            <tr>
                <td>{{vaja.ime}}</td>
                <td>{{vaja.opis}}</td>
                <td>{{vaja.tip}}</td>
            </tr>
        % end
    </table>

    <h2>Dodaj novo vajo</h2>
    <form action="/dodaj" method="post">
        <label>Ime: <input type="text" name="ime" required></label><br>
        <label>Opis: <input type="text" name="opis" required</label><br>
        <label>Tip:
            <select name="tip">
                <option>sprostitvena</option>
                <option>krepitvena</option>
                <option>raztezna</option>
            </select>
        </label><br>
        <input type="submit" value="Dodaj vajo">
    </form>

    <br>
    <a href="/">Nazaj na domačo stran</a>
</body>
</html>
