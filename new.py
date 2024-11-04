# HTML template
html_main = '''<!DOCTYPE html>
<html lang="en">
    <head>  
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ann Arbor Skyline Meets</title>
        <link rel="stylesheet" href="css/style.css">
        
    </head>
    <body class="bodyClass">
        <header class="mainHeader" id="Head">
            <h1 tabindex="0" id="h1id">Ann Arbor Skyline</h1>
        </header>
        <main>
            <div class="sectionTitle" id="meetList">
                <h2 tabindex="0" id="meetHeader2">Meets</h2>
                <div id="MeetScroll">
                    <table id="meet-table" class="table">
                    <thead>
                        <tr>
                            <th tabindex="0" id="meetTableHead">Meet Name</th>
                        </tr>
                    </thead>
                        <tbody>
                            {meet_rows}
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div tabindex="0" id="Roster">
                <h2 id="rosterHeader">Roster</h2>
                <div id="binaryRoster" tabindex="0">
                    <section id="women">
                        <h3 tabindex="0">Women's Team</h3>
                        <table id="women-table">
                            <thead>
                                <tr>
                                    <th tabindex="0">Name</th>
                                </tr>
                            </thead>
                            <tbody>
                                {womens_rows}
                            </tbody>
                        </table>
                    </section>

                    <section id="men">
                        <h3 tabindex="0">Men's Team</h3>
                        <table id="men-table">
                            <thead>
                                <tr>
                                    <th tabindex="0">Name</th>
                                </tr>
                            </thead>
                            <tbody>
                                {mens_rows}
                            </tbody>
                        </table>
                    </section>

                </div>
            </div>

            <div id="Meet-Photos">
                <h2 tabindex="0" id="PhotoHeader">Photos</h2>
                    <div id="photos">
                        <table id="photo-table">  
                            <thead>
                                <tr>
                                    <th tabindex="0">Meet Name</th>
                                </tr>
                            </thead>               
                            <tbody id="tablephotos">
                                {photo_rows}
                            </tbody>
                        </table>
                    </div>
            </div>
        </main>
    </body>
</html>    
'''

html_template = '''<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/style.css">
       
        <title>{meet_name} Country Meet</title>
    </head>
    <body class="bodyClass">
        <header class="mainHeader">
                <h1 tabindex="0">{meet_name}</h1>
                <nav>
                    <a id="homeButton" href="index.html">Back to Home</a>
                </nav>
        </header>
        <main>
            <!-- Section for overall team results -->
            <section id="team-results">
                <h2 tabindex="0" id="meetDate">{meet_date}</h2>
                <p tabindex="0" id="meetDesc">{meet_desc}</p>
                <h2 tabindex="0" id="resultsTitle">Overall Team Results</h2>
                <p id="resultsLink"><a href="{team_results_link}">Team results are available here.</a></p>
            </section>
            <!-- Section for athlete table -->
            <section id="athlete-results">
                <h2>Athlete Results</h2>
                <table id="athlete-table">
                    <thead>
                        <tr>
                            <th>Place</th>
                            <th>Profile Picture</th>
                            <th>Name</th>
                            <th>See More</th>
                    </tr>
                    </thead>
                    <tbody>
                        {athlete_rows}
                    </tbody>
                </table>
            </section>
        </main>
    </body>
     <script src=js/imagePlaceholder.js></script>
</html>
    '''


html_images = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meet Photos</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body class="bodyClass">
        <header class="mainHeader">
            <h1 tabindex="0" >{meet_title}</h1>
            <a id="homeButton" href="index.html">Back to Home</a>
        </header>   
        <main>
            <section id="photo-table">
                    <h2 tabindex="0" >All Photos</h2>
                    <div class="photo-grid">
                        {photo_list}
                    </div>
            </section>
        </main>
    </body>
</html>
         
