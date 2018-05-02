/* Javascript for BooksXBlock. */
function BooksXBlock(runtime, element, initialQuestion) {

    const $element = $(element);

    var author = initialQuestion.author;
    var writtenByAuthor = initialQuestion.written_by_author;
    var notWrittenByAuthor = initialQuestion.not_written_by_author;
    var shuffledTitles = initialQuestion.shuffled_titles;

    var newQuestionHandlerUrl = runtime.handlerUrl(element, 'get_new_question');
    $('.check-answer-btn', $element).click(checkAnswer)
    $('.new-question-btn', $element).click(getNewQuestion)

    function getNewQuestion(){
      $.ajax({
          type: "POST",
          url: newQuestionHandlerUrl,
          data: JSON.stringify({}),
          success: processNewQuestion
      });
    }

    function processNewQuestion(result){
        author = result.author;
        writtenByAuthor = result.written_by_author;
        notWrittenByAuthor = result.not_written_by_author;
        shuffledTitles = result.shuffled_titles;

        displayQuestion();
    }

    function displayQuestion(){
      $('.booksxblock-checkbox', $element).each(function(index) {
        $(this).prop('checked', false);
      })

      $('.answer-message', $element).hide();

      $('.author', $element).text(author)
      $('.booksxblock-answer-text', $element).each(function(index) {
        $(this).text(shuffledTitles[index])
      })
    }

    function checkAnswer(){

      selectedAnswers = [];

      $('.bookxblock-answer-option', $element).each(function(index) {
        chosenAnswer = $('.booksxblock-checkbox', this).prop('checked');

        if(chosenAnswer==true){
          selectedAnswers.push(
            $('.booksxblock-answer-text', this).text()
          )
        }
      })

      wasAnswerCorrect = areTwoStringArraysEqual(notWrittenByAuthor, selectedAnswers);
      $('.answer-message', $element).text(wasAnswerCorrect).show();

    }

    function areTwoStringArraysEqual(firstArray, secondArray){
      a = firstArray.slice(0).sort();
      b = secondArray.slice(0).sort();

      return JSON.stringify(a) === JSON.stringify(b);
    }

    $(function ($) {
        /* Here's where you'd do things on page load. */
        displayQuestion();
    });
}
