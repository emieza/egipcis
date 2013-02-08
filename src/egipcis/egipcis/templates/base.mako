<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>Pyramid ${project}</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
</head>
<body>
    <h1>Projecte ${project}</h1>
    <big>Estas a <b>${page}</b></big>
    <ul>
        <li><a href="/pagina1">pagina1</a></li>
        <li><a href="/pagina2">pagina2</a></li>
        <li><a href="/admin">admin page</a></li>
   </ul>

   ${next.body()}
   
</body>
</html>
