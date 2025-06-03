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
            <th>Username</th>
            <th>Rola</th>
            <th>Zadnja prijava</th>
        </tr>
        % for u in uporabniki:
            <tr>
                <td>{{u.username}}</td>
                <td>{{u.role}}</td>
                <td>{{u.last_login}}</td>
            </tr>
        % end
    </table>

    <a href="/">Nazaj na domačo stran</a>
</body>
</html>
