"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
import random
from itertools import chain

from xblock.core import XBlock
from xblock.fields import Scope, Dict
from xblock.fragment import Fragment

from .authors import AUTHORS

class BooksXBlock(XBlock):
    """
    A simple XBlock to check one's knowledge about writers
    and the books they authored.
    """

    question = Dict(
        default=0, scope=Scope.user_state,
        help="A question presented to the user",
    )


    def prepare_new_question(self):
        """
        Generates new question for the learner e.g.

        {
            'author': 'William Shakespeare'
            'written_by_author': ['Hamlet', 'Macbeth'],
            'not_written_by_author': ['Harry Potter and the Half-Blood Prince', 'War and Peace']
            'shuffled_titles': ['War and Peace', 'Macbeth', 'Hamlet', 'Harry Potter and the Half-Blood Prince']
        }

        The total count of books included in written_by_author and in not_written_by_author lists
        has to be equal to 4.
        """

        how_many_authored = random.randint(1, 3)
        how_many_not_authored = 4 - how_many_authored

        random.shuffle(AUTHORS)

        chosen_author, works_of_author = AUTHORS[0]

        random.shuffle(works_of_author)
        written_by_author = works_of_author[:how_many_authored]

        works_of_others = list(
            chain.from_iterable([works for author, works in AUTHORS[1:]])
        )
        random.shuffle(works_of_others)
        not_written_by_author = works_of_others[:how_many_not_authored]

        all_answers = list(chain(written_by_author, not_written_by_author))
        random.shuffle(all_answers)

        question = {
            'author': chosen_author,
            'written_by_author': written_by_author,
            'not_written_by_author': not_written_by_author,
            'shuffled_titles': all_answers
        }

        self.question = question


    def resource_string(self, path):
        """
        Handy helper for getting resources from our kit.
        """
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the BooksXBlock, shown to students
        when viewing courses.
        """

        self.prepare_new_question()

        html = self.resource_string("static/html/booksxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/booksxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/booksxblock.js"))
        frag.initialize_js('BooksXBlock', self.question)
        return frag


    @XBlock.json_handler
    def get_new_question(self, data, suffix=''):
        """
        A handler for a front-end request to generate new question.
        """
        self.prepare_new_question()
        return self.question

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("BooksXBlock",
             """<booksxblock/>
             """),
            ("Multiple BooksXBlock",
             """<vertical_demo>
                <booksxblock/>
                <booksxblock/>
                <booksxblock/>
                </vertical_demo>
             """),
        ]
