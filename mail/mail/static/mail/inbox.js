document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', deliver);

  // By default, load the inbox
  load_mailbox('inbox');
});

function observe(emailer) {
  fetch(`/emails/${emailer}`)
  .then(response => response.json())
  .then(mail => {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#main-email-content').style.display = 'block';
    document.querySelector('#main-email-content').innerHTML = `
    <strong>From: </strong>${mail.sender}<br>
    <strong>To: </strong>${mail.recipients}<br>
    <strong>Subject: </strong>${mail.subject}<br>
    <strong>Timestamp: </strong>${mail.timestamp}<br>
    <hr>
    ${mail.body}<br><br>
    `
    if (mail.read === false) {
      fetch(`/emails/${mail.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
    }

    if (mail.archived) {
      archiveStatus = 'Remove From Archive';
    } else {
      archiveStatus = 'Add To Archive';
    }

    const respondButtonElement = document.createElement('button');
    const responseHTML = 'Respond';
    const responseClass = 'btn btn-primary';
    let re = mail.subject;
    let reSplit = re.split(' ', 1)[0]

    respondButtonElement.className = responseClass;
    respondButtonElement.innerHTML = responseHTML;
    respondButtonElement.addEventListener('click', function() {
      compose_email();
      document.querySelector('#compose-recipients').value = mail.sender;

      if (reSplit === 'Re:') {
        document.querySelector('#compose-subject').value = `${mail.subject}`;
      } else {
        document.querySelector('#compose-subject').value = `Re: ${mail.subject}`;
      }

      document.querySelector('#compose-body').value = `On ${mail.timestamp} ${mail.sender} wrote:\n${mail.body}`;
    });
    document.querySelector('#main-email-content').append(respondButtonElement);

    const buttonElement = document.createElement('button');
    const yesClass = 'btn btn-warning';
    const noClass = 'btn btn-info';
    buttonElement.className = mail.archived ? yesClass : noClass;
    buttonElement.innerHTML = archiveStatus;
    buttonElement.addEventListener('click', function() {
      fetch(`/emails/${mail.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: !mail.archived
        })
      })
      .then(function() {
        load_mailbox('archive');
      })
    });
    document.querySelector('#main-email-content').append(buttonElement);
  });
}

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#main-email-content').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#main-email-content').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(mail => {
      mail.forEach(listedMail => {
        const atSymbol = listedMail.sender.indexOf('@');
        const element = document.createElement('div');
        element.style.cursor = "pointer";
        console.log(listedMail);
        element.innerHTML = `
          <h3>${listedMail.sender.slice(0, atSymbol)}</h3><h5>${listedMail.subject}</h5><h6>${listedMail.timestamp}</h6>
          <hr>
        `;

        if (listedMail.read) {
          element.className = 'p-3 mb-2 bg-secondary text-black';
        } else {
          element.className = 'p-3 mb-2 bg-white text-dark';
        }

        element.addEventListener('click', function() {
          observe(listedMail.id)
        });
      document.querySelector('#emails-view').append(element);
      })

  });
}

function deliver(consoleMsg) {
  consoleMsg.preventDefault();
  const recievers = document.querySelector('#compose-recipients').value;
  const topic = document.querySelector('#compose-subject').value;
  const main_content = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recievers,
        subject: topic,
        body: main_content
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('delivered');
  });
}

