// -------BURGER------

document.querySelector('.burger').addEventListener('click', function () {
  document.querySelector('.burger', '.menu').classList.toggle('active');
  document.querySelector('.menu').classList.toggle("open");
});

// --------ACCORDION----------

const accordionHeader = document.querySelectorAll('.questions-inner-all-accordions__accordion__header');

accordionHeader.forEach(accordionHeader => {
  accordionHeader.addEventListener('click', event => {
    const currentActiveHeader = document.querySelector('.questions-inner-all-accordions__accordion__header.active');
    if (currentActiveHeader && currentActiveHeader !== accordionHeader) {
      currentActiveHeader.classList.toggle('active');
      currentActiveHeader.nextElementSibling.style.maxHeight = 0;
    }

    accordionHeader.classList.toggle('active');
    const accordionBody = accordionHeader.nextElementSibling;

    if (accordionHeader.classList.contains('active')) {
      accordionBody.style.maxHeight = accordionBody.scrollHeight + 'px';
    } else {
      accordionBody.style.maxHeight = 0;
    }
  });
});

// -----------MODAL-WINDOW------------

window.addEventListener("load", function () {
  const div = document.querySelector(".events-inner__item1");
  const window = document.querySelector(".btn-modal");
  const windowClose = document.querySelector(".close");

  div.addEventListener("click", function () {
    window.classList.toggle("active");
  });

  windowClose.addEventListener("click", function () {
    window.classList.remove("active");

  });
});

window.addEventListener("load", function () {
  const div = document.querySelector(".events-inner__item2");
  const window = document.querySelector(".btn-modal");
  const windowClose = document.querySelector(".close");

  div.addEventListener("click", function () {
    window.classList.toggle("active");
  });

  windowClose.addEventListener("click", function () {
    window.classList.remove("active");

  });
});

window.addEventListener("load", function () {
  const div = document.querySelector(".events-inner__item3");
  const window = document.querySelector(".btn-modal");
  const windowClose = document.querySelector(".close");

  div.addEventListener("click", function () {
    window.classList.toggle("active");
  });

  windowClose.addEventListener("click", function () {
    window.classList.remove("active");

  });
});

window.addEventListener("load", function () {
  const div1 = document.querySelector(".submit");
  const window1 = document.querySelector(".btn-modal2");
  const windowClose1 = document.querySelector(".close2");

  div1.addEventListener("click", function () {
    window1.classList.toggle("active");
  });

  windowClose1.addEventListener("click", function () {
    window1.classList.remove("active");

  });
});

const anchors = document.querySelectorAll('a[href*="#"]');

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()

    const blockID = anchor.getAttribute('href').substr(1)

    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}