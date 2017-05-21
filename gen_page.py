# jinja2 is fucked, so build up the pages this way \o/

def gen_user_page(name, points, strings):
    points = str(points)
    int_points = int(points)
    if int_points > 0:
        points = '+' + points
    
    rows = '\n'.join(['<tr>' + '<td>' + s[2] + '</td>' + '<td>' + str(s[3]) + '</td>' + '</tr>' for s in strings])

    html = ['''<!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
          <script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
          <script>
            function submit() {
                var user = document.getElementById('user_name').innerHTML;
                var stext = document.getElementById('text_input').value;
                var spoints = document.getElementById('points_input').value;
                console.log(user + " " + stext + " " + spoints);
                if (stext === "" || spoints === "") {
                  alert('enter values for both!');
                }
               else {
				
			         $.get(  "/API/add_string?points=" + spoints + "&name=" + user + "&text=" + stext,
					function(data) {  alert('success');    location.reload(true);  }
				 );
                }
            };
          </script>


            <style>
                body {
                    text-align: center;
                    font-family: sans-serif;
                }

                th, td {
                    text-align: left;
                }
                .large {
                  font-size: 5em;
                }
                .red {
                  color: red;
                }
                .strings-table {
                  font-size: 1.75em;
                  display: inline-block;
                  margin-left: auto;
                  margin-right: auto;
                  padding-right: 1em;
                  max-height: 800px;
                  overflow-y: scroll;
                }
                .input-table {
                  margin-top: 1em;
                  margin-bottom: 1em;
                  font-size: 2em;
                  display: inline-block;
                  margin-left: auto;
                  margin-right: auto;
                  border-collapse:collapse;
                }
                .input-table th {
                  padding: .25em;
                }
                .input-table th input {
                  font-size: 1em;
                }

                table#t01 {
                  border-collapse:collapse;
                }
                table#t01 td {
                  padding: .25em;
                }
                table#t01 tr:nth-child(even) {
                    background-color: #eee;
                }
                table#t01 tr:nth-child(odd) {
                   background-color:#fff;
                }
            </style>

            <div class="large" id="user_name">''', name, '''</div>
            <div class="large red">''', points, ''' Weeb</div>
            <div>
              <table class="input-table" border="1">
                  <tr>
                      <th>reason</th>
                      <th>point value (max 10)</th>
                      <th>submit</th>
                  </tr>
                  <tr>
                      <th><input type="text" id="text_input"></th>
                      <th><input type="number" id="points_input"></th>
                      <th><button style="font-size: inherit;" onclick="submit();">Submit</button></th>
                  </tr>
              </table>
            </div>

              <table class="strings-table" id="t01" border="1">''', rows, '''

             </table>

        </body>
    </html>
    ''']

    return ''.join(html)


def link_user(user):
	return '<a href="/user/' + user + '">' + user + '</a>'


def gen_leaderboad_page(users):
    rows = '\n'.join(['<tr>' + '<td>' + str(i + 1) + '</td>' + '<td>' + link_user(u[1]) + '</td>' + '<td>' + str(u[2]) + '</td>' + '</tr>' for i, u in enumerate(users)])
    html = ['''<!DOCTYPE html>
        <html>
            <head>
            </head>
            <body>
                <style>
                    body {
                        text-align: center;
                        font-family: sans-serif;
                    }

                    th, td {
                        text-align: left;
                    }
                    .large {
                      font-size: 5em;
                    }
                    .red {
                      color: red;
                    }
                    .strings-table {
                      margin-top: 100px;
                      margin-bottom: 100px;
                      font-size: 3em;
                      display: inline-block;
                      margin-left: auto;
                      margin-right: auto;
                    }
                    .input-table th {
                      padding: .25em;
                    }
                    .input-table th input {
                      font-size: 1em;
                    }

                    table#t01 {
                      border-collapse:collapse;
                    }
                    table#t01 td {
                      padding: .25em;
                    }
                    table#t01 tr:nth-child(even) {
                        background-color: #eee;
                    }
                    table#t01 tr:nth-child(odd) {
                       background-color:#fff;
                    }
                </style>

                  <div class="large red">TOP WEEB SCORES</div>
                  <table class="strings-table" id="t01" border="1">
                    <tr><th>Position</th><th>Name</th><th>Score</th></tr>''', rows, '''

                 </table>

                 <div style="font-size: 3em">To see or add points go to /user/&lt;name&gt; This will automatically add new users.</div>
            </body>
        </html>
    ''']

    return ''.join(html)

