from django.http import HttpResponse

def indexPageView(request) :
    htmlOutput = """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap" rel="stylesheet">

        <style>
            body {
                font-family: 'Ubuntu', sans-serif;
                background-color: black;
                color: white;
            }

            h1 {
                text-align: center;
                color: red;
                font-size: 4rem;
            }

            h2 {
                text-align: center;
                color: lightgreen;
                margin: 30px auto;
            }

            table {
                margin: auto;
                width: 75%;
                text-align: center;
            }

            table, td {
                border: 1px solid white;
                border-collapse: collapse;
            }

            th {
                border: 2px solid black;
                border-collapse: collapse;
            }

            th {
                font-size: 1.3rem;
                padding: 5px;
                background-color: white;
                color: black;
            }

            td {
                padding: 5px 0;
            }

            #header-image {
                background-image: url('https://attorneygeneral.utah.gov/wp-content/uploads/2018/08/jonathan-wilson-rosas-pena-539091-unsplash-850x500.jpg');
                background-size: auto 100%;
                height: 400px;
                background-repeat: no-repeat;
                background-position: center;
            }

            a {
                color: white;
            }

            #source {
                text-align: center;
                margin-top: 20px;
            }

            p, h3 {
                text-align: center;
                margin: 20px;
            }

            h3 {
                color: lightblue;
            }
        </style>
        
        <h1>Combat Human Trafficking TODAY</h1>

        <div id="header-image">
        </div>

        <p>Defined: Human trafficking is a modern-day form of slavery involving the illegal trade of people for exploitation or commercial gain.</p>

        <h2>Check the list and make a difference</h2>

        <table class="table table-bordered table-hover table-condensed">
        <thead><tr><th title="Field #1">date_missing</th>
        <th title="Field #2">last_name</th>
        <th title="Field #3">first_name</th>
        <th title="Field #4">age_at_missing</th>
        <th title="Field #5">city</th>
        <th title="Field #6">state</th>
        <th title="Field #7">gender</th>
        <th title="Field #8">race</th>
        </tr></thead>
        <tbody><tr>
        <td>10/30/2009</td>
        <td>Sharmarice</td>
        <td>Halima</td>
        <td >14</td>
        <td>Granger</td>
        <td>UT</td>
        <td>F</td>
        <td>W</td>
        </tr>
        <tr>
        <td>10/16/2015</td>
        <td>Martinez</td>
        <td>Kimberly</td>
        <td >16</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>F</td>
        <td>M</td>
        </tr>
        <tr>
        <td>07/23/2004</td>
        <td>Gomez</td>
        <td>Brenda</td>
        <td >3</td>
        <td>Logan</td>
        <td>UT</td>
        <td>F</td>
        <td>H</td>
        </tr>
        <tr>
        <td>05/25/2003</td>
        <td>Bishop</td>
        <td>Acacia</td>
        <td >1</td>
        <td>Salt Lake City</td>
        <td>UT</td>
        <td>F</td>
        <td>W</td>
        </tr>
        <tr>
        <td>08/03/2020</td>
        <td>Salazar</td>
        <td>Maria</td>
        <td >14</td>
        <td>Snowville</td>
        <td>UT</td>
        <td>F</td>
        <td>H</td>
        </tr>
        <tr>
        <td>04/09/2020</td>
        <td>Hernandez-Soto</td>
        <td>Peggy</td>
        <td >6</td>
        <td>Ogden</td>
        <td>UT</td>
        <td>F</td>
        <td>H</td>
        </tr>
        <tr>
        <td>06/24/2021</td>
        <td>Jimenez</td>
        <td>Lucero</td>
        <td >14</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>F</td>
        <td>H</td>
        </tr>
        <tr>
        <td>11/08/2013</td>
        <td>Colindres-Avila</td>
        <td>Yuris</td>
        <td >17</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>F</td>
        <td>M</td>
        </tr>
        <tr>
        <td>07/15/2021</td>
        <td>Harris</td>
        <td>Kandis</td>
        <td >16</td>
        <td>Salt Lake City</td>
        <td>UT</td>
        <td>F</td>
        <td>W</td>
        </tr>
        <tr>
        <td>07/30/2006</td>
        <td>Seal</td>
        <td>Jaydan</td>
        <td >1</td>
        <td>Garleys Wash</td>
        <td>UT</td>
        <td>M</td>
        <td>W</td>
        </tr>
        <tr>
        <td>06/13/2018</td>
        <td>Lizarraga</td>
        <td>Jose</td>
        <td >13</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>M</td>
        <td>H</td>
        </tr>
        <tr>
        <td>04/23/2020</td>
        <td>Cortez Trujillo</td>
        <td>Eztli</td>
        <td >21</td>
        <td>North Ogden</td>
        <td>UT</td>
        <td>M</td>
        <td>H</td>
        </tr>
        <tr>
        <td>10/25/2017</td>
        <td>Fowles</td>
        <td>Juan</td>
        <td >15</td>
        <td>Lehi</td>
        <td>UT</td>
        <td>M</td>
        <td>M</td>
        </tr>
        <tr>
        <td>08/20/2012</td>
        <td>Garcia</td>
        <td>Isai</td>
        <td >17</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>M</td>
        <td>M</td>
        </tr>
        <tr>
        <td>09/01/2015</td>
        <td>Smith</td>
        <td>Macin</td>
        <td >17</td>
        <td>St. George</td>
        <td>UT</td>
        <td>M</td>
        <td>W</td>
        </tr>
        <tr>
        <td>01/26/2006</td>
        <td>Sisco-Ramirez</td>
        <td>Jose</td>
        <td >4</td>
        <td>West Valley City</td>
        <td>UT</td>
        <td>M</td>
        <td>M</td>
        </tr>
        </tbody></table>

        <p id="source">Copy sourced from <a href="https://attorneygeneral.utah.gov/initiatives/human-trafficking/">https://attorneygeneral.utah.gov/initiatives/human-trafficking/</p>
        """
    return HttpResponse(htmlOutput) 