# 2nd Qtr Drill 2
from pyscript import display, document

def result_checker(e):
    document.getElementById('output').innerHTML = ""

    # Define sets for each grade level
    grade7 = {'Mike Velarde', 'Munir Arbison', 'Rodante Marcoleta'}
    grade8 = {'Joshua Ortiz', 'Chezka Robles', 'Faisal Mangondato', 'Paolo Marcoleta'}
    grade9 = {'Lebron James', 'Rodrigo Duterte', 'Chiz Escudero'}
    grade10 = {'Georgina Sarmiento', 'Franco Maglaqui', 'Chester Roxas', 'Joseph Co'}

    # User input value for first and last name
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value

    # Combine first and last name 
    new_member = f_name + " " + l_name

    new_member_set = {new_member}        

    # | combines all the grade levels including the new member of club
    set_members = grade7 | grade8 | grade9 | grade10 | new_member_set
    total_members = len(grade7 | grade8 | grade9 | grade10 | new_member_set)


    members_list = "<br>".join(set_members)

    document.getElementById('result').innerHTML = f'All members:<br> {members_list}'
    display(f'Total members: {total_members}', target='result') 