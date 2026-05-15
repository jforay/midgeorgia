document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.faq-question').forEach(function (question) {
        question.addEventListener('click', function () {
            var answer = this.nextElementSibling;
            var arrow = this.querySelector('.arrow');
            var isOpen = answer.style.display === 'block';

            document.querySelectorAll('.faq-answer').forEach(function (a) { a.style.display = 'none'; });
            document.querySelectorAll('.faq-question').forEach(function (q) {
                q.classList.remove('active');
                q.querySelector('.arrow').style.transform = 'rotate(0deg)';
            });

            if (!isOpen) {
                answer.style.display = 'block';
                this.classList.add('active');
                arrow.style.transform = 'rotate(180deg)';
            }
        });
    });
});
