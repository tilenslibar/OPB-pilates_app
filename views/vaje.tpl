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
            <th>Težavnost</th>
            <th>Vrsta</th>
        </tr>
        % for vaja in vaje:
            <tr>
                <td>{{vaja['ime']}}</td>
                <td>{{vaja['opis']}}</td>
                <td>{{vaja['tezavnost']}}</td>
                <td>{{vaja['vrsta']}}</td>
            </tr>
        % end
    </table>
    <a href="/">Nazaj na domačo stran</a>
</body>
</html>