'''

import csv
import os
import re


# Define file names

main_file = "index.html"

    
# Function to generate HTML content based on CSV data

def generate_html_from_csv(csv_file, output_file):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # Extract event data from the CSV
        meet_name = data[0][0]  # Column A - Meet Name
        meet_date = data[1][0]  # Column B - Meet Date
        team_results_link = data[2][0]  # Column C - hyperlink for the team-results section
        meet_desc = data[3]  # Column D - Meet Description
        
        header_index = 0
        for i, row in enumerate(data):
            if row and row[0].strip().lower() == 'place':  # Assuming the first column contains 'Place'
                header_index = i

        # Generate athlete rows
        athlete_rows = ""
        for athlete in data[header_index + 1:]:  # Start from the third row (ignoring header rows)
            athlete_place = athlete[0]  # Column G - athlete-place
            athlete_grade = athlete[1] # Column E - athlete-grade
            athlete_name = athlete[2]  # Column F - athlete-name
            athlete_link = athlete[3]   # Column G - athlete-link
            athlete_time = athlete[4]  # Column H - athlete-time
            athlete_team = athlete[5]  # Column H - athlete-team
            athlete_image = athlete[7]
            
            # if not os.path.exists(f"AthleteImages/{athlete_image}"):
            #     athlete_image ="blankPic.webp"
                       
            # Format the row for each athlete
            athlete_rows += f'''
                <tr>
                    <td>{athlete_place}</td>
                    <td><img src="AthleteImages/{athlete_image}" alt="{athlete_name}" style="width: 60px; height: auto;"></td>  
                    <td><a href="{athlete_link}">{athlete_name}</a></td>
                    <td>
                        <details>
                            <summary>See More</summary>
                            <br>
                            <div class="collapsible-col">Time: {athlete_time}</div><br>
                            <div class="collapsible-col">Grade: {athlete_grade}</div><br>
                            <div class="collapsible-col">Team: {athlete_team}</div>
                        </details>
                    </td>
                    
                </tr>
            '''
        
        # Replace placeholders in the HTML template
        html_content = html_template.format(
            meet_name=meet_name,
            meet_date=meet_date,
            team_results_link=team_results_link,
            athlete_rows=athlete_rows,
            meet_desc=meet_desc
        )

        
        # Write the HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(html_content)

meet_rows = ""
mens_rows = ""
womens_rows = ""

for filename in os.listdir('meets'):
    if filename.endswith('.csv'):
        csv_file = os.path.join('meets', filename)
        name1 = filename[:-4]
        output_file = re.sub(r'[^a-zA-Z0-9_]', '', name1.lower().replace(" ", "_")) + '.html'

        # output_file = f"{filename[:-4]}.html"  # Remove the .csv extension
        generate_html_from_csv(csv_file, output_file)
        print(f"Generated: {output_file}")
        name = f"{filename[:-4]}".replace("_", " ")
        meet_rows += f'''
                <tr>
                    <td><a href="{output_file}">{name}</a></td>
                    
                </tr>
            '''
for filename in os.listdir('athletes/mens_team'):
    if filename.endswith('.csv'):
        csv_file = os.path.join('athletes/mens_team', filename)
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        mens_rows += f'''
                <tr>
                    <td tabindex="0">{data[5][0]}</td>
                </tr>
            '''
for filename in os.listdir('athletes/womens_team'):
    if filename.endswith('.csv'):
        csv_file = os.path.join('athletes/womens_team', filename)
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        womens_rows += f'''
                <tr>
                    <td tabindex="0">{data[5][0]}</td>
                </tr>
            '''

def make_photo_page(output_name, photolist, folder):
    html_photo_content = html_images.format(
        meet_title=folder,
        photo_list = photolist
    )
    # Write the HTML content to a file
    with open(output_name, 'w', encoding='utf-8') as output:
        output.write(html_photo_content)

photo_rows = ""
video_extensions = ['.mov', '.mp4', '.webm', '.ogg']
photo_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

for folder in os.listdir('images'):
    folder_path = os.path.join('images', folder)
    if os.path.isdir(folder_path):
        output_name = folder + '.html'
        photo_rows += f'''
                        <tr>
                            <td><a href="{output_name}">{folder}</a></td>
                        </tr>'''
        photolist = ""
        for photo in os.listdir(folder_path):
            file_path = os.path.join('images', folder, photo)
            file_ext = os.path.splitext(photo)[1].lower()
            file_name = os.path.splitext(photo)[0].lower()
            # if video
            
            if file_ext in photo_extensions:
                photolist += f'<img class="photoList" src="{file_path}" alt="">\n'
        make_photo_page(output_name, photolist, folder)

html_main_content = html_main.format(
    meet_rows=meet_rows,
    womens_rows=womens_rows,
    mens_rows=mens_rows,
    photo_rows=photo_rows
)

with open(main_file, 'w', encoding='utf-8') as output:
            output.write(html_main_content)

        

# Generate the HTML file from the CSV data