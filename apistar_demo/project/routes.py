from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes

from project.views import data, get_students, get_students_id

routes = [
    # API to create Polls
    #Route('/create_poll', 'POST', create_poll),
    # API to add choices to the polls
    #Route('/create_choices', 'POST', create_choices),
    Route('/students','GET', get_students),
    Route('/students/id/{student_id}','GET', get_students_id)
    ]
