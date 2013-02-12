<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>Pyramid ${project}</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <style>
      td {
          vertical-align: top;
      }
      #usuari-box {
          background-color: cyan;
      }
  </style>
</head>
<body>
    
<table border="0">
<tr><td>
    <img width="220" height="50" alt="pyramid" src="/static/pyramid-small.png" />
    <center><h1>Projecte ${project}</h1></center>
    <big>Estas a <b>${page}</b></big>
    % if logged_in:
        <p id="usuari-box">Usuari: <b>${logged_in}</b> | [<a href="/logout">Sortir</a>]</p>
    % endif
    <ul>
        <li><a href="/keops">Keops</a></li>
        <li><a href="/temple">Temple</a></li>
        <li><a href="/cairo">Ciutat del Cairo</a></li>
        <li><a href="/">Home</a></li>
   </ul>
   <br/>
</td>
<td>
<div id="imatge">
   ${next.body()}
</div>
</td></tr>
</table>

</body>
</html>
