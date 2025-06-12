<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{naslov}}</title>
    <link rel="stylesheet" href="/views/main.css">
    <style>
        table {
            border-collapse: collapse;
            width: 95%;
            margin: 36px auto 28px auto;
            background: #fff;
            box-shadow: 0 2px 24px #f9e7d7;
            border-radius: 18px;
            overflow: hidden;
            font-size: 1.04em;
            letter-spacing: 0.01em;
            border: 1.5px solid #e8b6d1;
        }
        th, td {
            border: 1.5px solid #e8b6d1;
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
    <h1>{{naslov}}</h1>
    <table>
        <tr>
            <th>Username</th>
            <th>Rola</th>
            <th>Zadnja prijava</th>
        </tr>
        % for u in uporabniki:
            <tr>
                <td class="vaja-ime">{{u.username}}</td>
                <td class="meta-label">{{u.role}}</td>
                <td class="meta-label">{{u.last_login}}</td>
            </tr>
        % end
    </table>

    <a href="/">Nazaj na domačo stran</a>
</div>
</body>
</html>
