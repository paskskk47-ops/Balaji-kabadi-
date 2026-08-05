document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle Logic
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggleBtn && navLinks) {
    toggleBtn.addEventListener('click', () => {
      navLinks.classList.toggle('show');
      toggleBtn.classList.toggle('open');
    });
  }

  // FAQ Accordion Logic
  const faqQuestions = document.querySelectorAll('.faq-question');
  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const item = question.parentElement;
      const isActive = item.classList.contains('active');
      
      // Close all open items
      document.querySelectorAll('.faq-item').forEach(faqItem => {
        faqItem.classList.remove('active');
        const answer = faqItem.querySelector('.faq-answer');
        if (answer) {
          answer.style.maxHeight = null;
        }
      });

      // Toggle active state for current item
      if (!isActive) {
        item.classList.add('active');
        const answer = item.querySelector('.faq-answer');
        if (answer) {
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      }
    });
  });
});
